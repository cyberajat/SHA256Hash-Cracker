#!/usr/bin/env python3

from pwn import *
import sys
import hashlib

if len(sys.argv) != 2:
	print("Invalid Argument!")
	print(f"{sys.argv[0]} <sha256sum>>")
	sys.exit()

wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

p = log.progress(f"Attempting to hack: {wanted_hash}\n")
with open(password_file, "r", encoding = 'latin-1') as password_list:
	for password in password_list:
		password = password.strip("\n").encode('latin-1')
		password_hash = hashlib.sha256(password).hexdigest()
		p.status(f"[{attempts}] {password.decode('latin-1')} == {password_hash}")

		if password_hash == wanted_hash:
			p.success(f"Congratulations- Password has Found after [{attempts}] attempts - '{password.decode('latin-1')}'")
			sys.exit()
		attempts += 1
print("Password has not found!")