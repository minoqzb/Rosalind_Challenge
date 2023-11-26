f = open("rosalind_cons.txt", "r")
dna = []
seq = ""
for line in f:
    if line.startswith('>'):
        if len(seq) > 0:
            dna.append(seq)
            seq = ""
    else:
        seq += line.strip()
dna.append(seq)
f.close()

profile = [[0 for i in range(len(dna[0]))] for j in range(4)]
for seq in dna:
    for i in range(len(seq)):
        if seq[i] == 'A':
            profile[0][i] += 1
        elif seq[i] == 'C':
            profile[1][i] += 1
        elif seq[i] == 'G':
            profile[2][i] += 1
        elif seq[i] == 'T':
            profile[3][i] += 1

consensus = ""
for i in range(len(profile[0])):
    most_common_cnt = 0
    most_common_nucleotide = 0
    for j in range(len(profile)):
        if profile[j][i] > most_common_cnt:
            most_common_cnt = profile[j][i]
            most_common_nucleotide = j
    if most_common_nucleotide == 0:
        consensus += "A"
    elif most_common_nucleotide == 1:
        consensus += "C"
    elif most_common_nucleotide == 2:
        consensus += "G"
    elif most_common_nucleotide == 3:
        consensus += "T"

f = open("rosalind_cons_output.txt", "w")
f.write(consensus + "\n")
for i in range(len(profile)):
    if i == 0:
        f.write("A:")
    elif i == 1:
        f.write("C:")
    elif i == 2:
        f.write("G:")
    elif i == 3:
        f.write("T:")
    for count in profile[i]:
        f.write(" " + str(count))
    f.write("\n")
f.close()