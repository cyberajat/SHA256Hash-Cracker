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
git clone https://github.com/cyberajat/SHA256Hash-Cracker.git
cd SHA256Hash-Cracker
python3 -m venv pwn-env
source pwn-env/bin/activate
pip install --upgrade pip
pip install pwntools
```
2️⃣ Run the script
```
./cracker.py <sha256_hash>
```

Or explicitly with Python:
```
python3 cracker.py <sha256_hash>
```
3️⃣ Example
```
./cracker.py 1236dabbe733f0dae4c00ac3135be5498fa16ce4118d8cece6ea8f5d28594d69
```

Output:
```
[12345] kalinux == 1236dabbe733f0dae4c00ac3135be5498fa16ce4118d8cece6ea8f5d28594d69
[+] Congratulations - Password has Found after [12345] attempts - 'kalinux'
```

📂 Requirements

Python 3

pwntools
 (pip install pwntools)

A wordlist (default: rockyou.txt)

⚠️ Disclaimer

This tool is intended for educational and research purposes only.
Do not use it for illegal activities.
