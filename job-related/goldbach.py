def goldbach_partitions(n):
    partitions = []
    siev = siev_of_eratosthenes(n)
    already_added = []

    if n %2 != 0:
        return []

#consider array slicing


    for i in range(len(siev)):
        if siev[i] not in already_added:
            if siev[i] + siev[i] == n:
                partitions.append("%d + %d" %(siev[i], siev[i]))
                already_added.append(siev[i])
            for j in range(len(siev)): 
                if siev[i] != siev[j] and siev[i] + siev[j] == n:
                    partitions.append("%d + %d" %(siev[i], siev[j]))
                    already_added.append(siev[i])
                    already_added.append(siev[j])
    return partitions

#I need to get range of primes efficiently
#modified sieve of erotosthenes
#https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def siev_of_eratosthenes(n):
    multiples = []
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primes

print(goldbach_partitions(100))