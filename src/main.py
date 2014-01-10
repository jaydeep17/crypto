from src import caesarCipher


def main():
    cipher = caesarCipher.encrypt('Jaydeep', 1)
    cipher += 'aA'
    print(caesarCipher.decrypt(cipher, 1))


if __name__ == "__main__":
    main()