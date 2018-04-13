import sys
import re

def parse(html):
    # facet_yr%3A">2018</a> (8)
    matches = re.finditer(r'facet_yr%3A">(\d+)</a> \((\d+)\)', html)
    d = {match.group(1): match.group(2) for match in matches}
    return d

if __name__ == '__main__':
    first = True
    years = [str(i) for i in range(1950, 2009)] # limit range to what was available from ngrams
    for path in sys.argv[1:]:
        with open(path) as f:
            html = f.read()
            d = parse(html)
            if first:
                print('\t'.join(['file'] + list(years)))
                first = False
            print('\t'.join([path] + [d.get(y) or '0' for y in years]))