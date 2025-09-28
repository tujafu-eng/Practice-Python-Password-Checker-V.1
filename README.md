# Practice-Python-Password-Checker-V.1
A basic Password strength checker and verifier Learning project

This is a simple Password checker that validates a user’s password based on several requirements:

- Minimum length of 12 characters
- At least 1 uppercase letter  
- At least 1 lowercase letter
- At least 1 number 
- At least 1 symbol  
- Passwords must match on re-entry  

The program also assigns a **strength score** (`0–5`) and outputs a rating from **"Very Weak"** to **"Strong"**.

---

## 🚀 How It Works
1. Prompts the user to enter a password (hidden input using `getpass`).
2. Re-asks for the password to confirm it matches.
3. Runs checks for:
   - Uppercase letters  
   - Lowercase letters  
   - Numbers  
   - Symbols  
   - Minimum length (12+)  
4. Prints missing requirements.  
5. Outputs a strength rating and a score (`x/5`).  
