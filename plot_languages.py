import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pylab

import sys
import pandas
import re


if __name__ == '__main__':
    df = pandas.read_csv(sys.argv[1], sep='\t')
    df = df[df['type'] == 'CASE_INSENSITIVE']
    df['ngram'] = df['ngram'].replace(to_replace=re.compile(r' \(All\)'), value='')
    df = df.drop(columns=['smoothing', 'type'])
    df = df.set_index(['corpus', 'ngram'])
    print(df.T)

    sns.set_style("darkgrid")
    plt.plot(df.T)
    plt.savefig('/tmp/lines.png')