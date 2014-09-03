Map Reduce Implementation in Python
===
### To Execute:
** Just go to the file directory root, open in terminal, and run `python master.py`

### Introduction on what each file is for:

**Master:**
* handles all I/O to and from :file_folder: file
* creates mapper and combiner classes for MapReduce Usage

**Mapper:**
* creates a list of tokenized words from an input file and stores these in an array with the assumption that its value is one
* DISCLAIMER: I tried using a dictionary here, but Python dictionaries require unique Keys. As such, the replicate words were being discounted in the dictionary initially in the map stage--hence the usage of an array

**Combiner/Reducer:**
* the combiner module adds the words from the array into a dictionary as a key and adds a value of 1
* if the word already exists as a key, then the value is (if following strict MapReduce theory) appended by another element of 1
* however, due to difficulty in manipulating arrays as a value for the key in the Combine step dictionary, I merged the combine step with the reduce step in the counting of the elements of the supposed array of 1s in the value of each key
