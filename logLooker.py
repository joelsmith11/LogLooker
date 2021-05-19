####################################################################
#
# @author Joel Smith
# date May 7 2021
#
# This script will look for test words in a text file and output the
# 5 lines before and after a line where the test word is found.
#
####################################################################

# argv.py
import sys

# This is how many arguments are required. We'll also use this
# to find out how many test words we have
REQD_ARGS = 3

# This function will print the lines leading up to and 
# after the line with the target word in it
# @param lines Every line from the input file
# @param idx The line number where the test word is 
#        located
def print_lines( lines, idx ):
    begIdx = 0
    endIdx = 0

    # If our target word was found in a line before 5,
    # set out beginning index to 0
    if( idx >= 5 ):
        begIdx = idx - 5
    
    # If our target word was found in a line that's less than 
    # 5 lines away from the end, set the endIdx to the last line
    if( (idx + 6) >= len(lines)):
        endIdx = len(lines)
    else:
        endIdx = idx + 6

    # Print each line from beginning index to the end
    while begIdx != endIdx:
        # Print the line number and line
        print(f"#{begIdx} {lines[begIdx]}")
        begIdx += 1

    print("\n")

# Parse the command line args
# If we don't have at least 4 args (program name, input file, and a test word)
# we'll exit with the error message
if len( sys.argv ) < REQD_ARGS:
    sys.exit("Invalid number of command line arguments.\nExpected format: logLooker input.txt testWord ...")

# If .txt isn't in the input file, exit
if ".txt" not in sys.argv[1]:
    sys.exit("Invalid input file. Expected a .txt file")

# Get the test words
testWords = []
argIdx = REQD_ARGS - 1
while argIdx != len(sys.argv):
    # Append the words to look for to our list of test words
    testWords.append(sys.argv[argIdx])
    argIdx += 1

# Read all the lines in from the file and strip the newline off
with open(sys.argv[1]) as f:
    lines = [line.rstrip() for line in f]
    f.close()

# We'll use this to know what index to pass to the print_lines function
linesTested = 0    

# Test each line for the test word. If it contains it,
# call the print_lines function
while linesTested != len(lines):
    
    # Get the line at the next index
    line = lines[linesTested]

    # For each of our test words, check to see if it's
    # in our line
    for words in testWords:
        
        # If it is, write to the file
        # Use lower to make sure we catch every instance
        if words.lower() in line.lower():
            #outFile.write("Word " + words + " on line " + str(linesTested) + "\n")
            print(f"Word {words} on line {linesTested}\n")
            print_lines( lines, linesTested )

    linesTested += 1
