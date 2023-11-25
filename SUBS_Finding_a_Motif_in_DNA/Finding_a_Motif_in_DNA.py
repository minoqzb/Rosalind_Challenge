f = open("rosalind_subs.txt", "r")
s = f.readline().strip()
t = f.readline().strip()
f.close()

locations = []
for i in range(len(s) - len(t) + 1):
    if s[i : i + len(t)] == t:
        locations.append(i + 1)

f = open("rosalind_subs_output.txt", "w")
for location in locations:
    f.write(str(location) + " ")
f.close()