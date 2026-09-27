# Cloud Security & DevSecOps Engineering — lesson m06l03 — Envelope Encryption & Data Protection with KMS
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l03
# © LearnSome.tech
from kmsauth import decide

APP = "arn:aws:iam::111122223333:role/payroll-app"
ADMIN = "arn:aws:iam::111122223333:role/platform-admin"
requests = [
    (APP, "kms:Decrypt", "payroll"),
    (APP, "kms:Decrypt", "hr"),
    (ADMIN, "kms:Decrypt", "payroll"),
    (ADMIN, "kms:ScheduleKeyDeletion", None),
    (ADMIN, "kms:PutKeyPolicy", None),
]
for role, action, department in requests:
    context = {"kms:EncryptionContext:department": department}
    print(role.rsplit("/", 1)[-1].ljust(14), action.ljust(24),
          (department or "-").ljust(8), decide(role, action, context))
