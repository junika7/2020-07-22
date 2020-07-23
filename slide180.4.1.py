def count_bases (fasta_file):
    sequence=''
    def count():
        if len(sequence):
            print("Number of A's: %d" % sequence.count("A"))
            print("Number of C's: %d" % sequence.count("C"))
            print("Number of G's: %d" % sequence.count("G"))
            print("Number of T's: %d" % sequence.count("T"))
            print()
    with open(fasta_file) as handle:
        i=1
        for seqs in handle:
            if seqs.startswith('>'):
                count()
                print("Sequence %d:" % i)
                i=i+1
                sequence=''
            else:
                sequence=sequence+seqs.strip()
        count()

result = count_bases('multiple_sequences.fasta')
