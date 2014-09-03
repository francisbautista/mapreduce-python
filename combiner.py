# Author: Francis Bautista
# Date Created: September 3, 2014

# This module combines the reduce and combine step in combine
# in one by automatically adding the value of the key if the key already
# exists in the dictionary
def combine(arr):
    combine_dict = {}
    val = 1
    for key in arr: # add another element to value list if word already exists 
        if key in combine_dict:
            val = combine_dict[key]
            combine_dict[key] = val + 1
        else: # copy arr[key] to combine_dict if new instance of word
            combine_dict[key] = 1
    return combine_dict
