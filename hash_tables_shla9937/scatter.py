import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


out_file = sys.argv[1]
x_label = sys.argv[2]
y_label = sys.argv[3]
title = sys.argv[4]

X = []
Y = []
i = 0
for l in sys.stdin:
    A = l.rstrip().split()
    if len(A) == 2:
        X.append(float(i))
        Y.append(float(A[1]))
        i += 1
    elif len(A) == 3:
        X.append(float(i))
        Y.append(float(A[2]))
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
