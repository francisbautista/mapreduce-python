# Author: Francis Bautista
# Date Created: September 3, 2014

# map takes in raw-text and parses them by isolating each word
# and storing these in an array
def map (filename):
    input_file = open(filename, 'r')
    word_arr = []
    for line in input_file:
        clean_line = lineSanitize(line)
        for word in clean_line.split():
            word = word.lower()
            word_arr.append(word)
    input_file.close()
    return word_arr
    print word_arr


def lineSanitize (line):
    tempLine = line
    garbage_string = "123456:;7890(){}[]!$%*&=:?,.+-\\\/\"\"'"
    for i in range(0, len(garbage_string)):
        tempLine = tempLine.replace(garbage_string[i],'')
        tempLine = tempLine.replace('<b>','')
        tempLine = tempLine.replace('</b>','')
        tempLine = tempLine.replace('<i>','')
        tempLine = tempLine.replace('</i>','')
        tempLine = tempLine.replace('<pd>','')
        tempLine = tempLine.replace('</pd>','')
        tempLine = tempLine.replace('<u>','')
        tempLine = tempLine.replace('</u>','')
        tempLine = tempLine.replace('<>','')
        tempLine = tempLine.replace('<','')
        tempLine = tempLine.replace('>','')
    return tempLine
