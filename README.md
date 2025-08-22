🔐 SHA-256 Hash Cracker

This is a simple SHA-256 hash cracker written in Python3.
It uses a dictionary attack (default: rockyou.txt) to attempt to recover the plaintext password from a given SHA-256 hash.

⚡ Features

Cracks SHA-256 hashes using rockyou.txt (or any wordlist)

Displays real-time attempt logs using pwntools

Stops immediately when the password is found

Simple and lightweight script

🚀 Usage

1️⃣ Clone the repository

```
git clone https://github.com/your-username/sha256-cracker.git
cd sha256-cracker
```
2️⃣ Run the script

```
./cracker.py <sha256_hash>
```

Or explicitly with Python:
```
python3 cracker.py <sha256_hash>
```
