# Cloud Security & DevSecOps Engineering — lesson m03l05 — Supply Chain Security: SBOMs & Cosign Signing
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l05
# © LearnSome.tech
import json, re, uuid

lock = open("requirements.txt").read()
pins = re.findall(r"^([\w.-]+)==([\d.]+)", lock, re.M)
components = [{"type": "library", "name": name, "version": version,
               "purl": f"pkg:pypi/{name.lower()}@{version}"}
              for name, version in pins]
bom = {
    "bomFormat": "CycloneDX",
    "specVersion": "1.5",
    "serialNumber": f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, lock)}",
    "version": 1,
    "metadata": {"timestamp": "2026-09-27T09:00:00Z",
                 "component": {"type": "container", "version": "1.4.2",
                               "name": "registry.example.com/shop/api"}},
    "components": components,
}
json.dump(bom, open("sbom.cdx.json", "w"), indent=2)
print(bom["bomFormat"], bom["specVersion"], bom["serialNumber"])
for c in components:
    print(" ", c["purl"])
