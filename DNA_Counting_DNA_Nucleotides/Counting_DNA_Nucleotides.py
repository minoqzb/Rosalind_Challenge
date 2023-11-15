f = open("rosalind_dna.txt", "r")
dna_seq = f.read().strip()
f. close()

A_cnt = 0
C_cnt = 0
G_cnt = 0
T_cnt = 0

for nucleobase in dna_seq:
    if nucleobase == 'A':
        A_cnt += 1
    elif nucleobase == 'C':
        C_cnt += 1
    elif nucleobase == 'G':
        G_cnt += 1
    elif nucleobase == 'T':
        T_cnt += 1

f = open("rosalind_dna_output.txt", "w")
f.write(str(A_cnt) + " " + str(C_cnt) + " " + str(G_cnt) + " " + str(T_cnt))