# Cloud Security & DevSecOps Engineering — lesson m01l01 — Shared Responsibility Model & Cloud Threat Landscapes
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m01l01
# © LearnSome.tech
import json

EU_ONLY = {"customer-pii"}                 # classes that must stay in the EU
LEGACY = {None: "us-east-1", "EU": "eu-west-1"}

for b in json.load(open("buckets.json")):
    loc = b["LocationConstraint"]          # as GetBucketLocation returns it
    region = LEGACY.get(loc, loc)
    cls = b["Tags"].get("data-class")
    if cls is None:
        verdict = "no data-class tag: cannot decide"
    elif cls in EU_ONLY and not region.startswith("eu-"):
        verdict = "breaks EU residency"
    else:
        verdict = "ok"
    print(f"{b['Name']:24} {str(loc):13} {region:13} {verdict}")
