A = input('input number:')
Num = int(A)
X = str(Num % 5)
Num = Num / 5
while Num > 0:
    X = str(Num % 5) + X
    Num = Num/5
print X 

