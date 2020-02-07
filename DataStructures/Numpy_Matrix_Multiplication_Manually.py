matr = [[12,7,3],[4 ,5,6],[7 ,8,9]]
natr = [[5,8,1],[6,7,3],[4,5,9]]

res = [[0]*3 for _ in range(3)]

for i in range(3):  # as the matrix above is 3X3
    for j in range(3):
        for k in range(3):
            res[i][j] += matr[i][k] * natr[k][j]

print(res)

"""
            0     1     2
        
    0      00     01   02    
    1      10     11   12
    2      20     21   22
    
    [ 00*00 + 01*10 + 02*20         00*01 + 01*11 + 02*21           00*02 + 01*12 + 02*22 ]
    [ 10*00 + 11*10 + 12*20         10*01 + 11*11 + 12*21           10*01 + 11*12 + 12*22 ]
    [ 20*00 + 21*10 + 22*20         20*01 + 21*11 + 22*21           20*01 + 21*12 + 22*22 ] 
    
    Thats how the Algebric Matrix Multiplication is done.
    We have just implemented this in the Above code.

    To escape such writing, numpy is used as it has in_built operators to do the matrices work like,
    * , @ , .dot , multiply , etc.
"""







