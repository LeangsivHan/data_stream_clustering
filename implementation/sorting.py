from ulab import numpy as np

# Custom less comparator
def lessPoints(lhs, rhs):
    return (lhs[0] < rhs[0]) or ((lhs[0] == rhs[0]) and (lhs[1] < rhs[1])) 

# Custom less or equal comparator
def lessEqualPoints(lhs, rhs):
    return (lhs[0] <= rhs[0]) or ((lhs[0] == rhs[0]) and (lhs[1] <= rhs[1]))

# Custom greater comparator
def greaterPoints(lhs, rhs):
#     print(f"lhs[0] = {lhs[0]}, lhs[1] = {lhs[1]} | rhs[0] = {rhs[0]}, rhs[1] = {rhs[1]}")
#     print(f"Greater Points = {(lhs[0] > rhs[0]) or ((lhs[0] == rhs[0]) and (lhs[1] > rhs[1]))}")
#     return (lhs[0] > rhs[0]) or ((lhs[0] == rhs[0]) and (lhs[1] > rhs[1]))
    return (lhs[0] > rhs[0]) or ((lhs[0] == rhs[0]) and (lhs[1] > rhs[1]))

# Costom greater or equal comparator
def greaterEqualPoints(lhs, rhs):
    return (lhs[0] >= rhs[0]) or ((lhs[0] == rhs[0]) and (lhs[1] >= rhs[1]))

# Custom equal comparator
def equalPoints(lhs, rhs):
    return (lhs[0] == rhs[0]) and (lhs[1] == rhs[1])

# Swapping two value of numpy ndarray
def swap(arr, a, b):
    # arr[[a, b]] = arr[[b, a]]
    tmp = arr[a] * 1
    arr[a] = arr[b]
    arr[b] = tmp


MAX_LEVELS = 64

def quickSort_without_stack_or_recursion(arr, elements): #arr is array for Points, elements is an integer
#     beg = [0] * MAX_LEVELS
#     end = [0] * MAX_LEVELS
    beg = np.zeros(MAX_LEVELS, dtype=np.int16) # dype=np.int16: use in micropython
    end = np.zeros(MAX_LEVELS, dtype=np.int16) # dype=np.int16: use in micropython
#     L, R = 0,0
    i = 0
    
    beg[0] = 0
    end[0] = elements
    while (i >= 0):
        L = beg[i]
        R = end[i]
        
        if ((R - L) > 1):
            M = L + ((R - L) >> 1)

#             piv = arr[M].copy()
            piv = arr[M] * 1

            swap(arr, M, L)

            if (i == MAX_LEVELS - 1):
                return -1
            R -= 1
            while(L < R):
                # Change from "greaterEqualPoints" to "greaterPoints"
                while(greaterPoints(arr[R], piv) and L < R):
                    R -= 1
                if (L < R):
                    swap(arr, L, R)
                    L += 1
                # Change from "lessEqualPoints" to "lessPoints"
                while(lessPoints(arr[L], piv) and L < R):
                    L += 1
                if (L < R):
                    swap(arr, R, L)
                    R -= 1
                    
            arr[L] = piv
            M = L + 1
            while (L > beg[i] and equalPoints(arr[L - 1], piv)):
                L -= 1
            while (M < end[i] and equalPoints(arr[M], piv)):
                M += 1
            if (L - beg[i] > end[i] - M):
                beg[i + 1] = M
                end[i + 1] = end[i]
                end[i] = L
                i += 1
            else:
                beg[i + 1] = beg[i]
                end[i + 1] = L
                beg[i] = M
                i += 1
        else:
            i -= 1
    return 0

##################
##### RESULT #####
##################
# using Numpy as the data

# TODO: - Testing
# from ulab import numpy as np
# p = np.array([[9,12], [1,3], [13,20], [10,10], [10,9]], dtype=np.int16)
# p = [[9,12], [1,3], [13,20], [10,10], [10,9]]
# p = np.array([[100,5], [90,5], [110,5], [97,4], [102,4], [112,4], [92,4], [95,3], [90,3], [100,3],
#      [110,5], [100,5], [110,4], [93,3], [107,2], [117,3], [96,2], [105,3], [100,3], [110,3],
#      [60,1], [70,1],[40,1], [70,3], [50,1], [80,0],[50,0],[60,1],[60,1],[55,0],
#      [40,1], [45,1],[40,0], [55,3], [60,1], [65,0],[70,0],[51,2],[51,1],[48,0]])
# n = len(p)
# # print(f"n = {n}")
# quickSort_without_stack_or_recursion(p, n)
# print(p)