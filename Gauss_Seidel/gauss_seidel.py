#Gauss-Seidel method

def print_matrix(matrix):
    for line in matrix:
        l = '';
        for element in line:
            l = l + str(element) + ' '
            #print(element," ")
        print(l)


#matrix = [[int(num) for num in line.split(' ')] for line in file ]
#print_matrix(matrix)


num_lines = len(open('matrix.txt').readlines())
file = open ( 'matrix.txt' , 'r')

values = []
columns = []
lines = [0]
count = 0
i = 0
for l in file:
    numbers = list(map(int,l.split(' ')))
    count = 0
    for j in range(len(numbers)):
        if numbers[j] != 0:
            values.append(numbers[j])
            columns.append(j)
            count += 1
    if i != num_lines-1:
        lines.append(lines[i]+count)
    i += 1

print(values)
print(columns)
print(lines)

file.close()

result = []
for i in range(len(lines)):
    result.append(0)

file = open('b_array.txt','r')
l = file.readline()
b = [int(num) for num in l.split(' ')]
file.close()
print(b)

print(result)


for i in range(len(result)):
    start = lines[i]
    sum = 0
    diagonal = 0

    if i != len(result)-1:
        quant = lines[i+1] - lines[i]
    else:
        quant = len(values) - start

    for k in range(quant):
        if i != columns[start+k]:
            sum += values[start+k]
        else:
            diagonal = values[start+k]
    result[i] = (b[i] - sum)/diagonal
print(result)
