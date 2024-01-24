def simple_encrypt(message):
    encrypted_message = message.replace(" ", "")[::-1]
    return encrypted_message


encrypted_text = simple_encrypt("Hello world")
print(encrypted_text)
