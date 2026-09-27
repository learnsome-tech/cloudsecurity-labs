package platform.buckets

default allow := false

allow if input.user.team == "platform"

allow if {
    input.action == "read"
    input.bucket.owner == input.user.team
}

deny contains msg if {
    input.action == "delete"
    not input.user.mfa
    msg := sprintf("%s: delete without MFA", [input.user.name])
}
