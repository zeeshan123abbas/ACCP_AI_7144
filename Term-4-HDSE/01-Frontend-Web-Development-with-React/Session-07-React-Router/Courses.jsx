import { Link, useNavigate, useParams } from "react-router-dom";

const data = [
  { id: "1", name: "React", sessions: 12 },
  { id: "2", name: "Node.js", sessions: 12 },
  { id: "3", name: "MongoDB", sessions: 16 },
];

export function Courses() {
  return (
    <>
      <h1>Courses</h1>
      <ul>
        {data.map((c) => (
          <li key={c.id}>
            <Link to={`/courses/${c.id}`}>{c.name}</Link>
          </li>
        ))}
      </ul>
    </>
  );
}

export function CourseDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const course = data.find((c) => c.id === id);

  if (!course) return <p>Course {id} does not exist.</p>;

  return (
    <>
      <h1>{course.name}</h1>
      <p>{course.sessions} sessions</p>
      <button onClick={() => navigate(-1)}>⬅ Back</button>
      <button onClick={() => navigate("/courses", { replace: true })}>All courses</button>
    </>
  );
}
