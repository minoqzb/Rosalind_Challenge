f = open("rosalind_rna.txt", "r")
dna_seq = f.read().strip()
f.close()

rna_seq = ""

for nucleotide in dna_seq:
    if nucleotide == 'T':
        rna_seq += 'U'
    else:
        rna_seq += nucleotide

f = open("rosalind_rna_output.txt", "w")
f.write(rna_seq)
f.close()