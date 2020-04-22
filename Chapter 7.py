import time
import math
from Chapter6 import factorial
def countdown(n):
    while n>0:
        print(n)
        time.sleep(1)
        n= n - 1
    print('Blast of')

def kehnsa(n):
    while n!= 1:
        print(n)
        time.sleep(1)
        if n%2==0:
            n=n/2
        else:
            n=n+1
    print("n gov 1")

def abc(x,a):
    while True:
        y=(x+a/x)/2
        if round(y,3)==round(x,3):
            break
        x = y
    print(a, y, math.sqrt(a), abs(math.sqrt(a) - y))



def test_square_root():
    print('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff)')
    print('_','  ', '_ _ _ _ _ _', '  ', '_ _ _ _ _ _ _', '  ',  '_ _ _ _ _')
    a=1
    x=1
    while True:
        abc(x,a)
        a=a+1
        x=x+1
        if a ==10:
            break

def eval_loop():
    while True:
        x = input('>')
        if x =='done':
            break
        print(eval(x))


def estimate_pi():
    out= (2*math.sqrt(2))/(9801)
    k=0
    total=0
    while True:
        top=factorial(4*k)*(1103+26390*k)
        bottom=(factorial(k)**4)*((396**(4*k)))
        shabash=(top/bottom)
        k=k+1
        print(shabash)
        total=total+shabash
        if shabash<(1e-15):
            break
    return (1/(out*total))


print(estimate_pi())
print(math.pi)
