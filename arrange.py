import sys
import subprocess
from shutil import copy2
# This function will copy the text to Clipboard
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
# This function read and stores the name in text file
con = "Filename.txt"#File should be in the same folder where this pyhton file is.
def storing(string):
    print string
    result = {}
    # Create backup file before execution
    copy2(con,'{}backup.txt'.format(con))
    # Opens the text file and it automatically closes the file after the block ends
    with open(con,'r') as f:
        for line in f:
            value = line.strip().split()
            result[value[0]] = int(value[1])
    # Get the input string and splits with white spaces and strips off "\n"
    input_words = string.strip().split()
    # It checks wether the word is in text file or not, if word is there it updates
    # it count and if not add the word to the text file
    for word in input_words:
        try:
            result[word]+=1
        except KeyError:
            result[word]=0
    #It opens the text file and add the word to it
    with open(con,'w') as f:
        for k,v in result.items():
            f.write('{} {}\n'.format(k,str(v)))

x=""
final =""
while x != 1:
    
    my_str = raw_input()
    my_str = my_str.title()
    # Calls the storing function
    storing(my_str)
    words = my_str.split()
    #It sorts the name into alphabetical order
    words.sort()
    result={} # Dictionary is declared here
    # It opens the file 
    with open(con,'r') as f:
        for line in f:
            value = line.strip().split()
            result[value[0]] = int(value[1])
    #To read the values of occurance
    for word in words:
        for name, occur in result.items():
            if name == word:
                if occur == 0:
                    final = final + word
                else:
                    final = final + word+"{}".format(occur)
                
    print final
    copy2clip(final)
    final = ""
    print("_________")
    x=len(my_str)
