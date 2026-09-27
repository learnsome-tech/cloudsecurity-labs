# Cloud Security & DevSecOps Engineering — lesson m05l04 — Continuous IaC Drift Detection & State Protection
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l04
# © LearnSome.tech
terraform {
  backend "s3" {
    bucket       = "example-org-tfstate-prod"
    key          = "network/terraform.tfstate"
    region       = "eu-west-2"
    encrypt      = true
    kms_key_id   = "arn:aws:kms:eu-west-2:111122223333:key/example-state-key"
    use_lockfile = true # lock object in the bucket; recent Terraform only
  }
}

# The state bucket itself, built by a separate bootstrap configuration:
#   versioning enabled, so a bad or deleted state can be rolled back
#   public access block with all four settings true
#   bucket policy denying any request where aws:SecureTransport is false
#   KMS key policy: kms:Decrypt only for the deploy and drift roles
