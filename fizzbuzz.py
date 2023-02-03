for blah in range(100):
    if blah % 3 == 0 and blah % 5 == 0:
        print("fizzbuzz")
        continue
    elif blah % 3 == 0:
        print("fizz")
        continue
    elif blah % 5 == 0:
        print("buzz")
        continue
    print(blah)
