import hashlib

def crack_hash(hash_to_crack, wordlist_path, algo='md5'):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for word in f:
                word = word.strip()
                if algo == 'md5':
                    hashed = hashlib.md5(word.encode()).hexdigest()
                elif algo == 'sha1':
                    hashed = hashlib.sha1(word.encode()).hexdigest()
                else:
                    print("❌ Unsupported hash algorithm.")
                    return

                if hashed == hash_to_crack:
                    print(f"✅ Password found: {word}")
                    return
        print("❌ Password not found in wordlist.")
    except FileNotFoundError:
        print("🚫 Wordlist file not found.")

if __name__ == "__main__":
    print("🔓 Hash Cracker Tool")
    algo = input("Hash Algorithm (md5/sha1): ").lower()
    hash_input = input("Enter the hash to crack: ")
    wordlist = input("Path to your wordlist (e.g. rockyou.txt): ")

    crack_hash(hash_input, wordlist, algo)
