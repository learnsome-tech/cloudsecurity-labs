# Cloud Security & DevSecOps Engineering — lesson m03l02 — Pre-Commit Secret Scanning with Gitleaks & Entropy
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l02
# © LearnSome.tech
import random
rng = random.Random(7)
alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789"
print("".join(rng.choice(alphabet) for _ in range(32)))
