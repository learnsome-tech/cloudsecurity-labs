# m03l05-04 · Signing a digest the way cosign does

**Lesson:** [Supply Chain Security: SBOMs & Cosign Signing](https://learnsome.tech/learn/cloudsecurity-course/m03l05) (lesson 3.5, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can produce and query CycloneDX SBOMs, sign and verify an image digest the way cosign does, and roll out signature enforcement as a controlled change.

In the lesson: Now signing. Cosign is not installed here, but the cryptography underneath is standard, so this script does the same steps with openssl. First, a trimmed image manifest. An image's digest really is the S H A two fifty six of its manifest bytes, which is why a digest cannot be moved the way a tag can. Next comes the payload cosign actually signs, in the simple signing format: the repository, the manifest digest, and a fixed type string. Then a key pair on the P two fifty six curve, which is the key type cosign generates, a signature over the payload using S H A two fifty six, and a check with the public key. Openssl prints verified OK. With real cosign, the private key is encrypted with a password, and the signature is pushed to the registry beside the image.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/sign.sh`](starter/sign.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-04/starter`
2. Read `sign.sh` the way the lesson builds it:
   - Lines 1–8: First, a trimmed image manifest
   - Lines 9–15: Next comes the payload
   - Lines 16–21: Then a key pair
3. Run it: `bash sign.sh`.
4. Check it from the repository root: `./check m03l05-04`.

## Expected output

```text
signed sha256:7e5f112c6d43c2d7f31e428ab628e76fa099f9ab1fc6b4d6b49b00e0cfc57036
Verified OK
```

## How to check

`./check m03l05-04` copies `starter/` into a scratch directory and runs `bash sign.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
