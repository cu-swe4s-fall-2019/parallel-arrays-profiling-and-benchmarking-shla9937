import matplotlib
import matplotlib.pyplot as plt
import sys


def boxplot(L, out_file, Title, xlabel, ylabel, tick_labels):
    '''takes array of arrays, plots boxplot, saves output'''
    list_idx = 0
    for i in L:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, int):
                    continue
                elif isinstance(j, float):
                    continue
                else:
                    L.pop(list_idx)
                    print('Item '+str(list_idx)+' was removed from list.')
                    break
            list_idx += 1
        else:
            if isinstance(i, int):
                continue
            elif isinstance(i, float):
                continue
            else:
                print('Non-number item in list')
                sys.exit(1)
    fig, ax = plt.subplots(figsize=(10, 3), dpi=300)
    ax.set_title(Title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(tick_labels, rotation='vertical')
    ax.boxplot(L)
    plt.savefig(out_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
