f = open("rosalind_hamm.txt", "r")
dna = []
for line in f:
    dna.append(line.strip())
f.close()

hamming_dist = 0
for i in range(len(dna[0])):
    if dna[0][i] != dna[1][i]:
        hamming_dist += 1

f = open("rosalind_hamm_output.txt", "w")
f.write(str(hamming_dist))
f.close()