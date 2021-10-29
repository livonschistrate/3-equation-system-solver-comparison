filename = 'system.txt'

numbers =['']
r = ['']

with open(filename) as fdc: # descriptor ce citeste tot continutul intr-un string
    content = fdc.read()

with open(filename) as fdl: # descriptor ce citeste toate liniile
    lines = fdl.readlines()

print(lines,"\n")

content = content.replace(' ','')

print("Sistemul din fisier este:\n",content)

def ctoi(numbers):   # functie care converteste din char in int toate elementele din vector
    for i in range(len(numbers)):
        numbers[i] = (int(numbers[i]))
    return numbers


pr = 0 # verificam daca am trecut de '='
ex = 0 # verificam daca exista x
ey = 0 # verificam daca exista y
ez = 0 # verificam daca exista z


for line in lines:

    line = line.replace(' ','') # daca exista spatii intre caractere

    # verificam existenta necunoscutelor
    ex = line.count('x')
    ey = line.count('y')
    ez = line.count('z')

    for ch in line:
        if ch in ['x','y','z']: 
            if numbers[len(numbers) - 1] == '' or numbers[len(numbers) - 1] == '-': # exista x,y sau z dar au coeficientul 1
                numbers[len(numbers) - 1] += '1'

        if ch in ['-'] and pr != 1: # coeficientul este un numar negativ
            numbers[len(numbers) - 1] += ch
        elif ch.isdigit() and pr != 1: # caracterul este o cifra si nu apare dupa '='
            numbers[len(numbers) - 1] += ch
        elif len(numbers[len(numbers) - 1]) != 0: # coeficientul creat este introdus in vectorul cu coeficienti
                numbers.append('')
                
        if ch in ['=']: # apare semnul '='
            pr = 1
            if ez == 0: # coeficientul lui z este 0
                numbers.pop(len(numbers)-1) # stergem spatiul gol care apare inaintea lui 0
                numbers.append('0')
            if ey == 0: # coeficientul lui y este 0
                if ez == 0:
                    numbers.append('0')
                else:
                    numbers.pop(len(numbers)-1)
                    numbers.append('0')
                    numbers[len(numbers) - 1], numbers[len(numbers) - 2] = numbers[len(numbers) - 2], numbers[len(numbers) - 1]
            if ex == 0: # coeficientul lui x este 0
                if ey == 0:
                    numbers.append('0')
                    numbers[len(numbers) - 1], numbers[len(numbers) - 2] = numbers[len(numbers) - 2], numbers[len(numbers) - 1]
                elif ez == 0:
                    numbers.append('0')
                    numbers[len(numbers) - 2], numbers[len(numbers) - 3] = numbers[len(numbers) - 3], numbers[len(numbers) - 2]
                else:
                    numbers.pop(len(numbers)-1)
                    numbers.append('0')
                    numbers[len(numbers) - 1], numbers[len(numbers) - 2] = numbers[len(numbers) - 2], numbers[len(numbers) - 1]
                    numbers[len(numbers) - 2], numbers[len(numbers) - 3] = numbers[len(numbers) - 3], numbers[len(numbers) - 2]

        if ch in ['-'] and pr == 1: # numarul din egalitate este negativ
            r[len(r) - 1] += ch
        elif ch.isdigit() and pr == 1: # caracterul este o cifra si apare dupa '=' urmand sa apara in vectorul r
            r[len(r) - 1] += ch
        elif len(r[len(r) - 1]) != 0: # numarul este introdus in vectorul cu egalitati
                r.append('')
                # resetam in acelasi timp si indicatoarele
                pr = 0
                ex = 0
                ey = 0
                ez = 0

numbers.pop() # apare '' la sfarsitul listei
matrix = [ [0 for i in range(3)] for j in range(3) ] # cream matricea
index = 0
print(numbers)
print(r)

# convertim coeficientii obtinuti
numbers = ctoi(numbers)
r = ctoi(r)


# introducem coeficientii in matrice
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        matrix[row][col] = numbers[index]
        index += 1
        

print(matrix)

# functie care calculeaza determinantul unei matrici 2x2 - folositor la crearea matricii adjuncte
def det_2x2(A):
    det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    return det

# functie pentru determinantul matricii
def det_matrix(A):
    
    det = 0
    for col in range(len(A[0])):
        Ac = A
        Ac = Ac[1:] # stergem prima linie
        for row in range(len(Ac)):
            Ac[row] = Ac[row][0:col] + Ac[row][col+1:] 
        minidet = det_2x2(Ac)
        det += A[0][col] * minidet * ((-1) ** col)

    return det

# transpusa matricii
def transpose(A):
    newA = []
    for row in range(len(A[0])):
        newrow = []
        for col in range(len(A)):
            newrow.append(A[col][row])
        newA.append(newrow)

    return newA

# adjuncta matricii
def adjoint(A):
    transA = transpose(A)
    adjoint = []
    for row in range(len(transA)):
        newrow = []
        for col in range(len(transA[0])):
            transAc = transA
            transAc = transAc[:row] + transAc[row+1:]
            for Trow in range(len(transAc)):
                transAc[Trow] = transAc[Trow][0:col] + transAc[Trow][col+1:]
            minidet = det_2x2(transAc)
            element = ((-1) ** (row+col)) * minidet
            newrow.append(element)
        adjoint.append(newrow)
    
    return adjoint

            
determinant = det_matrix(matrix)

print("Determinantul este:", determinant, "\n")

transpose_matrix = transpose(matrix)

print("Transpusa este:\n", transpose_matrix)

adjoint_matrix = adjoint(matrix)

print("Matricea adjuncta:\n", adjoint_matrix)

# determinam inversa matricii
if determinant == 0:
    print("Determinantul este nul si nu poate fi calculat astfel inversa matricei.")
    exit
else:
    reverse_matrix = []
    for row in range(len(adjoint_matrix)):
        newrow = []
        for col in range(len(adjoint_matrix[0])):
            element = adjoint_matrix[row][col] / determinant
            newrow.append(element)
        reverse_matrix.append(newrow)

print("Matricea inversa:\n", reverse_matrix)

result = []
for row in range(len(reverse_matrix)):
    newrow = []
    element = 0
    row_r = 0
    for col in range(len(reverse_matrix[0])):
        element += reverse_matrix[row][col] * r[row_r]
        row_r += 1
    newrow.append(element)
    result.append(newrow)

print("Matricea rezultata:\n", result)


