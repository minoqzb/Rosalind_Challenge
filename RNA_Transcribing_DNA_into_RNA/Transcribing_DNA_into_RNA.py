f = open("rosalind_rna.txt", "r")

dna_seq = f.read().strip()
rna_seq = ""

for nucleotide in dna_seq:
    if nucleotide == 'T':
        rna_seq += 'U'
    else:
        rna_seq += nucleotide

print(rna_seq)