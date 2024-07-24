# Password-Security-Checker


**Python Password Checker using Have I Been Pwned (HIBP)**

This Python script provides a simple way to check if a password has been compromised in data breaches using the Have I Been Pwned (HIBP) API.

**Features:**

* Uses the HIBP API to query for password leaks.
* Hashes passwords securely using SHA-1 (Note: SHA-1 is not considered a secure hashing algorithm for password storage. This script is for demonstration purposes only).
* Provides feedback on whether the password is likely compromised.

**Requirements:**

* Python 3
* `requests` library (`pip install requests`)
* `hashlib` library (included in Python)

**Usage:**

1. Clone or download the repository.
2. Install the required library: `pip install requests`
3. Run the script: `python pass_check_hibp.py`
4. Enter your password when prompted. (**Important:** The script will not store the password. It only hashes it for the API query.)

**Example Output:**

```
Enter your password to check: 123456
The password "123456" has been compromised!
```

**Disclaimer:**

This script is for educational purposes only and should not be used for real-world password management.  It is recommended to use strong, unique passwords and a password manager for secure storage. 

**Contributing:**

Feel free to fork and contribute to this project!

**License:**

MIT License
