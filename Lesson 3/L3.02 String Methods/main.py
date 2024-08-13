# L3.02 String Methods
# REDACTED(I <3 not doxxing myself)
# Write a program that translates english to pig latin by adding "hay" to words that start with a vowel
# and moving the starting consonant to the end of the word and adding ay if the word starts with a consonant

# Get a sentence from the user to translate into pig latin
sentence = input("Please enter a sentence to translate to pig latin:")
sentence = sentence.replace('"', "")
specialChars = "!@#$%^&*(){[}]\\|':;/?>.<,~`1234567890"
for i in range(0,len(specialChars)):
    sentence = sentence.replace(specialChars[i], "")
# Split the sentence at every space, dividing the sentence into an array of words

words = str.split(sentence)

# For every word,
for currentWord in range(0,len(words)):
    # If the first letter of the word is a vowel
    if words[currentWord][0] == 'a' or words[currentWord][0] == 'A':
        # make the word all lowercase
        words[currentWord] = words[currentWord][0].lower()
        # add hay to the end of the word
        words[currentWord] = words[currentWord] + "hay"
    elif words[currentWord][0] == 'e' or words[currentWord][0] == 'E':
        words[currentWord] = words[currentWord][0].lower()
        words[currentWord] = words[currentWord] + "hay"
    elif words[currentWord][0] == 'i' or words[currentWord][0] == 'I':
        words[currentWord] = words[currentWord][0].lower()
        words[currentWord] = words[currentWord] + "hay"
    elif words[currentWord][0] == 'o' or words[currentWord][0] == 'O':
        words[currentWord] = words[currentWord][0].lower()
        words[currentWord] = words[currentWord] + "hay"
    elif words[currentWord][0] == 'u' or words[currentWord][0] == 'U':
        words[currentWord] = words[currentWord][0].lower()
        words[currentWord] = words[currentWord] + "hay"
    # If the first letter of the word is a consonant
    else:
        # Add the consonant to the end of the word
        words[currentWord] = words[currentWord] + words[currentWord][0].lower()
        # Add ay to the end of the word
        words[currentWord] = words[currentWord] + "ay"
        # Remove the consonant from the start of the word
        words[currentWord] = words[currentWord].removeprefix(words[currentWord][0])

# Print all the words seperated by spaces
print(*words, sep=" ")

# Test cases
"""
Please enter a sentence to translate to pig latin: this is a sentence with many words
histay ishay ahay entencesay ithway anymay ordsway
"""
"""
Please enter a sentence to translate to pig latin: mary had a little lamb
arymay adhay ahay ittlelay amblay
"""
"""
Please enter a sentence to translate to pig latin: a beautiful day started with snowfall
ahay eautifulbay ayday tartedsay ithway nowfallsay
"""
"""
Please enter a sentence to translate to pig latin: string manipulation is a fun day for everyone involved                  
tringsay anipulationmay ishay ahay unfay ayday orfay everyonehay involvedhay
"""
"""
Please enter a sentence to translate to pig latin: This IS A SentenCe With Many Words
histay ihay ahay entenCesay ithway anymay ordsway
"""
"""
Please enter a sentence to translate to pig latin: this #s3ntence $!has A *\"sjs Lot 0f $pecial ~characters
histay ntencesay ashay ahay jssay otlay fay ecialpay haracterscay
"""