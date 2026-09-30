# The pipeline step: scan, keep the exit code, let the runner decide.
for tf in network.tf.json network-fixed.tf.json; do
  echo "scanning $tf"
  python3 check_sg.py "$tf"
  echo "exit code $?"
done
