import data_viz


def linear_search(key, L):
    '''searches array with keyword using linear searching'''
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


def best_binary_search(key, L):
    '''searches array with keyword using binary searching by making array of arrays'''
    L2 = []
    L3 = []
    idx = 0
    for item in L:
        L2.append(item)
        L2.append(idx)
        L3.append(L2)
        L2 = []
        idx += 1
    L3.sort(key=lambda x: x[0])
    lo = -1
    hi = len(L3)
    while (hi - lo > 1):
        mid = (hi + lo) // 2
        if key == L3[mid][0]:
            return L3[mid][1]
        if (key < L3[mid][0]):
            hi = mid
        else:
            lo = mid
    return -1


def nested_binary_search(key, L):
    '''searches array of array with keyword using binary searching'''
    lo = -1
    hi = len(L)
    while (hi - lo > 1):
        mid = (hi + lo) // 2
        if key == L[mid][0]:
            return L[mid][1]
        if (key < L[mid][0]):
            hi = mid
        else:
            lo = mid
    return -1


def binary_search(key, L):
    '''searches array with keyword using binary searching'''
    lo = -1
    hi = L
    hi = len(hi)
    while (hi - lo > 1):
        mid = (hi + lo) // 2
        if key == L[mid]:
            return mid
        elif (key < L[mid]):
            hi = mid
        else:
            lo = mid
    return -1


def main():
    None


if __name__ == '__main__':
    main()
