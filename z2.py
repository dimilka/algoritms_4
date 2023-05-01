# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys

chain_line = ''
name = 'A'
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    # m[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float("inf")
            for k in range(i, j):

                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                s[i][j] = k

   # return m[1][n - 1]

    chain(s, 0, n-2)
    return m


def chain(s, i, j):
    global chain_line, name
    if i == j:
        chain_line += name
        name = chr(ord(name) + 1)
    else:
        chain_line += '('
        chain(s, i, s[i][j])
        chain(s, s[i][j] + 1, j)
        chain_line += ')'

arr = [10, 30, 5, 60]
size = len(arr)

answer = (MatrixChainOrder(arr, size))

print('\n', answer[1][size-1])
print(chain_line)