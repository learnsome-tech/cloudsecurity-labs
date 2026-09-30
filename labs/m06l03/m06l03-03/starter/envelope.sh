set -euo pipefail
hex() { od -An -v -tx1 "$1" | tr -d ' \n'; }
wrap_iv=A6A6A6A6A6A6A6A6                 # RFC 3394 key wrap default IV

openssl rand 32 > kms-key.bin            # in real KMS this never leaves the HSM

# GenerateDataKey: a fresh key, and the same key wrapped under the KMS key
openssl rand 32 > data-key.bin
openssl enc -id-aes256-wrap -K "$(hex kms-key.bin)" -iv "$wrap_iv" \
  -in data-key.bin -out data-key.enc

# Encrypt the file locally with the plaintext data key, then forget it
iv=$(openssl rand -hex 16)
openssl enc -aes-256-cbc -K "$(hex data-key.bin)" -iv "$iv" \
  -in payroll.csv -out payroll.csv.enc
echo "$iv" > payroll.csv.iv
rm data-key.bin

for f in payroll.csv payroll.csv.enc data-key.enc; do
  printf '%-16s %4s bytes\n' "$f" "$(wc -c < "$f" | tr -d ' ')"
done
