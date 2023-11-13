f = open("rosalind_dna.txt", "r")

dna_seq = f.read()
dna_seq = dna_seq.strip()

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

print(A_cnt, C_cnt, G_cnt, T_cnt)