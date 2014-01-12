from src import caesarCipher
from src import freqAnalysis


def main():
    text = 'iq ifcc vqqr fb rdq vfllcq na rdq cfjwhwz hr bnnb hcc hwwhbsqvqbre hwq vhlq'
    arr = freqAnalysis.analyse(text)
    print(arr)
    print(freqAnalysis.englishLetterFreq())


if __name__ == "__main__":
    main()