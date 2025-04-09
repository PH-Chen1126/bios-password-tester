﻿# bios-password-tester

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
