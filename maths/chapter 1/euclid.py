
def algo_hcf(num1, num2):
    smaller = num1 if num1 < num2 else num2
    greater = num1 if num1 > num2 else num2
    while True:
        quatient = greater // smaller
        remainder = greater % smaller
        print(greater,'=',smaller,'x',quatient,'+',remainder)
        greater = smaller
        smaller = remainder
        if remainder == 0: break
 
if __name__ == '__main__':
    num1 = int(input('enter num1: '))
    num2 = int(input('enter num2: '))
    algo_hcf(num1, num2)