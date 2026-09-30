from iam_eval import decide

def effective(policies, action, resource):
    verdicts = [decide(p, action, resource, {}) for p in policies]
    if "explicit deny" in verdicts:
        return "explicit deny"
    return "allow" if set(verdicts) == {"allow"} else "implicit deny"

admin = {"Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]}
boundary = {"Statement": [
    {"Effect": "Allow", "Action": "s3:*",
     "Resource": "arn:aws:s3:::example-app-data/*"},
    {"Effect": "Allow", "Action": "logs:*", "Resource": "*"}]}

for action, resource in [
        ("s3:GetObject", "arn:aws:s3:::example-app-data/reports/q3.csv"),
        ("s3:GetObject", "arn:aws:s3:::example-payroll/2026-09.csv"),
        ("iam:CreateUser", "arn:aws:iam::111122223333:user/backdoor")]:
    alone = effective([admin], action, resource)
    capped = effective([admin, boundary], action, resource)
    print(f"{action:14} {resource.split(':')[-1]:30} {alone:5} -> {capped}")
