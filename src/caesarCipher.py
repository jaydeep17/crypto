def encrypt(text, key):
    txt = list(text)
    for i in range(len(txt)):
        txt[i] = chr(ord(txt[i]) + key)
    return ''.join(txt)


def decrypt(cipherText, key):
    txt = list(cipherText)
    for i in range(len(txt)):
        txt[i] = chr(ord(txt[i]) - key)
    return ''.join(txt)