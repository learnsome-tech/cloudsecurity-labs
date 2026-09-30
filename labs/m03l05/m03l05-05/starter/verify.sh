bash sign.sh > /dev/null                 # sign the original image first
sha() { openssl dgst -sha256 -r "$@" | cut -c1-64; }

admit() {                                # $1: digest the tag points to now
  if ! openssl dgst -sha256 -verify cosign.pub -signature payload.sig \
       payload.json > /dev/null 2>&1; then
    echo "$2: signature does not verify, reject"
  elif ! grep -q "\"$1\"" payload.json; then
    echo "$2: valid signature for another digest, reject"
  else
    echo "$2: signed digest matches, admit"
  fi
}

signed=$(grep -o 'sha256:[0-9a-f]*' payload.json)
admit "$signed" "original image"
printf '{"schemaVersion":2,"layers":[{"digest":"sha256:%s"}]}' \
  "$(printf 'app v1.4.2 plus miner' | sha)" > evil.json
evil="sha256:$(sha evil.json)"
admit "$evil" "tag moved to a new image"
sed "s/$signed/$evil/" payload.json > edited && mv edited payload.json
admit "$evil" "payload edited to match"
