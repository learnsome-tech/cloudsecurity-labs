# m04l01 · Container Hardening: Distroless & Rootless

Module 4: Container & Kubernetes Runtime Defense · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m04l01)

**Goal:** You can build a distroless, non-root image and prove from process status and ID maps what an attacker inside it can and cannot do.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-02](m04l01-02/) | A two-stage Dockerfile ending in distroless | Checker |
| [m04l01-03](m04l01-03/) | Command injection with and without a shell | Graded |
| [m04l01-04](m04l01-04/) | Reading capabilities out of proc status | Graded |
| [m04l01-05](m04l01-05/) | Rootless: what container root is on the host | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: prove each control with a change

1. In thumbnail.py, use a pipe instead of the semicolon; predict what each image prints.
2. Add a status file whose CapEff is 0000000000002000 and name the one capability it grants.
3. Append the line 65532 200000 1 to userns.uid_map; predict where uid 65532 lands.
4. Write the ENTRYPOINT in shell form and explain why the distroless container won't start.

> **Hint:** Bit thirteen is the only bit set in that mask. The helper returns the first matching range, but the real kernel rejects overlapping ranges when the map is written.

## Check yourself

- Why did the same injection payload run in the slim directory but fail with no such file or directory in the distroless one?
- A process runs as uid 65532 with CapEff zero but CapBnd still at Docker's fourteen defaults. What could raise its privileges, and which setting blocks that?
- Why must the Dockerfile USER be numeric for Kubernetes to verify runAsNonRoot?
- With the map 0 100000 65536, what host uid does container root have, and why does that matter after a container escape?
- Name one attack class that distroless does nothing to stop, and explain why.

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
