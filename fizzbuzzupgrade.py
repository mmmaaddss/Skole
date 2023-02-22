print('Hvad skal jeg tælle til?') #guider useren
userrange = input() #tager imod et input

def isDisibleBy3(): #functioner, som gør koden mere læsbar
    if i % 3 == 0:
        print('fizz')
def isDisibleBy5():
    if i % 5 == 0:
        print('buzz') ##buzzzzer
def isDisibleBy3and5():
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')

for i in range(int(userrange)):
    if isDisibleBy3and5(): #kalder function
        continue
    elif isDisibleBy3():
        continue
    elif isDisibleBy5():
        continue
    print(i)
