# Exercises — Securing the Kubernetes Control Plane & Node Components

Lesson `m04l05` · [Watch](https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l05)

## Exercise 1: Your turn: fix the manifest, prove the encryption

1. Add the flags that make every check in audit_flags.py pass; predict the output first.
2. Change --authorization-mode to Node,RBAC,AlwaysAllow and explain why one check now fails.
3. Decrypt the aescbc value with a different key and read the error openssl gives you.
4. Put identity first in the provider order and say what etcd would hold for new Secrets.

> **Hint**: Authorisers are asked in order and the first one that allows wins. A wrong key usually fails the padding check, which is why openssl reports bad decrypt.


---

© LearnSome.tech · support@iwantto.learnsome.tech
