# A3.5 List of Languages
# REDACTED(I <3 not doxxing myself)
# Read from a file called languages.txt and print every language listed in that file and write to a file called
# no_commas.txt with the list of language names with one on each line

# Open the languages text file with read permissions
langFile = open("languages.txt", 'r')
# Read all the text from the languages text file and place it into a string
langFileText = langFile.read()
# Close the languages text file
langFile.close()
# Make an array of strings containing the name of each language by splitting the string at every comma
languages = langFileText.split(",")
# Print the languages array without brackets and each item seperated by a new line
print(*languages, sep="\n", end="")
# Open the no_commas.txt file, creating it if necessary
noCommasFile = open("no_commas.txt", 'w')
# For every language in the array except for the last one
for i in range(0,len(languages) - 1):
    # Write the name of the language to the array and add a newline in between each language name
    noCommasFile.write(languages[i] + "\n")
# Wrie the name of the last language without a newline
noCommasFile.write(languages[len(languages) - 1])
# Close the file
noCommasFile.close()

# Test cases
# languages.txt:
# ActionScript,Ada,Algol,Alice,APL,AppleScript,Arduino,Assembly,Awk,Bash,(Visual) Basic,Bourne Shell,C,C Shell,C#,C++,Clojure,COBOL,ColdFusion,Common Lisp,Delphi/Object Pascal,Erlang,Forth,Fortran,Haskell,HyperTalk,Java,JavaScript,Lisp,Logo,Lua,Modula-3,Oberon,OCaml,Pascal,Perl,PHP,Processing,Prolog,Python,R,Ruby,Scala,Scheme,Scratch,Smalltalk,SPSS,Tcl,Turing,Visual Basic .NET
# program output:
"""
ActionScript
Ada
Algol
Alice
APL
AppleScript
Arduino
Assembly
Awk
Bash
(Visual) Basic
Bourne Shell
C
C Shell
C#
C++
Clojure
COBOL
ColdFusion
Common Lisp
Delphi/Object Pascal
Erlang
Forth
Fortran
Haskell
HyperTalk
Java
JavaScript
Lisp
Logo
Lua
Modula-3
Oberon
OCaml
Pascal
Perl
PHP
Processing
Prolog
Python
R
Ruby
Scala
Scheme
Scratch
Smalltalk
SPSS
Tcl
Turing
Visual Basic .NET
"""
# no_commas.txt:
"""
ActionScript
Ada
Algol
Alice
APL
AppleScript
Arduino
Assembly
Awk
Bash
(Visual) Basic
Bourne Shell
C
C Shell
C#
C++
Clojure
COBOL
ColdFusion
Common Lisp
Delphi/Object Pascal
Erlang
Forth
Fortran
Haskell
HyperTalk
Java
JavaScript
Lisp
Logo
Lua
Modula-3
Oberon
OCaml
Pascal
Perl
PHP
Processing
Prolog
Python
R
Ruby
Scala
Scheme
Scratch
Smalltalk
SPSS
Tcl
Turing
Visual Basic .NET
"""
# languages.txt: A,beautiful,morning,was,spent,writing,these,test,cases
# program output:
"""
A
beautiful
morning
was
spent
writing
these
test
cases
"""
# no_commas.txt: 
"""
A
beautiful
morning
was
spent
writing
these
test
cases
"""
# languages.txt: 1,2,3,4,5,6,7,8,9,10,15,20,25,100
# program output:
"""
1
2
3
4
5
6
7
8
9
10
15
20
25
100
"""
# no_commas.txt: 
"""
1
2
3
4
5
6
7
8
9
10
15
20
25
100
"""
# languages.txt: !,@,354,a piece of text,.-.,(@^@)
# program output:
"""
!
@
354
a piece of text
.-.
(@^@)
"""
# no_commas.txt:
"""
!
@
354
a piece of text
.-.
(@^@)
"""
# languages.txt: 123,,35,abcdefgh
# program output:
"""
123

35
abcdefgh
"""
# no_commas.txt
"""
123

35
abcdefgh
"""