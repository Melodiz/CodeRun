# Solution for https://coderun.yandex.ru/problem/q1-c-text/

def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    data = ''
    with open('Algorithms/Easy/446_q1_c_text/encoded.txt', 'r') as file:
        data = file.read()
    decrypted_text = decrypt_caesar(data, 13)
    with open('Algorithms/Easy/446_q1_c_text/decrypted.txt', 'w') as file:
        file.write(decrypted_text)
if __name__ == "__main__":
    main()
