import random

def case1():
    numtex = '123456789'
    n1 = random.choice(numtex) 
    n2 = random.choice(numtex)
    n3 = random.choice(numtex) 
    n4 = random.choice(numtex)
    n5 = random.choice(numtex) 
    n6 = random.choice(numtex) 
    n7 = random.choice(numtex) 
    n8 = random.choice(numtex)
    n9 = random.choice(numtex)
    n10 = random.choice(numtex)
    n11 = random.choice(numtex)
    n12 = random.choice(numtex)
    print(n1, n2, n3, n4, n5, n6, 
          n7, n8, n9, n10, n11, n12)


def case2():
    num = '123456789'
    numtex = 'abcdefghijklmnopqrstuvwxyz'
    n1 = random.choice(num) 
    n2 = random.choice(num)
    n3 = random.choice(num) 
    n4 = random.choice(num)
    n5 = random.choice(num) 
    n6 = random.choice(num) 
    n7 = random.choice(numtex) 
    n8 = random.choice(numtex)
    n9 = random.choice(numtex)
    n10 = random.choice(numtex) 
    n11 = random.choice(numtex) 
    n12 = random.choice(numtex)   
    print(n1, n2, n3, n4, n5, n6, 
          n7, n8, n9, n10, n11, n12)

def case3():
    num = '123456789'
    numtex = 'abcdefghijklmnopqrstuvwxyz' \
            'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    n1 = random.choice(num) 
    n2 = random.choice(num)
    n3 = random.choice(num) 
    n4 = random.choice(num)
    n5 = random.choice(num) 
    n6 = random.choice(num) 
    n7 = random.choice(numtex) 
    n8 = random.choice(numtex)
    n9 = random.choice(numtex)
    n10 = random.choice(numtex) 
    n11 = random.choice(numtex) 
    n12 = random.choice(numtex)   
    print(n1, n2, n3, n4, n5, n6, 
          n7, n8, n9, n10, n11, n12)
