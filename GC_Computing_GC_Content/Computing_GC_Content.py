f = open("rosalind_gc.txt", "r")
dna = {}
dna_id = ""
dna_seq = ""
for line in f:
    if line.startswith('>'):
        if len(dna_seq) != 0:
            dna[dna_id] = dna_seq
            dna_seq = ""
        dna_id = line.strip()[1:]
    else:
        dna_seq += line.strip()
f.close()

max_gc = 0
max_gc_id = ""
for dna_id in dna:
    dna_seq = dna.get(dna_id)
    gc_cnt = dna_seq.count('C') + dna_seq.count('G')
    gc = gc_cnt / len(dna_seq) * 100
    if gc > max_gc:
        max_gc = gc
        max_gc_id = dna_id

f = open("rosalind_gc_output.txt", "w")
f.write(max_gc_id + "\n%.6f" % max_gc)
f.close()