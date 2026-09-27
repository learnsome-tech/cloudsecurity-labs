# Cloud Security & DevSecOps Engineering — lesson m06l04 — Cloud Security Posture Management & Remediation
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l04
# © LearnSome.tech
resource "aws_config_remediation_configuration" "restricted_ssh" {
  config_rule_name           = "restricted-ssh" # source: INCOMING_SSH_DISABLED
  target_type                = "SSM_DOCUMENT"
  target_id                  = "AWS-DisableIncomingSSHOnPort22"
  automatic                  = true
  maximum_automatic_attempts = 3
  retry_attempt_seconds      = 60
  parameter {
    name           = "GroupId"
    resource_value = "RESOURCE_ID"
  }
  parameter {
    name         = "AutomationAssumeRole"
    static_value = "arn:aws:iam::111122223333:role/config-remediation"
  }
  execution_controls {
    ssm_controls {
      concurrent_execution_rate_percentage = 10
      error_percentage                     = 10
    }
  }
}
