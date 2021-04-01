

def report(s, t, u):
    r = 'X^3'
    
    if s > 0:
        r += ' - ' + str(s) + 'X^2'
    elif s < 0:
        r += ' + ' + str(-s) + 'X^2'

    if t > 0:
        r += ' - ' + str(t) + 'X'
    elif t < 0:
        r += ' + ' + str(-t) + 'X'

    if u > 0:
        r += ' - ' + str(u)
    elif u < 0:
        r += ' + ' + str(-u)

    r += ' = 0'
    return r
    
while True:
    x1 = float(input('x1 = '))
    x2 = float(input('x2 = '))
    x3 = float(input('x3 = '))

    a = x1 + x2 + x3
    b = (x1*x2) + (x2*x3) + (x1*x3)
    c = x1 * x2 * x3

    equation = report(a, b, c)

    if x1==0 and x2==0 and x3==0:
        print(equation)
        print('The program is terminated.')
        break
    else:
        print(equation)
        print('-----------------------------------------\n')
        
