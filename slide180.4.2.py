import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta file]")
    sys.exit()

fasta_dict = {}
header = None
seq = ''

with open(sys.argv[1], 'r') as handle:
    for line in handle:
        line = line.rstrip()
        if line.startswith(">"):
            if header:
                fasta_dict[header] = seq
            header = line[1:]
            fasta_dict[header] = ''
            seq = ''
        else:
            seq = seq + line
    if header:
        fasta_dict[header] = seq

for keys, values in fasta_dict.items():
    A = values.count("A")
    T = values.count("T")
    G = values.count("G")
    C = values.count("C")
    print(keys)
    print(f"A: {A}, T: {T}, G: {G}, C: {C}")


