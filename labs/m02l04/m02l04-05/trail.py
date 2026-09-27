# Cloud Security & DevSecOps Engineering — lesson m02l04 — Least Privilege Enforcement & CIEM Architecture
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m02l04
# © LearnSome.tech
import json

ALIASES = {"s3:ListObjectsV2": "s3:ListBucket", "s3:HeadObject": "s3:GetObject"}

def action_of(record):
    action = record["eventSource"].split(".")[0] + ":" + record["eventName"]
    return ALIASES.get(action, action)

def scope_of(record):
    arns = {r["type"]: r["ARN"] for r in record["resources"]}
    if "AWS::S3::Object" in arns:  # widen an object key to its prefix
        return arns["AWS::S3::Object"].rsplit("/", 1)[0] + "/*"
    return next(iter(arns.values()))

def calls(path, role):
    records = json.load(open(path))["Records"]
    return [(action_of(r), scope_of(r)) for r in records
            if r["userIdentity"]["arn"].split("/")[1] == role]
