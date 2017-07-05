"This is a test module"
A = input('a number:')
B = input('b number:')
C = raw_input('+,-,*,/:')
 
if C == '+':
    result = int(A)+int(B)
    print('a+b=' + str(result)) 
elif C == '-':
    result = int(A)-int(B)
    print('a-b=' + str(result))
elif C == '*':
    result = int(A)*int(B)
    print('a*b=' + str(result))
elif C == '/':
    result = int(A)/int(B)
    print('a/b=' + str(result))

else:
    print('error') 
  
