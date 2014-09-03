# Author: Francis Bautista
# Date Created: September 3, 2014
import sys
import mapper
import combiner

def main():
    filename = 'input_text.txt'
    word_map = mapper.map(filename)
    word_reduced = combiner.combine(word_map)

    outfile = open('file.txt', 'wb')
    outfile.write(str(word_reduced))

    print "File written successfully in file.txt"
    sys.exit(1)

if __name__ == '__main__':
    main()
