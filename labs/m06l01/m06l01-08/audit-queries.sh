# Cloud Security & DevSecOps Engineering — lesson m06l01 — CloudTrail Logging, Integrity Validation & Athena
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m06l01
# © LearnSome.tech
echo "who touched secrets"
jq -r 'select(.objectRef.resource == "secrets")
  | [.stageTimestamp[11:19], .user.username, .verb,
     .objectRef.namespace + "/" + (.objectRef.name // "*"),
     (.responseStatus.code | tostring)] | join(" ")' audit.log

echo "denied requests per user"
jq -rs 'map(select(.annotations["authorization.k8s.io/decision"] == "forbid"))
  | group_by(.user.username)[] | "\(.[0].user.username) \(length)"' audit.log

echo "shells opened inside pods"
jq -r 'select(.objectRef.subresource == "exec")
  | "\(.user.username) \(.objectRef.namespace)/\(.objectRef.name)"' audit.log
