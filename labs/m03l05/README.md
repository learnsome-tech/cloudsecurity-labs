# m03l05 · Supply Chain Security: SBOMs & Cosign Signing

Module 3: CI/CD Security & Shift-Left Automation · lesson 3.5 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m03l05)

**Goal:** You can produce and query CycloneDX SBOMs, sign and verify an image digest the way cosign does, and roll out signature enforcement as a controlled change.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l05-02](m03l05-02/) | Writing a CycloneDX SBOM from the lockfile | Graded |
| [m03l05-03](m03l05-03/) | Answering a new advisory from stored SBOMs | Graded |
| [m03l05-04](m03l05-04/) | Signing a digest the way cosign does | Graded |
| [m03l05-05](m03l05-05/) | What verification must check, and two attacks | Graded |
| [m03l05-06](m03l05-06/) | The same flow with cosign | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Attack your own verifier

1. In verify.sh, delete the digest check. Predict which attack is now admitted, then run it.
2. Generate a fresh key pair after signing. What happens to the original image, and why?
3. Add sboms/batch.cdx.json with urllib3 2.0.7 and predict the jq verdict first.
4. Run make_sbom.py twice and compare serial numbers; change one pin and compare again.

> **Hint:** A valid signature over a payload says nothing about which digest the tag points to now.

## Check yourself

- An attacker with registry push rights moves the 1.4.2 tag to a new image. Why would a check that only verifies the signature let it through?
- Why can a stored SBOM answer a new advisory without rescanning every image, including for images that turn out not to be affected?
- What does the payload cosign signs contain, and why does it name a digest rather than a tag?
- An admission policy that fails closed is switched straight to enforce, and the signing infrastructure becomes unreachable. What change management step was skipped?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
