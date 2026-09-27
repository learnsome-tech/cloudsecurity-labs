# Exercises — Zero-Trust Network Access & IdP Federation

Lesson `m02l05` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l05)

## Exercise 1: Extend the broker and its SCIM endpoint

1. Issue alice a token with iat one day earlier; predict the status and reason first.
2. Make do_PATCH accept op "Replace" and value "False" as a string, as some IdPs send.
3. Require a SCIM bearer token in do_PATCH and show an unauthenticated PATCH is refused.
4. Refuse devices whose owner differs from the token's sub, and test it with bob's laptop.

> **Hint**: In Python the string "False" is truthy, so compare it explicitly. The device owner is in devices.json.


---

© LearnSome.tech · support@iwantto.learnsome.tech
