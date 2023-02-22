
def giverAltidEnFloat(askThisQuestion):
    tastet = input(askThisQuestion)
    try:
        return float(tastet)
    except ValueError:
        print(f"Du tastede {tastet}... Det lykkedes ikke at tolke som et tal. Prøv igen...")
        return giverAltidEnFloat(askThisQuestion) #https://media.tenor.com/C_typNW6OgEAAAAC/recursion-winnie.gif

userrange = giverAltidEnFloat("Hvad skal jeg tælle til?")

def isDisibleBy3(): #functioner, som gør koden mere læsbar
    if i % 3 == 0:
        print('fizz')
def isDisibleBy5():
    if i % 5 == 0:
        print('buzz')
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
