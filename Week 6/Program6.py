def interval_decrypt(encrypted_message, interval):
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            if i % interval == 0:
                decrypted_message += char
    return decrypted_message


decrypted_msg = interval_decrypt("sxyexynxydxy cxyhxyexyexysxye", 2)
print(f"Decrypted message: {decrypted_msg}")
