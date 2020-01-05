import sys
import numpy as np


def print_matrix(M):
    for i in M:
        for j in i:
            print(j,end=' '),
        print()

####

def init_matrix():
    lines = sys.stdin.readlines() #input
    matrix = []

    # if its empty text file
    if (lines == []):
        exit(1)

    # if its text file with empty lines
    for line in lines:
        if(line == '\n'):
            exit(1)

    # turn lines to rows in matrix
    for line in lines:
        matrix.append(line.split())

    # remove spaces,tabs and new-lines from matrix
    res = []
    for row in matrix:
        res.append(list(filter(lambda x:x!='\t' and x!=' ' and x!='\n',row)))
    matrix = res

    # checks if the amount of elements in each
     # row is the same
    for line in matrix:
        if (len(line) != len(matrix[0])):
            exit(1)

    # string matrix to int matrix
    for i in matrix:
        for j in i:
            try:
                if(int(j)<0): exit(1) #exit if number is negetive
                matrix[matrix.index(i)][i.index(j)] = int(j) #change to int!
            except:
                exit(1)

    return np.array(matrix)

####

def gauss(M):
    inverse_z7 = [0,1,4,5,2,3,6]
    i,j = 0,0
    m,n = M.shape
    flag = False #if flag true, a column of zeros was found ->
                # so j++ and moving on to the next iteration

    # first do modulu 7 to each element in the matrix
    M[:, :] %= 7

    while(i<m and j<n):
        if(M[i,j] == 0):
            # checks for the first row with element != 0 (in column j)
            for x in range(i,m):
                if(M[x,j] != 0): # replace between the rows
                    tmp = M[i].copy()
                    M[i] = M[x].copy()
                    M[x] = tmp
                    break
                if(x == m-1): # if is the last row (then its zeros column)
                    j+=1
                    flag = True
        if(flag):
            flag = False
            continue

        # Normalization operation:
        #   changes the opening coefficient(which is not zero)to digit 1
        factor = M[i,j]
        M[i, :] = (M[i, :] * inverse_z7[factor]) % 7  # nirmul

        # turn all elements that below the digit 1 to zeros!
        for x in range(i+1,m):
            if(x>=m): break  # avoid index matrix exception
            M[x, :] = (M[x, :] - (M[x, j] * M[i, :])%7) % 7

        i+=1
        j+=1

    #makes the matrix canonical:
    # when this stage wiil end, all elements above the opening element (1)
    # in the same column will be equal to zero.
    for x in range(m-1,0,-1):
        for y in range(0,n):
            if(M[x,y] == 1):
                for row in range(x-1,-1,-1):
                    M[row,:] = (M[row,:] - (M[x,:]*M[row,y])%7 )%7
                break
            else: #if M[x,y] == 0
                continue
            break

    return M


#####

##run program:

M = init_matrix()
print_matrix(gauss(M))



