# Cloud Security & DevSecOps Engineering — lesson m03l02 — Pre-Commit Secret Scanning with Gitleaks & Entropy
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l02
# © LearnSome.tech
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
git init -q -b main svc && cd svc
git config user.name "Dev" && git config user.email dev@example.com
cat > .git/hooks/pre-commit <<'EOF'
#!/bin/sh
git diff --cached -U0 | python3 ../scan_staged.py
EOF
chmod +x .git/hooks/pre-commit

tok=$(python3 ../fake_token.py)          # random, seeded, fake
echo "API_TOKEN = \"exmp_$tok\"  # fake" > client.py
git add client.py
git commit -qm "Add API client" 2>&1 || echo "commit refused, exit $?"
git log --oneline 2>/dev/null || echo "no commits yet"

git commit -q --no-verify -m "Add API client" && echo "committed anyway"
git log --format=%s
