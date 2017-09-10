# def is_even(i):
#     """ hey """
#     print("hi")
#     return i%2 ==0
# is_even(4)

# def f(x):
#     x = x+1
#     print("value f is ", x)
#     return x
# x=3;
# z=f(x)

# def f(y):
#     x = 1
#     print("when f(5) is executed the result is at line 17",x)

# x = 5
# f(x)
# print("separately executed print at line 21 ",x)

# def g(y):
#     print("at line 24",x)
#     print("at line 25",x+1)

# x = 5
# g(x)
# print("at line 29",x)


# def h(y):
#     x = x+1

# x = 5
# h(x)
# print("at line 37",x)

# def print_Name(firstName, lastName, reverse = False):
#     if reverse:
#         print(lastName+ '' +firstName)
#     else :
#         print(firstName + '' + lastName)
# print_Name('happy', 'shandilya')
# print_Name('aditya', 'pandey', True)


# create a dictionary

def lyrics_to_frequencies(lyrics):
    myDict = {}  # created an empty dictionary
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


lyrics = ["You", "you", "see", "me", "you", "see", "you", "see"]
coldPlay = lyrics_to_frequencies(lyrics)


# using the dictionary
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


#
def word_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])  # remove word from the dictionary
        else:
            done = True
    return result


print(word_often(coldPlay, 2))


def test():
    print("hello")
