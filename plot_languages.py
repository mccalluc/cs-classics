import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pylab
import matplotlib.ticker

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

    filters = ['American English', 'British English', 'Spanish',
               'French', 'German', 'Italian']
    for (i, filter) in enumerate(filters):
        ax = plt.subplot(len(filters), 1, i+1)
        ax.set_xticklabels(every_fifth)
        plt.plot(df.loc[filter].T)

    plt.savefig('/tmp/lines.svg')