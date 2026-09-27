# Cloud Security & DevSecOps Engineering — lesson m03l05 — Supply Chain Security: SBOMs & Cosign Signing
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l05
# © LearnSome.tech
IMAGE="registry.example.com/shop/api@$DIGEST"   # digest from the build step

# Key pair: cosign.key is encrypted with a password, cosign.pub is shared
cosign generate-key-pair
cosign sign --key cosign.key "$IMAGE"
cosign verify --key cosign.pub "$IMAGE"

# The SBOM as a signed attestation attached to the same digest
cosign attest --key cosign.key --type cyclonedx \
  --predicate sbom.cdx.json "$IMAGE"
cosign verify-attestation --key cosign.pub --type cyclonedx "$IMAGE"

# Keyless in CI: certificate from Fulcio, entry in the Rekor log
cosign sign --yes "$IMAGE"
cosign verify "$IMAGE" \
  --certificate-identity-regexp '^https://github.com/example-org/api/' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
