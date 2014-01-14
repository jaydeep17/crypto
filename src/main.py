from src import caesarCipher

def main():
    text = 'Hello world is the best program'
    key = 10
    cipherText = caesarCipher.encrypt(text, key)
    print(caesarCipher.bruteForce(cipherText))
    print('smart brute force')
    sb = caesarCipher.smartBruteForce(cipherText, 0.5)
    print(sb)


if __name__ == "__main__":
    main()