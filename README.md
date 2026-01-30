# random_hash

Simple script that generates random 32-character hexadecimal hashes and stops when it finds one that starts with a given prefix.

Usage (PowerShell):

```powershell
python random_hash.py
# or change number of tries / prefix
python random_hash.py -n 1000 -p 00
```

What it does (in plain words):
- It creates secure random 32-character hex strings (like a hash).
- It repeats up to `-n` times (default 1000).
- If any generated hash starts with the prefix (default `'00'`), the script prints a PASS message and exits with code 0.
- If none match after all tries, it prints FAIL and exits with code 1.

You can change the prefix with `-p` if you want a different target.
