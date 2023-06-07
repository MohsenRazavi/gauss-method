n = int(input('n: '))
mat = [[float(j) for j in input().split()] for i in range(n)]

equations = []

variables = {f'x{i}':0 for i in range(1, n+1)}

for i in range(n - 1):  # choose which index should be zero
    for j in range(i + 1, n):  # choose which row
        m = -mat[j][i] / mat[i][i]
        for k in range(len(mat[j])):  # make ith index of jth row zero
            mat[j][k] += mat[i][k] * m

for i in range(n, 0, -1):
    t = mat[i-1][-1]
    for j in range(1,n):
        t -= mat[i-1][j]*variables[f'x{j+1}']
    variables[f'x{i}'] = t / mat[i-1][i-1]

# creating equations ...
for i in range(n):
    equation = ''
    for j in range(i, n):
        equation += f'{mat[i][j]}*x{j+1} + '
    equation = equation[:-2] + f'= {mat[i][-1]}'
    equations.append(equation)

print(equations)
print(variables)
