f = open("rosalind_revc.txt", "r")

dna = f.read().strip()
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

print(reverse)