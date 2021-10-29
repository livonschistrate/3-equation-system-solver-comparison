import numpy as np

filename = 'system.txt'

numbers = np.empty((0, 3), int)
r = np.empty((0, 3), str)

with open(filename) as fdc:  # descriptor ce citeste tot continutul intr-un string
    content = fdc.read()

with open(filename) as fdl:  # descriptor ce citeste toate liniile
    lines = fdl.readlines()

print(lines, "\n")

content = content.replace(' ', '')

print("Sistemul din fisier este:\n", content)

r_number = ''  # variabila pentru numarul din egalitate
c_number = ''  # variabila pentru coeficienti
pr = 0  # verificam daca am trecut de '='

for line in lines:

    line = line.replace(' ', '')  # daca exista spatii intre caractere

    # verificam existenta necunoscutelor
    ex = line.count('x')
    ey = line.count('y')
    ez = line.count('z')

    row = np.chararray(0, 3)

    for ch in line:
        if ch in ['x', 'y', 'z']:
            if np.any([c_number == '', c_number == '-']):  # exista x,y sau z dar au coeficientul 1
                row = np.append(row, '1')
            else:
                row = np.append(row, c_number)
                c_number = ''

        if ch in ['-'] and pr != 1:  # coeficientul este un numar negativ
            c_number = np.char.add(c_number, ch)
        elif ch.isdigit() and pr != 1:  # caracterul este o cifra si nu apare dupa '='
            c_number = np.char.add(c_number, ch)

        if ch in ['=']:  # apare semnul '='
            pr = 1
            if ez == 0:  # coeficientul lui z este 0
                row = np.append(row, '0')
            if ey == 0:  # coeficientul lui y este 0
                if (ez == 0):
                    row = np.append(row, '0')
                else:
                    row = np.append(row, '0')
                    row[[0, 1]] = row[[1, 0]]
            if ex == 0:  # coeficientul lui x este 0
                if ey == 0:
                    row = np.append(row, '0')
                    row[[1, 2]] = row[[2, 1]]
                elif ez == 0:
                    row = np.append(row, '0')
                    row[[0, 1]] = row[[1, 0]]
                else:
                    row = np.append(row, '0')
                    row[[1, 2]] = row[[2, 1]]
                    row[[0, 1]] = row[[1, 0]]

        if ch in ['-'] and pr == 1:  # numarul din egalitate este negativ
            r_number = np.char.add(r_number, ch)
        elif ch.isdigit() and pr == 1:  # caracterul este o cifra si apare dupa '=' urmand sa apara in vectorul r
            r_number = np.char.add(r_number, ch)

    r = np.append(r, [r_number])
    r_number = ''

    # resetam in acelasi timp si indicatoarele
    pr = 0
    ex = 0
    ey = 0
    ez = 0

    # row = ctoi(row)
    numbers = np.append(numbers, row)

# r = ctoi(r)
numbers = numbers.astype(np.int32)
r = r.astype(np.int32)
print(numbers)
print(r)

matrix = np.reshape(numbers, (3, 3))

print(matrix)

print("Determinantul este:", np.linalg.det(matrix), "\n")

print("Matricea transpusa:\n", matrix.transpose(), "\n")

print("Matricea inversa:\n", np.linalg.inv(matrix), "\n")

print("Matricea rezultata:\n", np.dot(np.linalg.inv(matrix), r), "\n")