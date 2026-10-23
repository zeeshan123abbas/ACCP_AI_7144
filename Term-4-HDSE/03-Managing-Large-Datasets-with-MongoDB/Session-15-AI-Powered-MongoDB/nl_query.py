"""pip install pymongo openai   set OPENAI_API_KEY   then: python nl_query.py "average marks per city" """
import json
import os
import sys

from openai import OpenAI
from pymongo import MongoClient

ALLOWED = {"$match", "$group", "$sort", "$project", "$limit", "$count", "$unwind", "$addFields"}
SCHEMA = "Collection students: {name: str, city: str, age: int, batch: str, marks: {react: int, node: int, mongo: int}, skills: [str], active: bool}"


def generate_pipeline(question: str) -> list:
    client = OpenAI()
    resp = client.chat.completions.create(
        model=os.getenv("AI_MODEL", "gpt-4o-mini"),
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": f"You write MongoDB aggregation pipelines. {SCHEMA}. "
                                          'Reply only as JSON: {"pipeline": [...]}. Use only read-only stages.'},
            {"role": "user", "content": question[:300]},
        ],
    )
    return json.loads(resp.choices[0].message.content)["pipeline"]


def validate(pipeline: list) -> list:
    if not isinstance(pipeline, list) or not pipeline:
        raise ValueError("Pipeline must be a non-empty list")
    for stage in pipeline:
        if len(stage) != 1 or next(iter(stage)) not in ALLOWED:
            raise ValueError(f"Stage not allowed: {stage}")
    return pipeline + [{"$limit": 50}]


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "average mongo marks per city, highest first"
    pipeline = validate(generate_pipeline(question))
    print("Pipeline:", json.dumps(pipeline, indent=2))
    with MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017")) as c:
        for row in c.campus.students.aggregate(pipeline):
            print(row)
