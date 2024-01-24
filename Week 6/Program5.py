import random

def interval_encrypt(message):
    interval = random.randint(2, 20)
    encrypted_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            if i % interval == 0:
                encrypted_message += char
            else:
                encrypted_message += random.choice("abcdefghijklmnopqrstuvwxyz")
    return encrypted_message, interval


encrypted_msg, used_interval = interval_encrypt("send cheese")
print(f"Encrypted message: {encrypted_msg}")
print(f"Interval used: {used_interval}")
