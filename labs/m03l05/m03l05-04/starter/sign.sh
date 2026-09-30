set -e
sha() { openssl dgst -sha256 -r "$@" | cut -c1-64; }

# A trimmed image manifest; the image digest is the SHA-256 of these bytes
layer=$(printf 'app v1.4.2' | sha)
printf '{"schemaVersion":2,"layers":[{"digest":"sha256:%s"}]}' "$layer" \
  > manifest.json
digest="sha256:$(sha manifest.json)"

# What cosign signs: a simple signing payload that names the digest
cat > payload.json <<EOF
{"critical":{"identity":{"docker-reference":"registry.example.com/shop/api"},
"image":{"docker-manifest-digest":"$digest"},
"type":"cosign container image signature"},"optional":null}
EOF

openssl ecparam -name prime256v1 -genkey -noout -out cosign.key
openssl ec -in cosign.key -pubout -out cosign.pub 2>/dev/null
openssl dgst -sha256 -sign cosign.key -out payload.sig payload.json
echo "signed $digest"
openssl dgst -sha256 -verify cosign.pub -signature payload.sig payload.json
