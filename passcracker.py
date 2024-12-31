import hashlib

def convert_hash_to_pass(text):
    digest=hashlib.sha1(text.encode()).hexdigest()
    return digest

def main():
    hashed_pass=input("Enter Hashed PASS:")
    mod_hash=hashed_pass.strip().lower()
    with open('passwords.txt') as passlist:
        for line in passlist:
            password=line.strip()
            converted_pass=convert_hash_to_pass(password)

            if mod_hash==converted_pass:
                print(f"The password {password}")
                return
    print("couldn't find the hash")
if __name__=="__main__":
    main()