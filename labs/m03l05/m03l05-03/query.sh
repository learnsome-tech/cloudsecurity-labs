# Cloud Security & DevSecOps Engineering — lesson m03l05 — Supply Chain Security: SBOMs & Cosign Signing
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l05
# © LearnSome.tech
# New advisory: urllib3 before 1.26.17, or 2.0.0 up to 2.0.5.
# Which of our images ship an affected version? No rescan needed.
jq -r '
  .metadata.component.name as $image
  | .components[] | select(.name == "urllib3")
  | (.version | split(".") | map(tonumber)) as $v
  | if $v < [1, 26, 17] or ($v >= [2] and $v < [2, 0, 6])
    then "\($image)  urllib3 \(.version)  affected"
    else "\($image)  urllib3 \(.version)  not affected" end
' sboms/*.cdx.json
