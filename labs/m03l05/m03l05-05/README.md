# m03l05-05 · What verification must check, and two attacks

**Lesson:** [Supply Chain Security: SBOMs & Cosign Signing](https://learnsome.tech/learn/cloudsecurity-course/m03l05) (lesson 3.5, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can produce and query CycloneDX SBOMs, sign and verify an image digest the way cosign does, and roll out signature enforcement as a controlled change.

In the lesson: Verification has two halves, and an admission controller has to do both. The admit function first checks the signature over the payload with the public key. Then it checks that the digest inside the signed payload is the digest the tag points to right now. Three cases. The original image passes both. Next, an attacker with push rights builds a new image and moves the tag to it. The signature is still perfectly valid, but it is for a different digest, so the image is rejected. A check of the signature alone would have let it through. Finally, the attacker edits the payload to name the new digest. Now the digests match, but the signature no longer verifies, because producing a new one needs the private key. That is the whole guarantee: only the key holder can bind a name to a digest.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/sign.sh`](starter/sign.sh)
- [`starter/verify.sh`](starter/verify.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-05/starter`
2. Read `verify.sh` the way the lesson builds it:
   - Lines 1–13: The admit function first checks
   - Lines 14–16: Three cases
   - Lines 17–20: an attacker with push rights
   - Lines 21–22: the attacker edits the payload
3. Run it: `bash verify.sh`.
4. Check it from the repository root: `./check m03l05-05`.

## Expected output

```text
original image: signed digest matches, admit
tag moved to a new image: valid signature for another digest, reject
payload edited to match: signature does not verify, reject
```

## How to check

`./check m03l05-05` copies `starter/` into a scratch directory and runs `bash verify.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
