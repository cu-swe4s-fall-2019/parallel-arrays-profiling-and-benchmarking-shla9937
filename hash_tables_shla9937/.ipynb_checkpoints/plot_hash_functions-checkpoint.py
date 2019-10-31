import hash_tables
import hash_functions
import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def plot_scatter(hash_values, out_file, x_label, y_label, title):
    X = []
    Y = []
    i = 0
    for item in hash_values:
        A = item
        X.append(float(i))
        Y.append(float(A))
        i += 1

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.title(title)

    plt.savefig(out_file, bbox_inches='tight')


if __name__ == '__main__':
    file_name = sys.argv[1]
    f = open(file_name, 'r')

    word_list = []
    for l in f:
        word_list.append(l.rstrip())

    f.close()
    N = len(word_list)*1.3

    hash_values = []

    if sys.argv[2] == 'h_rolling':
        for word in word_list:
            hash_values.append(hash_functions.h_rolling(word, N))
    elif sys.argv[2] == 'h_ascii':
        for word in word_list:
            hash_values.append(hash_functions.h_ascii(word, N))
    elif sys.argv[2] == 'h_python':
        for word in word_list:
            hash_values.append(hash_functions.h_python(word, N))
    else:
        print('Invalid hash function called.')
        sys.exit

    out_file = sys.argv[3]
    x_label = sys.argv[4]
    y_label = sys.argv[5]
    title = sys.argv[6]

    plot_scatter(hash_values, out_file, x_label, y_label, title)
