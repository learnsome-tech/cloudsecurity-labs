# m01l01-06 · Data residency: where do the buckets really live?

**Lesson:** [Shared Responsibility Model & Cloud Threat Landscapes](https://learnsome.tech/learn/cloudsecurity-course/m01l01) (lesson 1.1, module 1: Multi-Account Cloud Architecture & Isolation) · Free  
**Check:** Graded

## Goal

You can say which security tasks stay with you in each cloud service model, audit a real security group export for admin ports open to the internet, and check bucket regions against a data residency rule.

In the lesson: Data residency sits on your side of the line too. S three keeps an object in the region you chose unless you configure replication, but choosing the region is up to you. This check reads locations as the get bucket location A P I reports them, and that A P I has two quirks worth knowing. A bucket in u s east one comes back with a null location constraint, and older buckets in Ireland can come back as the letters E U, which means e u west one. The script maps both, looks up the data class tag, and compares each region with the rule that customer data stays in the E U. It prints one line per bucket. The result shows one real breach, the support uploads in u s east one, and one bucket nobody can judge, because without a classification tag there is nothing to check residency against.

## Files

- [`starter/buckets.json`](starter/buckets.json)
- [`starter/residency.py`](starter/residency.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-06/starter`
2. Read `residency.py` the way the lesson builds it:
   - Lines 1–4: has two quirks
   - Lines 5–9: compares each region
   - Lines 10–16: prints one line per bucket
3. Run it: `python3 residency.py`.
4. Check it from the repository root: `./check m01l01-06`.

## Expected output

```text
orders-exports-example   eu-central-1  eu-central-1  ok
support-uploads-example  None          us-east-1     breaks EU residency
invoices-2019-example    EU            eu-west-1     ok
build-cache-example      us-west-2     us-west-2     ok
ml-scratch-example       us-west-2     us-west-2     no data-class tag: cannot decide
```

## How to check

`./check m01l01-06` copies `starter/` into a scratch directory and runs `python3 residency.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cloudsecurity-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
