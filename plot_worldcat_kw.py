import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.ticker import FormatStrFormatter

import sys
import pandas
import re
from cycler import cycler

if __name__ == '__main__':
    dfs = {}
    files = sys.argv[1:]
    for file in files:
        df = pandas.read_csv(file, sep='\t').set_index(['file'])
        print(file)
        print(df)
        every_fifth = ['' if int(i) % 5 else i for i in df.T.index.tolist()]
        dfs[file] = pandas.rolling_mean(df.T, 2)



    sns.set_style("darkgrid")
    fig, ax = plt.subplots(1, len(files))

    plt.rc('axes', prop_cycle=(cycler('linestyle', ['--', '-', ':'])))
    f = plt.figure(figsize=(6, 6))
    for (i, file) in enumerate(files):
        ax = f.add_subplot(len(files), 1, i+1)
        ax.set_xticklabels(every_fifth)
        #ax.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
        if 'kw' in file:
            search = 'keyword'
        else:
            search = 'title'
        if 'book' in file:
            media = 'book'
        else:
            media = 'article'
        plt.title('English {}, {} search'.format(media, search))
        plt.plot(dfs[file])
        if i == 0:
            plt.legend(['Algol', 'Fortran', 'Lisp'])

    plt.subplots_adjust(hspace=0.7)
    plt.savefig('/tmp/lines.svg')