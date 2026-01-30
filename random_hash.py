import secrets
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--trials", type=int, default=1000)
parser.add_argument("-p", "--prefix", default="00")
args = parser.parse_args()

for i in range(1, args.trials + 1):
    h = secrets.token_hex(16)
    if h.startswith(args.prefix):
        print(f"PASS: Found {h} after {i} tries.")
        raise SystemExit(0)
else:
    print(f"FAIL: No hash starting with '{args.prefix}' found.")
    raise SystemExit(1)