# Projects After Learning Python Basics 🐍

Welcome to my Python repository! This collection contains foundational console applications created after mastering the core basics of Python programming. Each project is engineered with comprehensive user input validation, complete cross-platform terminal control, and stA
## 🚀 Projects Included

### 1. Interactive Command-Line Calculator
A reliable, robust console calculator designed to execute arithmetic calculations securely without unexpected run-time crashes.
* **Key Features:**
  * Strict inputs validation (only allows floating-point decimals or integers).
  * Comprehensive **ZeroDivisionError** handling (safely checks if the divisor is `0`).
  * Infinite runtime loop with an interactive prompt to exit (`n`) or continue.
  * Cross-platform screen clearing after calculation steps.

### 2. Secure Random Password Generator
A highly secure utility designed to generate cryptographically safe, random passwords according to custom length constraints.
* **Key Features:**
  * Uses Python's `secrets` module for cryptographically secure pseudo-random number generation.
  * Combines uppercase/lowercase letters, numerical digits, and special punctuation markers.
  * Strict password length boundary checking (limits values safely between 1 and 100 characters).
  * Automated generation countdown delay system.

---

## 🛠️ Key Architectural Strengths

### 🖥️ Cross-Platform Terminal Management
Both scripts utilize a seamless terminal environment wrapper that checks operating system fingerprints before choosing the appropriate screen-clearing method. This keeps user history neat and readable on both Windows (`cls`) and Unix/Linux/macOS (`clear`).

```python
def clear():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)
```

### 🎨 100% PEP 8 Compliant
Every script inside this repository is cleanly written, linted, and fully structured according to [PEP 8 - Style Guide for Python Code](https://python.org). 
* Follows explicit two-line vertical spacing rules for core functions.
* Implements consistent double quote structures (`"`) across all print streams.
* Utilizes safe multi-line string implicit continuations.
* Includes explicit main conditional block definitions (`if __name__ == "__main__": main()`).

---

## 💻 How to Run the Applications

1. Ensure you have **Python 3.x** installed on your system.
2. Clone this repository directly onto your desktop environment:
   ```bash
   git clone https://github.com
   ```
3. Navigate into the specific directory:
   ```bash
   cd Projects-After-Learning-Python-Basics
   ```
4. Run the chosen application target file (e.g., executing the calculator):
   ```bash
   python calculator.py
   ```

---

### 🌟 Project Details & Author Info
* **Created By:** Satyaki Debnath
* **Project Ecosystem:** Personal Python Mini-Apps Portfolio
* **Design Pattern:** Functional execution wrappers with explicit PEP 8 layout syntax

*"I am happy that you used my program 😀 Thank you for visiting!"*
