import csv

with open('phoible-by-phoneme.tsv','rb') as tsvin, open('spa-vowels.tsv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    # csvout = csv.writer(csvout)
    writer = csv.writer(csvout, delimiter='\t')

    first = True
    for row in tsvin:
        if first:
            writer.writerow(row)
            first = False
            continue
        if 'spa' in row and row[11] == '+' and row[14] == '-':
            writer.writerow(row)
