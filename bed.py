"""
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [.bed]")
    sys.exit()

f = sys.argv[1]

length = 0
whole_length = 0

with open(f, 'r') as handle:
    for line in handle:
        splitted = line.strip().split("\t")
        length = int(splitted[2]) - int(splitted[1])
        whole_length += length
    print(f"whole length: {whole_length}")
"""
#위에는 내가 한 것
#아래는 강사님이 한 것
total = 0

with open("077.bed", 'r') as handle:
    for line in handle:
        splitted = line.strip().split("\t")
        start = int(splitted[1])
        end = int(splitted[2])
        total += end - start

print(total)

