# Cloud Security & DevSecOps Engineering — lesson m03l02 — Pre-Commit Secret Scanning with Gitleaks & Entropy
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l02
# © LearnSome.tech
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
export GIT_AUTHOR_DATE=2026-04-01T09:00Z GIT_COMMITTER_DATE=2026-04-01T09:00Z
git init -q -b main svc && cd svc
git config user.name "Dev" && git config user.email dev@example.com

echo "API_TOKEN = \"exmp_$(python3 ../fake_token.py)\"  # fake" > client.py
git add client.py && git commit -qm "Add API client"
echo 'API_TOKEN = os.environ["EXMP_TOKEN"]' > client.py
git commit -qam "Read the token from the environment"

echo "in the working tree: $(grep -c exmp_ client.py) matches"
echo "commits that added or removed a token:"
git log -G 'exmp_[A-Za-z0-9]{32}' --format='  %h %s'
echo "whole history, as gitleaks reads it:"
git log -p -U0 | python3 ../scan_staged.py
