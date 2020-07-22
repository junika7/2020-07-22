from Bio import SeqIO

record = SeqIO.read("059.fasta", "fasta") #하나의 record가 있는 파일에 사용(여러개면 parse). 하나의 레코드가 있다는 것은 header가 1개고 sequence도 1개가 들어있는 파일이라는 뜻.

A = record.seq.count("A")
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(f"A: {A}")
print(f"C: {C}")
print(f"G: {G}")
print(f"T: {T}")
