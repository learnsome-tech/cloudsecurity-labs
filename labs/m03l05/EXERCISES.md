# Exercises — Supply Chain Security: SBOMs & Cosign Signing

Lesson `m03l05` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l05)

## Exercise 1: Attack your own verifier

1. In verify.sh, delete the digest check. Predict which attack is now admitted, then run it.
2. Generate a fresh key pair after signing. What happens to the original image, and why?
3. Add sboms/batch.cdx.json with urllib3 2.0.7 and predict the jq verdict first.
4. Run make_sbom.py twice and compare serial numbers; change one pin and compare again.

> **Hint**: A valid signature over a payload says nothing about which digest the tag points to now.


---

© LearnSome.tech · support@iwantto.learnsome.tech
