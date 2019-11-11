# Fibonacci
def fibo(urut) :
    listData = [1,1]
    for i in range(2,urut):
        listData.append(listData[i-2] + listData[i-1])
    print(listData[-1])

fibo(9)


# Vice Versa
def viceVersa(x):
    y = ''
    for i in x:
        if i.isupper():
            a = i.lower()
        else:
            a = i.upper()
        y += a
    print(y)

viceVersa('AbcdEFgHi')


# Clockwise matriks
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x = []
y = []
for i in range(len(matriks)):
    for j in range(len(matriks[0])):
        x.append(matriks[j][i])
    y.append(x)
    x = []
print(y)