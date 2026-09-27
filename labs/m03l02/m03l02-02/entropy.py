# Cloud Security & DevSecOps Engineering — lesson m03l02 — Pre-Commit Secret Scanning with Gitleaks & Entropy
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l02
# © LearnSome.tech
import math, random
from collections import Counter

def shannon(s):
    n = len(s)
    return sum(-c / n * math.log2(c / n) for c in Counter(s).values())

rng = random.Random(42)           # fixed seed: the same fake token every run
b62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
fake_token = "".join(rng.choice(b62) for _ in range(32))

samples = [
    ("english words", "correcthorsebatterystaple"),
    ("placeholder", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    ("git commit id", "9fceb02d0ae598e95dc970b74767f19372d61af8"),
    ("uuid", "123e4567-e89b-12d3-a456-426614174000"),
    ("random base62", fake_token),
]
for label, s in samples:
    print(f"{label:14} {len(s):2} chars  {shannon(s):.2f} bits per char")
