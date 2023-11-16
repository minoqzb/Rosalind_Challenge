def getNumberOfRabbitsRec(month, offspring):
    if month == 1 or month == 2:
        return 1
    else:
        return getNumberOfRabbitsRec(month - 1, offspring) + getNumberOfRabbitsRec(month - 2, offspring) * offspring


f = open("rosalind_fib.txt", "r")
int_arr = f.read().split(" ")
f.close()

n = int(int_arr[0])
k = int(int_arr[1])

f = open("rosalind_fib_output.txt", "w")
f.write(str(getNumberOfRabbitsRec(n, k)))
f.close()