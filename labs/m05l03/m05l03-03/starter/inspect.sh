# What will this plan do, and to data of which classification?
jq -r '.resource_changes[] | (.change.after // .change.before) as $s
  | [(.change.actions | join("+")), .address,
     ($s.tags.data_classification // "none")] | join("  ")' plan.json

# Which changes are replacements, and what forced them?
jq -r '.resource_changes[] | select(.change.replace_paths)
  | "\(.address) replaced because of \(.change.replace_paths)"' plan.json

# What will Terraform only know after apply?
jq -c '.resource_changes[] | select(.address == "aws_ebs_volume.scratch")
  | .change.after_unknown' plan.json
