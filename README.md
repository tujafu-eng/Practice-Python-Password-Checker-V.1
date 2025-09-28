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

---

## Tech Stack
- **Python 3**
- `getpass` (to securely enter hidden passwords)

---

##  What I Learned
- String handling (`any()` checks across sets of characters)  
- Input validation and feedback loops  
- Basic password security rules  
- Writing a simple scoring system  

---

##  Future Improvements
- Add **entropy-based scoring** for stronger security evaluation.  
- Block common passwords (e.g., `password123`, `qwerty`).  
- Estimate **crack time** based on complexity.  
- Build a **GUI version** (Tkinter or PyQt).  
- Deploy as a simple **web app** (Flask/Django).  

---

##  Disclaimer
This is a **learning project**, not a production-grade security tool.  
Real password strength checkers use advanced methods like entropy calculations, breach database checks, and machine learning to detect weak patterns.  
