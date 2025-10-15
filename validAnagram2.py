from collections import defaultdict
def isAnagram(str):
    # how to solve this problem 
    # how to loops throught a list to check if pairs of words that are anagram
    # i think that we can take it object in the list, first sorting the length and check the pair of it, i mean categorized the length
    # add the different lenght to different list
    # this is not efficient because we cannot have infinite dict if the input growth so i will use the index and nums
    my_dict = {}
    for nums in str:
        my_dict[nums] = len(nums)
    print(my_dict)
    same_value_key = defaultdict(list)
    for keys,values in my_dict.items():
        same_value_key[values].append(keys)
    result = list(same_value_key.values())
    print(result)
    for i in result:
        print(isAnagram_list(i))
    
   
#this method will check and return the things that isAnagram in the list
def isAnagram_list(list_of_string):
    anagrams = defaultdict(list)
    for l in list_of_string:
        key = ''.join(sorted(l))
        anagrams[key].append(l)  
    result = list(anagrams.values())
    return result

print(isAnagram_list(["act","pots","tops","cat","stop","hat"])
)