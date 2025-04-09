# bios-password-tester

A simple simulation of BIOS password verification logic, with automated unit tests using Python.

---

## Project Description

This project simulates a basic BIOS boot-time password authentication mechanism.  
It was designed as a self-driven side project to demonstrate:

- System-level thinking (BIOS-level logic)
- Python function design & exception handling
- Automated testing using `unittest`

---

## Features

-  Verifies password correctness
-  Handles incorrect attempts and lockout scenarios
-  Unit tested with edge cases:
  - Correct password
  - Wrong password
  - Locked state (no attempts left)
  - Case sensitivity

---

## How to Run Tests

```bash
python test_bios.py
```

---

## bios-password-tester/
```
├── bios_sim.py       # Core logic
├── test_bios.py      # Automated unit tests
└── README.md         # Project description
```

---

Why I Built This
To prepare for a software validation internship,
I challenged myself to implement a BIOS-like feature and test it thoroughly.
It’s a learning-focused project to demonstrate:
Self-motivation, testing mindset, and system-level awareness.
