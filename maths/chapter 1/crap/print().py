while True:

    num1 = int(input('number1: '))
    num2 = int(input('number2: '))
    r = 1
    q = None

    while r >= 0:
        loop = 1
        if num1 > num2:
            divisor = num2
            dividend = num1

            try:
                q = divisor // dividend
            except ZeroDivisionError:
                break

            r = divisor % dividend
            num2 = num1
            num1 = r

            if loop == 1:
                loop += 1
                pass
            
            print(divisor, '=', dividend, 'X', q, '+', r)

        else:
            divisor = num2 
            dividend = num1

            try:
                q = divisor // dividend
            except ZeroDivisionError:
                break

            r = divisor % dividend
            num2 = num1
            num1 = r

            if loop == 1:
                loop += 1
                pass

            print(divisor, '=', dividend, 'X', q, '+', r)
