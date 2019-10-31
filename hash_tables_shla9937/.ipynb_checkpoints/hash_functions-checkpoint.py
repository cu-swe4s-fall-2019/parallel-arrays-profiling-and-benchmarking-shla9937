import sys


def h_ascii(key, N):
    if isinstance(key, str):
        hash_value = 0
        for letter in key:
            hash_value += ord(letter)
        return hash_value % N
    else:
        print('Input not str.')
        return -1


def h_rolling(key, N, p=53, m=2**64):
    if isinstance(key, str):
        s = 0
        for i in range(len(key)):
            s += ord(key[i]) * p**i
        s = s % m
        return s % N
    else:
        print('Input not str.')
        return -1


def h_python(key, N):
    return hash(key) % N


if __name__ == '__main__':
    word_list = ['blue', 'green', 'orange']
    N = 4
    for word in word_list:
        print(h_python(word, N))
