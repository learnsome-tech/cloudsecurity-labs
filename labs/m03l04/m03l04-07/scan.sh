# Cloud Security & DevSecOps Engineering — lesson m03l04 — Software Composition Analysis with Trivy
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l04
# © LearnSome.tech
# Code: lockfiles in the repository, plus secrets
trivy fs --scanners vuln,secret --severity HIGH,CRITICAL --exit-code 1 .

# Container: OS packages and app dependencies inside the built image
trivy image --ignore-unfixed --severity HIGH,CRITICAL --exit-code 1 \
  registry.example.com/shop/api:1.4.2

# Cluster: Kubernetes manifests and Helm charts, before they are applied
trivy config --severity HIGH,CRITICAL ./deploy

# Cloud: the Terraform that builds the account and the cluster
trivy config ./terraform

# Machine-readable output for a gate, a dashboard or code scanning
trivy fs --format json --output report.json .
trivy fs --format sarif --output trivy.sarif .
