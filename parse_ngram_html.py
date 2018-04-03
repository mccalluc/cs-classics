import re
import json
import sys

def parse_data(html):
    json_string = re.search(r'var data = (.*?);', html).group(1)
    return json.loads(json_string)

def parse_meta(html):
    smoothing = re.search(r'smoothing=(\d+)', html).group(1)
    match = re.search(
        r'<meta itemprop="description" content="[^"]+?(\d+)-(\d+) in (.*?).">',
        html)
    return {
        'start': match.group(1),
        'end': match.group(2),
        'corpus': match.group(3),
        'smoothing': smoothing,
    }


if __name__ == '__main__':
    first = True
    for path in sys.argv[1:]:
        with open(path) as f:
            html = f.read()

            meta = parse_meta(html)
            if first:
                year_range = range(int(meta['start']), int(meta['end'])+1)
                head = ['corpus', 'smoothing', 'ngram', 'type'] \
                       + [str(y) for y in year_range]
                print('\t'.join(head))
                first = False

            data = parse_data(html)
            for record in data:
                row = [meta['corpus'], meta['smoothing'], record['ngram'], record['type']] \
                      + ["{0:.4g}".format(y) for y in record['timeseries']]
                print('\t'.join(row))
