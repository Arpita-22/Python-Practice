def palindrome():
    userInput = input("Enter a sequence:")
    
    reverse = ""

    for char in userInput:
        reverse = char + reverse

    if reverse == userInput:
        print(f'{userInput} is a Palindrome')

    else:
        print(f'{userInput} is not a Palindrome')

palindrome()