def fizzBuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if result == "":
        result = str(number)

    return result



def firstNumbers(highest):
    listOfResults = []
    for counter in range(1,highest+1):
        listOfResults.append(fizzBuzz(counter))
    return listOfResults

if __name__ == "__main__":
    print(firstNumbers(16))
