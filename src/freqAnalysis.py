from operator import itemgetter


def analyse(text):
    """
    frequency analysis of the given text
    @rtype : list( (str,float), (str,float) )
    @param text: string to analyse
    @return: list containing letter frequencies in percentage% (decreasing order)
    """
    arr = dict()
    count = 0
    for c in text:
        if c == ' ':
            continue
        if c in arr:
            arr[c] += 1
            count += 1
        else:
            arr[c] = 1
            count += 1
    arr = {k: round((v * 100) / count, 3) for k, v in arr.items()}
    return sorted(arr.items(), key=itemgetter(1), reverse=True)


def englishLetterFreq():
    """
    @rtype : list( (str,float), (str,float) )
    @return: frequency of each english letter in percentage%
    """
    arr = {
        'a': 8.167,
        'b': 1.492,
        'c': 2.782,
        'd': 4.253,
        'e': 12.702,
        'f': 2.228,
        'g': 2.015,
        'h': 6.094,
        'i': 6.966,
        'j': 0.153,
        'k': 0.772,
        'l': 4.025,
        'm': 2.406,
        'n': 6.749,
        'o': 7.507,
        'p': 1.929,
        'q': 0.095,
        'r': 5.987,
        's': 6.327,
        't': 9.056,
        'u': 2.758,
        'v': 0.978,
        'w': 2.360,
        'x': 0.150,
        'y': 1.974,
        'z': 0.074
    }
    return sorted(arr.items(), key=lambda x: x[1], reverse=True)
