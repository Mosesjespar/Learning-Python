# Write a Python program to find the list of words that are longer than n from a given list of words
def str_count(n, words):
    result = []
    for word in words.split(' '):
        if len(word) > n:
            result.append(word)
    return result