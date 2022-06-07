#  Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of strings.
def get_str_count(mylist):
    count = 0
    for word in mylist:
        if len(word)>1 and word[0] == word[-1]:
            count +=1
    return count


