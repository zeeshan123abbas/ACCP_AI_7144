#!/bin/bash
# Lab 12 - smoke test: is the site alive and healthy? Usage: bash smoke-test.sh <url>

URL=$1

# Step 1: call /health and keep only the HTTP status code
STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL/health")

# Step 2: pass (exit 0) only on 200, otherwise fail (exit 1) and stop the release
if [ "$STATUS" = "200" ]; then
  echo "PASS: $URL/health returned 200"
  exit 0
else
  echo "FAIL: $URL/health returned $STATUS"
  exit 1
fi
