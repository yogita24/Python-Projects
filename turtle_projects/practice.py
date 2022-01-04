#dictionary Comprehension
'''Getting length of each word in sentence'''
sent="Dictionary Comprehension is efficient and neat way of writing code."
d={x:len(x) for x in sent.split(" ")}
print(d)
