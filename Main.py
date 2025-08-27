from utils import *
try:
    user = int(input("Option For You (1 - 3): "))
    match user:
        case 1:case1()
        case 2:case2()
        case 3:case3()
        case user: ("Enter Number Range 1 - 3")
except ValueError as e:
    print('Number Only',e)