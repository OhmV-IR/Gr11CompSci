# L3.03 File Input and Output
# REDACTED(I <3 not doxxing myself)
# Asks the user about the morst important thing in their day, and appends it to the end of a file called
# diary.txt and then opens and prints everything inside of diary.txt

# Set the path / file location of the diary text file
diaryPath = "diary.txt"
# Get a string from the user as a new string to add to the diary text file
newEntry = input("What is the most important thing that happened today:")

# Open the diary text file with append permissions(move to the end of the file and create it if it does not exist)
diaryFile = open(diaryPath, 'a')
# Write the user's entry to the file with a newline so it is less cluttered
diaryFile.write(newEntry + "\n")
# Close the file
diaryFile.close()
# Open the file with read permissions, starting at the start of the file
diaryFile = open(diaryPath, 'r')
# Take all the text from the diary text file and store it in the fullDiary variable
fullDiary = diaryFile.read()
# Close the diary file, since we have read the text and saved it in the fullDiary variable, we no longer need it
diaryFile.close()
# Print the full diary, starting with some whitespace seperating the previous program inputs
print("\n" + fullDiary)

# Test cases
"""

What is the most important thing that happened today? this is a first testing sentence

this is a first testing sentence

"""
"""
What is the most important thing that happened today? this is a second testing sentence

this is a first testing sentence
this is a second testing sentence

"""
"""
What is the most important thing that happened today? this program stores all the previous inputs in a text file for future read
ing

this is a first testing sentence
this is a second testing sentence
this program stores all the previous inputs in a text file for future reading

"""
"""
What is the most important thing that happened today? this is such a great program :), I can even add capitals and other special
 characters like these -> &!@(#\mnnO(JU:(*732

this is a first testing sentence
this is a second testing sentence
this program stores all the previous inputs in a text file for future reading
this is such a great program :), I can even add capitals and other special characters like these -> &!@(#\mnnO(JU:(*732

"""