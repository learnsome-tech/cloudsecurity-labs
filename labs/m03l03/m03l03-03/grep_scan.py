# Cloud Security & DevSecOps Engineering — lesson m03l03 — Static Application Security Testing with Semgrep
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l03
# © LearnSome.tech
import re, sys

# "execute(" followed later on the line by %, +, .format( or an f-string
RISKY = re.compile(r'execute\(.*(%|\+|\.format\(|f")')

for number, line in enumerate(open(sys.argv[1]), start=1):
    if RISKY.search(line):
        print(f"{sys.argv[1]}:{number}  {line.strip()}")
