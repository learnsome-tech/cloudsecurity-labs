# Exercises — Static IaC Scanning: Linting Terraform with Checkov

Lesson `m05l01` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l01)

## Exercise 1: Extend the check and the gate

1. Add a group with protocol "-1", ports 0 to 0, from 0.0.0.0/0. Predict, then run check_sg.py
2. Give exposes_ssh a port argument and add CKV_AWS_25, the same test for RDP on port 3389
3. Make gate.sh stop at the first file that fails and print that file's name

> **Hint**: Ports 0 to 0 do not contain 22, so only the protocol test can catch it. In bash, test $? straight after the scan.


---

© LearnSome.tech · support@iwantto.learnsome.tech
