set -uo pipefail
bash envelope.sh > /dev/null             # the files from the last step
hex() { od -An -v -tx1 "$1" | tr -d ' \n'; }
unwrap() {                               # what KMS Decrypt does inside the HSM
  openssl enc -d -id-aes256-wrap -K "$(hex "$1")" -iv A6A6A6A6A6A6A6A6 \
    -in data-key.enc -out data-key.bin 2> /dev/null
}

# With the right KMS key
unwrap kms-key.bin
openssl enc -d -aes-256-cbc -K "$(hex data-key.bin)" \
  -iv "$(cat payroll.csv.iv)" -in payroll.csv.enc | cut -d, -f1,2
rm data-key.bin

# With a different KMS key of the same size and type
openssl rand 32 > other-key.bin
unwrap other-key.bin || echo "other key: unwrap refused, integrity check failed"

# After the KMS key is deleted
rm kms-key.bin
unwrap kms-key.bin 2> /dev/null || echo "key deleted: nothing can unwrap it"
