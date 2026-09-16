import math

def get_primes_list(biggest_num):
    numbers = list(range(2, biggest_num+2))
    numbers[-1] = -1
    n = 2
    i = 1
    j = 1
    start = 1
    last = biggest_num-1
    while n < math.sqrt(biggest_num):
        if numbers[i] % n == 0:
            numbers[i] = -1
        else:
            if j < i:
                numbers[j] = numbers[i]
                numbers[i] = -1
            j += 1
        i += 1
        if numbers[i] == -1:
            n = numbers[start]
            start += 1
            last = j
            i = start
            j = i
    return numbers[:last]
