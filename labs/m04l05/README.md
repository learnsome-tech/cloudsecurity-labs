# m04l05 · Securing the Kubernetes Control Plane & Node Components

Module 4: Container & Kubernetes Runtime Defense · lesson 4.5 · Pro · [Open the lesson](https://learnsome.tech/learn/cloudsecurity-course/m04l05)

**Goal:** You can audit API server and kubelet settings against CIS-style checks, and turn on and verify encryption at rest for Secrets in etcd.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l05-02](m04l05-02/) | The API server's static pod manifest | Checker |
| [m04l05-03](m04l05-03/) | Auditing the flags like a benchmark would | Graded |
| [m04l05-04](m04l05-04/) | Locking down the kubelet | Checker |
| [m04l05-05](m04l05-05/) | Encryption at rest for Secrets | Checker |
| [m04l05-06](m04l05-06/) | What etcd holds with and without encryption | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: fix the manifest, prove the encryption

1. Add the flags that make every check in audit_flags.py pass; predict the output first.
2. Change --authorization-mode to Node,RBAC,AlwaysAllow and explain why one check now fails.
3. Decrypt the aescbc value with a different key and read the error openssl gives you.
4. Put identity first in the provider order and say what etcd would hold for new Secrets.

> **Hint:** Authorisers are asked in order and the first one that allows wins. A wrong key usually fails the padding check, which is why openssl reports bad decrypt.

## Check yourself

- The manifest has no --anonymous-auth flag at all. Why did the audit still mark that check as failed?
- A kubelet started with no configuration file listens on 10250. What can an unauthenticated caller do, and which two settings stop it?
- You enabled aescbc encryption, but etcdctl shows an old Secret still in plain text. Why, and how do you fix it?
- In the encryption configuration, why is identity listed after aescbc rather than removed, and what would happen if it came first?
- Why is authorization-mode=Node,RBAC,AlwaysAllow as dangerous as AlwaysAllow on its own?

---

[Course README](../../README.md) · [Cloud Security & DevSecOps Engineering on LearnSome.tech](https://learnsome.tech/courses/cloudsecurity-course)
