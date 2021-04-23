
# Provide a program that solves the following problem 
# (either in pseudo-code, or the language of your choice)

# You have a given word. You want to transform it into Pig Latin. 
# To do so, all letters before the initial vowel (a, e, i, o, u or y) are placed at the end of the word sequence. 
# Then, "ay" is added to the end of the word. 

# pig 	 =>  igpay
# banana =>  ananabay
# school =>  oolschay
# apple  =>  appleay
# year   =>  yearay

# You may use: string indexing/single character operations, lists, list length, loops, string concatenation
# You may not use: string slicing/multi-character operations, recursion




def pigLatin(word):
    n = len(word)
    indexOfVowel = -1 
    vowels = "aeiouy"
	
    for i in range(n):
        # if current character is a vowel
        if word[i] in vowels: 
        	indexOfVowel = i
        	break
	
    # add characters after (and including) vowel to newWord
    newWord = ""
    for i in range(indexOfVowel, n):
    	newWord += word[i]

    # get beginning of word before vowel
    for i in range(indexOfVowel):
        newWord = newWord + word[i]
    	
    newWord = newWord + "ay"
    return newWord

print(pigLatin("banana"))