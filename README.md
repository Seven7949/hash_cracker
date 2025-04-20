# hash_cracker

# 🔓 Hash Cracker (MD5/SHA1)

A brute-force/dictionary-style hash cracker written in Python.  
Feed it a hash and a wordlist — it'll try every word until it finds a match.

---

## 🧠 Why?

To understand the weaknesses of outdated hashing algorithms and how attackers might crack weak passwords.

---

## 🚀 Features

- Supports MD5 and SHA1 hashes
- Uses a local wordlist (e.g., `rockyou.txt`)
- Clear feedback on match or failure
- Easy to extend to SHA256, SHA512, etc.

---

## 🛠️ Requirements

Python 3+

---

## 🧪 Usage

```bash
python hash_cracker.py
