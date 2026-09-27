# Cloud Security & DevSecOps Engineering — lesson m05l04 — Continuous IaC Drift Detection & State Protection
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l04
# © LearnSome.tech
# Nightly drift job. In production the check is the real command:
#   terraform plan -detailed-exitcode -input=false -lock=false
# which exits 0 for no changes, 1 for an error, 2 for changes present.
check() {
  python3 drift.py "$1" > report.txt 2>&1
  case $? in
    0) echo "$1: clean" ;;
    2) echo "$1: drift, ticket opened for the owning team"
       cat report.txt ;;
    *) echo "$1: check failed, status unknown, paging on-call"
       tail -n 1 report.txt ;;
  esac
}
check describe-security-groups.json
check describe-never-arrived.json
