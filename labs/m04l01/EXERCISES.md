# Exercises — Container Hardening: Distroless & Rootless

Lesson `m04l01` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l01)

## Exercise 1: Your turn: prove each control with a change

1. In thumbnail.py, use a pipe instead of the semicolon; predict what each image prints.
2. Add a status file whose CapEff is 0000000000002000 and name the one capability it grants.
3. Append the line 65532 200000 1 to userns.uid_map; predict where uid 65532 lands.
4. Write the ENTRYPOINT in shell form and explain why the distroless container won't start.

> **Hint**: Bit thirteen is the only bit set in that mask. The helper returns the first matching range, but the real kernel rejects overlapping ranges when the map is written.


---

© LearnSome.tech · support@iwantto.learnsome.tech
