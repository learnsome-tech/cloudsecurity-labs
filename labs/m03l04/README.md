# m03l04 · Software Composition Analysis with Trivy

Module 3: CI/CD Security & Shift-Left Automation · lesson 3.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m03l04)

**Goal:** You can match pinned dependencies against OSV advisory ranges, gate a Trivy report with severity thresholds and expiring waivers, and place composition analysis within the four Cs of cloud native security.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l04-02](m03l04-02/) | A pinned lockfile and where each pin came from | Read along |
| [m03l04-03](m03l04-03/) | One advisory in OSV format | Read along |
| [m03l04-04](m03l04-04/) | Matching pinned versions against advisory ranges | Graded |
| [m03l04-05](m03l04-05/) | A gate with severity and expiring waivers | Graded |
| [m03l04-07](m03l04-07/) | Trivy at each layer | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Move the pins and the dates

1. Pin requests==2.31.0 and rerun sca_match.py. Which finding remains, and why?
2. Set urllib3 to 2.0.3. Predict which pair of OSV events matches, then run it.
3. Change the waiver to exp:2026-12-31 and rerun sca_gate.py. What changed?
4. Add CVE-2023-32681 to .trivyignore with no date. Is that a good waiver? Why not?

> **Hint:** The lockfile pins urllib3 separately: bumping requests does not move it until pip-compile runs again.

## Check yourself

- You bump requests to 2.31.0 in the lockfile and leave the other pins alone. Why does the urllib3 finding stay?
- Why must a scanner read every introduced and fixed pair in an OSV range, rather than only the first fixed version?
- A waiver for a high finding carried an expiry date that has now passed. What does the gate do, and why is that the behaviour you want?
- Your images are patched and the lockfile is clean, but the cluster API server is reachable from the internet. What does the four Cs model say about that?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
