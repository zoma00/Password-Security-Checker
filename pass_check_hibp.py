import requests
import hashlib

def check_password_hibp(password):
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Query the Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        # Check if the suffix exists in the response
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(':')
            if hash_suffix == suffix:
                return True  # Password has been compromised
        return False  # Password is safe
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False

def main():
    password = input("Enter your password to check: ")
    if check_password_hibp(password):
        print(f'The password "{password}" has been compromised!')
    else:
        print(f'The password "{password}" is safe.')

if __name__ == '__main__':
    main()


"""
Example output: (Terminal):

(MyDjangoEnv) PS E:\Integration developer\Linkedin python challenges and data science posts\password checker> python pass_check_hibp.py
Enter your password to check: hello
The password "hello" has been compromised!
(MyDjangoEnv) PS E:\Integration developer\Linkedin python challenges and data science posts\password checker>
"""