import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pylab

from matplotlib.ticker import FormatStrFormatter

import sys
import pandas
import re


if __name__ == '__main__':
    df = pandas.read_csv(sys.argv[1], sep='\t')
    df = df[df['type'] == 'CASE_INSENSITIVE']
    df['ngram'] = df['ngram'].replace(to_replace=re.compile(r' \(All\)'), value='')
    df = df.drop(columns=['smoothing', 'type'])
    df = df.set_index(['corpus', 'ngram'])
    #print(df.T)

    sns.set_style("darkgrid")
    # fig, ax = plt.subplots(1, 1)
    every_fifth = ['' if int(i) % 5 else i for i in df.T.index.tolist()]
    # ax.set_xticklabels(['' if int(i) % 5 else i for i in df.T.index.tolist()])

    f = plt.figure(figsize=(6, 8))
    filters = ['American English', 'British English', 'Spanish',
               'French', 'German', 'Italian']
    for (i, filter) in enumerate(filters):
        ax = f.add_subplot(len(filters), 1, i+1)
        ax.set_xticklabels(every_fifth)
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.2e'))
        plt.title(filter)
        plt.plot(df.loc[filter].T)

    plt.subplots_adjust(hspace=0.7)
    plt.savefig('/tmp/lines.svg')