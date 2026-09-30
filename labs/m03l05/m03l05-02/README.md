# m03l05-02 · Writing a CycloneDX SBOM from the lockfile

**Lesson:** [Supply Chain Security: SBOMs & Cosign Signing](https://learnsome.tech/learn/cloudsecurity-course/m03l05) (lesson 3.5, module 3: CI/CD Security & Shift-Left Automation) · Pro  
**Check:** Graded

## Goal

You can produce and query CycloneDX SBOMs, sign and verify an image digest the way cosign does, and roll out signature enforcement as a controlled change.

In the lesson: Syft or Trivy would normally write this file, and neither is installed here, so this is a few lines of Python writing the same kind of CycloneDX document from the lockfile. The pins come from the regular expression you met in the last lesson. Each component gets a type, a name, a version and a purl, a package URL: pkg, a colon, the ecosystem, then the name and version. Purls are how scanners and inventory tools agree on which package is meant. The document header says CycloneDX, spec version one point five. The serial number is a UUID derived from the lockfile, so the same input always gives the same id. The metadata names the image this bill of materials describes. Then the file is written and each package URL is printed. Keep each S B O M with the release it describes. One written for a different build is worse than none.

## Files

- [`starter/make_sbom.py`](starter/make_sbom.py): the listing from the lesson
- [`starter/requirements.txt`](starter/requirements.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `make_sbom.py` the way the lesson builds it:
   - Lines 1–7: Each component gets
   - Lines 8–17: The document header says
   - Lines 18–21: Then the file is written
3. Notes from the lesson:
   - Line 11: Derived from the lockfile: same input, same serial number
4. Run it: `python3 make_sbom.py`.
5. Check it from the repository root: `./check m03l05-02`.

## Expected output

```text
CycloneDX 1.5 urn:uuid:425f015a-8dea-5df4-ac34-2e893df43eb9
  pkg:pypi/certifi@2024.7.4
  pkg:pypi/charset-normalizer@3.3.2
  pkg:pypi/idna@3.7
  pkg:pypi/requests@2.28.2
  pkg:pypi/urllib3@1.26.15
```

## How to check

`./check m03l05-02` copies `starter/` into a scratch directory and runs `python3 make_sbom.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
