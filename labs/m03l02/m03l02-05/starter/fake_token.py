import random
rng = random.Random(7)
alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789"
print("".join(rng.choice(alphabet) for _ in range(32)))
