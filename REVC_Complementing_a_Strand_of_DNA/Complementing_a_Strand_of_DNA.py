f = open("rosalind_revc.txt", "r")
dna = f.read().strip()
f.close()

reverse = ""

for nucleotide in dna:
    if nucleotide == 'A':
        reverse = 'T' + reverse
    elif nucleotide == 'C':
        reverse = 'G' + reverse
    elif nucleotide == 'G':
        reverse = 'C' + reverse
    elif nucleotide == 'T':
        reverse = 'A' + reverse

f = open("rosalind_revc_output.txt", "w")
f.write(reverse)
f.close()