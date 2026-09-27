# Cloud Security & DevSecOps Engineering — lesson m05l03 — Enforcing OPA Guardrails on Terraform Plan Payloads
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l03
# © LearnSome.tech
# The revised plan: what changes, then what the guardrails say.
jq -r '.resource_changes[]
  | "\(.change.actions | join("+"))  \(.address)"' plan-fixed.json
python3 guard.py plan-fixed.json
echo "exit code $?"
