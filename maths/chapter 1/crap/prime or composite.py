while True:
    num = int(input("what's the number: "))
    for i in range(2, num):
        if num % i == 0:
            print("it's a composite number and it is devesible by", i)
            break
        else:
            print("it's a prime")
            break
