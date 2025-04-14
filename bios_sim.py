# bios_sim.py

MAX_TRIES = 3

def verify_password(input_password, correct_password="abc123", tries_left=3):
    if tries_left <= 0:
        return "LOCKED"
    elif input_password == correct_password:
        return "ACCESS GRANTED"
    else:
        return "WRONG PASSWORD"

if __name__ == "__main__":
    tries = 3
    correct_pw = "abc123"
    
    while tries > 0:
        pw = input("Please enter your password: ")
        tries -= 1
        result = verify_password(pw, correct_password=correct_pw, tries_left=tries)
        
        if result == "ACCESS GRANTED":
            print(result)
            break
        elif tries == 0:
            print("LOCKED")
            print("System Locked!")
            break
        else:
            print(f"WRONG PASSWORD ({tries} attempts left)")
