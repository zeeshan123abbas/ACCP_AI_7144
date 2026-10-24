#!/usr/bin/env bash
# Create a merge conflict ON PURPOSE, so you learn to fix it calmly.
mkdir -p conflict-demo && cd conflict-demo
git init -q

# 1. Starting point: one line of text
echo "Welcome to our website" > welcome.txt
git add . && git commit -q -m "feat: add welcome text"

# 2. Branch "ali" changes the SAME line
git switch -q -c ali
echo "Welcome to Ali's website" > welcome.txt
git commit -q -am "feat: personalise welcome (Ali)"

# 3. Meanwhile main also changes that SAME line
git switch -q main
echo "Welcome to the Tech Club website" > welcome.txt
git commit -q -am "feat: rename to Tech Club"

# 4. Merge -> CONFLICT, because Git cannot choose between the two lines
git merge ali

# 5. Look at the file. Git added markers:
#    <<<<<<< HEAD          (your branch: main)
#    Welcome to the Tech Club website
#    =======
#    Welcome to Ali's website
#    >>>>>>> ali           (the branch being merged)
cat welcome.txt

# 6. FIX: write the final text you want and delete ALL marker lines
echo "Welcome to the Tech Club website by Ali" > welcome.txt

# 7. Tell Git it is solved, then finish the merge
git add welcome.txt
git commit -q -m "merge: combine welcome text from ali"
git log --oneline --graph
