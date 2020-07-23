from collections import Counter

def display(index, counter):
    print("Sequence {}:".format(index))
    for nucleotide in 'ACGT':
        print("Number of {}'s: {}".format(nucleotide, counter[nucleotide]))
    print()

with open('multiple_sequences.fasta') as file:
    index = 0
    counter = Counter()
    for line in file:
        string = line.rstrip('\n')
        if string.startswith('>'):
            if index > 0:
                display(index, counter)
            index += 1
            counter.clear()
        else:
            counter.update(string)
    if counter:  # pop out the last one in the now closed file
        display(index, counter)
