# Alina Chadwick
# CS 31 Problem Set 3
# Select Algorithm using Partition
# Goal: O(n) run time

# returns the median of an array
def median(a, i, num):
    temp_list = []

    for i in range(i, i + num):
        temp_list.append(a[i])
    temp_list.sort()

    return temp_list[num // 2]

# partition algorithm used to arrange elements in the array based on a pivot
def partition(a, i, j, x):
    # permutes the array
    for k in range(i, j):
        if a[k] == x:
            a[j], a[k] = a[k], a[j]  # swaps in place
            break
    k = i
    x = a[j]
    for l in range(i, j):
        if a[l] <= x:
            a[k], a[l] = a[l], a[k]  # swaps in place
            k +=1
    a[k], a[j] = a[j], a[k]  # swaps in place
    return k

# print("Partition output: " + str(partition([1, 3, 5, 17], 0, 3, 2))) #test code


def select(a, i, j, k):
    # if the size of the array is one, return that value
    if i == j:
        return a[i]

    # check constraints
    if k< j - i + 1 and k > 0:
        num_elements = j - i + 1

        # to pick a valid pivot, we need to break the array into 5 parts and find medians
        m = 0
        med_array = []

        # find median of each block, append to an array
        while (m < num_elements // 5):
            med_array.append(median(a, i + m * 5, 5))
            m +=1

        if num_elements > m * 5:
            med_array.append(median(a, i + m * 5, num_elements % 5))
            m +=1

        # array is too small
        if m == 1:
            ultimate_median = med_array[m - 1]
        else:
            # obtain the median of the 5 medians using the select method
            ultimate_median = select(med_array, 0, m - 1, m //2)

         # use the new median to partition
        x = partition(a, i, j, ultimate_median)

        # recursively call select based on where k is
        if x - i + 1 == k:
             return a[x]
        if x - i + 1 > k:
            return select(a, i, x - 1, k)
        return select(a, x + 1, j, k - x + i - 1)



a = [12, 40, 355, 2, 66]
k = 3
print("Partition output: " + str(partition(a, 0, len(a) // 2, 2))) #test code
print("Select output: " + str(select(a, 0, len(a) - 1, k)))

b = [9, 12, 8, 30, 10, 5, 4, 3]
k = 4
print("Partition output: " + str(partition(b, 0, len(a) // 2, 1))) #test code
print("Select output: " + str(select(b, 0, len(a) - 1, k)))