import sys
import re

def parse(html):
    pairs = re.search(r'id="raw_tc_data">\{(.*?)\}', html).group(1)
    d = {year: count for (year, count) in
               [pair.split('=') for pair in pairs.split(', ')]
         }
    return d

if __name__ == '__main__':
    first = True
    for path in sys.argv[1:]:
        with open(path) as f:
            html = f.read()
            d = parse(html)
            if first:
                print('\t'.join([path] + list(d)))
                first = False
            print('\t'.join([path] + list(d.values())))