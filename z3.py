def min_steps(p):
    n = len(p) - 1
    table = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            table[i][j] = float('inf')
            for k in range(i, j):
                q = table[i][k] + table[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < table[i][j]:
                    table[i][j] = q
                    s[i][j] = k

    return table[1][len(table) - 1], s



def line_of_multiply(s, i, j):
    global chain_line, letter
    if i == j:
        chain_line += letter
        letter = chr(ord(letter) + 1)
    else:
        chain_line += "("
        line_of_multiply(s, i, s[i][j])
        line_of_multiply(s, s[i][j] + 1, j)
        chain_line += ")"


chain_line = ''
letter = 'A'

p = [10, 30, 5, 60]
m, s = min_steps(p)
print(m)
line_of_multiply(s, 0, len(p)-2)
print(chain_line)