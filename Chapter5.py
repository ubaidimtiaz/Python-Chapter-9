import time
import turtle

bob = turtle.Turtle()
def countdown(n):
    if n<0:
        print("Done")
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)




z = (time.time())


def conv(ft):

        mt= ft//60
        se=round(ft%60,2)
        # ht=mt//60
        ht = ft // 60//60
        mi=mt%60
        d=ft//60//60//24
        hr=ht%24
        print(d,'days', hr, 'hours', mi,'minutes and', se, 'seconds')


def check_fermat(a, b, c,n):

        lhs= a**n + b**n
        print(lhs)
        rhs=c**n
        print(rhs)
        if lhs==rhs:
            print('Holy smoked fermat was wrong')
        else:
            print('No that doestn work')



def take():
        a, b, c, n = input('Please enter values for a,b,c,n separated by space\n').split()
        if int(n) < 2:
            print ('Please enter n greater than 2')
            take()
        else:
            check_fermat(int(a), int(b), int(c), int(n))


def is_traingle(a, b, c):
    if c>a+b or a>b+c or b>a+c:
        print('No')
    else:
        print('Yes')


def input_triangle():
    a, b,c = input('Please enter the length of the 3 stick').split()
    is_traingle(int(a), int(b), int(c))


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


draw(bob, 4, 10)