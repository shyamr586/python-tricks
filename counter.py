from collections import Counter

word = "Hello World!"                   #can be any iterable like a list also

word_countobj = Counter(word)           #make a counter object

top_letter = word_countobj.most_common(1)   #.most_count helps calculate most common element, in argument 
                                            #enter the number of elements you want to see, for example,
                                            #putting 3 will give top 3 frequent letters in this case.
print (top_letter)

#to get how many times an element occurs:

words = [
    "hello",
    "hi",
    "hello",
    "how",
    "are",
    "are",
    "you",
    "world",
    "?",
    "hello",
]

words_counterobj = Counter(words)
print (words_counterobj["hello"])
print (words_counterobj["hello?"])
print (words_counterobj["are"])
print (words_counterobj["?"])