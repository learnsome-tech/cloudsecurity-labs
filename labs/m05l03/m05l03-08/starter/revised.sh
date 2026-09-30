# The revised plan: what changes, then what the guardrails say.
jq -r '.resource_changes[]
  | "\(.change.actions | join("+"))  \(.address)"' plan-fixed.json
python3 guard.py plan-fixed.json
echo "exit code $?"
