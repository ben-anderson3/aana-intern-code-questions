# Question 6
# Python-Specific Questions:
# Question: Implement a Python function that takes a string and returns a dictionary where the keys are the unique words in the string, and the values are the frequencies of each word.

# Code solution here
def doc_function(sentence):
    new_sentence = sentence.lower().split()
    output = dict()
    for word in new_sentence:
        if word in output.keys():
            output[word] += 1
        else:
            output[word] = 1
    return output

 #I'm ignoring case