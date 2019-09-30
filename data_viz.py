import matplotlib.pyplot as plt
import sys
import get_data

this is commited
def boxplot(L, out_file):
    ax1 = plt.subplot()
    ax1.set_title('Title')
    ax1.set_xlabel('xlabel')
    ax1.set_ylabel('ylabel')
    ax1.boxplot(L)
    plt.savefig(out_file)
    sys.stdin
    

if __name__ == '__main__':
    main()