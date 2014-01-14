from operator import itemgetter


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


def bruteForce(cipherText):
    """
    @rtype : [ (key, plaintext) ]
    @param cipherText: cipher text
    @return: a list of plainTexts
    """
    lst = []
    for i in range(26):
        plainText = decrypt(cipherText, i)
        lst.append((i, plainText))
    return lst


def smartBruteForce(cipherText, thresh):
    """
    Uses NLTK to detect if the resulting text from brute force
    is a valid english text or not. If the ratio of (valid-english-words/total-words)
    is >= thresh, it assumes that it is a valid result

    @rtype : [ (key, plaintext, ratio) ]
    @param cipherText: cipher text
    @param thresh: percentage of words in resulting plain text to be valid english words [ should be between (0...1) ]
    @return: a filtered list of results that pass the threshold
    """
    import nltk
    from nltk.corpus import wordnet

    lst = []
    for i in range(26):
        plainText = decrypt(cipherText, i)
        tokens = nltk.word_tokenize(plainText)
        cnt = 0
        for token in tokens:
            if wordnet.synsets(token):
                cnt += 1
        ratio = cnt / len(tokens)
        if ratio >= thresh:
            lst.append((i, plainText, ratio))
    return sorted(lst, key=itemgetter(2), reverse=True)