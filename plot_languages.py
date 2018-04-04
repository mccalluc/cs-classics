from ggplot import ggplot

import sys
import pandas
import re


if __name__ == '__main__':
    df = pandas.read_csv(sys.argv[1], sep='\t')
    df = df[df['type'] == 'CASE_INSENSITIVE']
    df['ngram'] = df['ngram'].replace(to_replace=re.compile(r' \(All\)'), value='')
    df = df.drop(columns=['smoothing', 'type'])
    df = df.set_index(['corpus', 'ngram'])
    print(df)