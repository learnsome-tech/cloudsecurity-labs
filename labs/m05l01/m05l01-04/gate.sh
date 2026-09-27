# Cloud Security & DevSecOps Engineering — lesson m05l01 — Static IaC Scanning: Linting Terraform with Checkov
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l01
# © LearnSome.tech
# The pipeline step: scan, keep the exit code, let the runner decide.
for tf in network.tf.json network-fixed.tf.json; do
  echo "scanning $tf"
  python3 check_sg.py "$tf"
  echo "exit code $?"
done
