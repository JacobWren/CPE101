# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Calcudoku Project
# Term:         Winter 2020


def main():
    Num_cages = int(input())
    l = []
    for i in range(0, Num_cages):
        hold = input()
        l.append(hold.split())
    n = nest_list_max(l)
    N = int(n ** 2)
    matx = make_zeros(n)
    short_matx = del_one(l)
    matx_1D = flatten(matx)
 
    i = 0
    while i < N:
        index = i
        matx_1D[i] = matx_1D[i] + 1 # Increment the value in the current cell by 1 (starting from the top-left cell)
        if matx_1D[i] > n:
            matx_1D[i] = 0
            i = i - 1
        elif (valid_row(n, matx_1D, index) and valid_col(n, N, matx_1D, index)
              and invalid_too_big(l, index, matx_1D, short_matx) and
              invalid_not_equal(l, index, matx_1D, short_matx)):
            i = i + 1
    for k in range(0, N, n):
        print( * matx_1D[k: k + n] , sep = ' ')
    
    
# Max value in 1D list
def find_max(ls):
    count = 0
    for j in ls:
        j = int(j)
        if count == 0:
            mx = j
        if mx >= j and count != 0:
            mx = mx
        else:
            mx = j
        count = count + 1
    return mx


# Max value in 2D list
def nest_list_max(l):
    count = 0
    for i in l:
        if count == 0:
            default = find_max(i)
        elif default >= find_max(i) and count != 0:
            default = default
        else:
            default = find_max(i)
        count = count + 1
    return int((int(default) + 1) ** (1 / 2)) 
    
    
# grid of zeros    
def make_zeros(n):
    p = []
    p_prime = []
    for i in range(0, n):
        p.append(0)
    for k in range(0, n):
        p_prime.append(p)
    return p_prime


# Flatten list
def flatten(matx):
    matx_1D = [j for i in matx for j in i]
    return matx_1D


def valid_row(n, matx_1D, index): 
    start = int((index // n) * n)
    # Check for duplicates
    mini = matx_1D[start: start + n]
    if mini.count(matx_1D[index]) > 1:
        return False
    return True


def valid_col(n, N, matx_1D, index): 
    start = int(index % n)
    # Check for duplicates
    mini = matx_1D[start: start + N - n + 1: n]
    if mini.count(matx_1D[index]) > 1:
        return False
    return True

            
# delete first element of each inner list            
def del_one(l):
    l_prime = []
    for j in l:
        l_prime.append(j[1:])
    return l_prime


def cage_index(l, index, short_matx):
    j = 0
    for i in short_matx:
        if str(index) in i:
            return j
        j = j + 1


    
def partial_full(l, index, short_matx):
    spot = cage_index(l, index, short_matx) # cage index
    cage_length = len(short_matx[spot]) - 1 # cage length - 1
    inner_index = short_matx[spot].index(str(index)) # index of index in inner list
    if cage_length > inner_index:
        return True
    return False


# only use if partial_full is True!
def invalid_too_big(l, index, matx_1D, short_matx): 
    if partial_full(l, index, short_matx):
        spot = cage_index(l, index, short_matx) # cage index
        tot = int(l[spot][0]) # Sum of cage
        short_matx = short_matx # no total element
        inner_index = short_matx[spot].index(str(index)) # index of index in inner list
        partial_sum = 0
        j = 0
        for g in short_matx[spot]:
            if j <= inner_index: # don't add the last element in inner list
                partial_sum = partial_sum + matx_1D[int(g)]
            j = j + 1
        tot = int(l[spot][0]) # Sum of cage
        if partial_sum >= tot:
            return False
        return True
    return True


# check if we are at last value in the cage
def last_value(l, index, short_matx):
    short_matx = short_matx # no total element
    spot = cage_index(l, index, short_matx ) # cage index
    cage_length = len(short_matx[spot]) - 1 # cage length - 1
    inner_index = short_matx[spot].index(str(index)) # index of index in inner list
    if cage_length == inner_index: # last value check
        return True
    return False


# only use if last_value is True!
def invalid_not_equal(l, index, matx_1D, short_matx): #4
    if last_value(l, index, short_matx):
        spot = cage_index(l, index, short_matx) # cage index
        tot = int(l[spot][0]) # Sum of cage
        short_matx = short_matx # no total element
        inner_index = short_matx[spot].index(str(index)) # index of index in inner list
        total_sum = 0
        for i in short_matx[spot]:
            total_sum = total_sum + matx_1D[int(i)]
        tot = int(l[spot][0]) # Sum of cage
        if total_sum != tot:
            return False
        return True
    return True
    
        
if __name__ == "__main__":
    main()
