f = open("rosalind_iprb.txt", "r")
int_arr = f.read().split(' ')
f.close()

k = float(int_arr[0])  # homozygous dominant
m = float(int_arr[1])  # heterozygous
n = float(int_arr[2])  # homozygous recessive
pop = k + m + n

dominant_prob = k / pop * (k - 1) / (pop - 1) + \
                k / pop * m / (pop - 1) + \
                k / pop * n / (pop - 1) + \
                m / pop * k / (pop - 1) + \
                m / pop * (m - 1) / (pop - 1) * 0.75 + \
                m / pop * n / (pop - 1) * 0.5 + \
                n / pop * k / (pop - 1) + \
                n / pop * m / (pop - 1) * 0.5

f = open("rosalind_iprb_output.txt", "w")
f.write("%.5f" % dominant_prob)
f.close()
