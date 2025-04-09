# bios_sim.py

MAX_TRIES = 3

def verify_password(input_password, correct_password="abc123", tries_left=3):
    if tries_left <= 0:
        return "LOCKED"
    elif input_password == correct_password:
        return "ACCESS GRANTED"
    else:
        return "WRONG PASSWORD"
