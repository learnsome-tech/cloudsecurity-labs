package terraform.guardrails
deny contains msg if {
    some rc in input.resource_changes
    rc.change.actions != ["delete"]
    not rc.change.after.tags.data_classification
    msg := sprintf("%s: no data_classification tag", [rc.address])
}

deny contains msg if {
    some rc in input.resource_changes
    rc.change.after.tags.data_classification in {"confidential", "restricted"}
    not rc.change.after.storage_encrypted
    not rc.change.after.encrypted
    msg := sprintf("%s: sensitive data not encrypted at rest", [rc.address])
}

deny contains msg if {
    some rc in input.resource_changes
    "delete" in rc.change.actions
    rc.change.before.tags.data_classification == "restricted"
    msg := sprintf("%s: plan destroys restricted data", [rc.address])
}
