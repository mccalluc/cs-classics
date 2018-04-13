import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.ticker import FormatStrFormatter

import sys
import pandas
import re
from cycler import cycler

if __name__ == '__main__':
    dfs = {}
    for file in sys.argv[1:]
    df = pandas.read_csv(sys.argv[1], sep='\t')
    dfs.append(df.set_index(['file']))
    df = pandas.read_csv(sys.argv[2], sep='\t')
    dfs.append(df.set_index(['file']))

    sns.set_style("darkgrid")
    fig, ax = plt.subplots(1, 2)
    every_fifth = ['' if int(i) % 5 else i for i in dfs[0].T.index.tolist()]
    #ax.set_xticklabels(['' if int(i) % 5 else i for i in df.T.index.tolist()])

    plt.rc('axes', prop_cycle=(cycler('linestyle', ['--', '-', ':'])))
    f = plt.figure(figsize=(6, 4))
    filters = ['English articles, in title', 'English books, in title']
    for (i, filter) in enumerate(filters):
        ax = f.add_subplot(len(filters), 1, i+1)
        ax.set_xticklabels(every_fifth)
        #ax.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
        plt.title(filter)
        transpose = dfs[i].T
        plt.plot(pandas.rolling_mean(transpose, 2))
        if i == 0:
            plt.legend(['Algol', 'Fortran', 'Lisp'])

    plt.subplots_adjust(hspace=0.7)
    plt.savefig('/tmp/lines.svg')