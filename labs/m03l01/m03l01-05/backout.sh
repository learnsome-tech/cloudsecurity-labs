# Cloud Security & DevSecOps Engineering — lesson m03l01 — Shift-Left Security Principles & Automated Pipeline Gates
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l01
# © LearnSome.tech
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
export GIT_AUTHOR_DATE=2026-03-02T10:00Z GIT_COMMITTER_DATE=2026-03-02T10:00Z
git init -q -b main infra && cd infra
git config user.name "Priya Shah" && git config user.email priya@example.com

echo "allow 198.51.100.0/24 tcp/443" > egress-allow.txt
git add egress-allow.txt && git commit -qm "Egress: payments API only"

echo "allow 0.0.0.0/0 tcp/443" > egress-allow.txt
git commit -qa -m "CHG-1042: open egress for vendor webhooks" \
  -m "Approved-by: Sam Okafor
Backout: git revert, no restart needed"

git -c user.name="On-call" revert --no-edit HEAD >/dev/null
git log --format='%h %an: %s%n%(trailers:key=Approved-by,key=Backout)'
cat egress-allow.txt
