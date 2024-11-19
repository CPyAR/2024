#AR 2024
# collections - container datatypes
#https://docs.python.org/3/library/collections.html
#counter -A Counter is a dict subclass for counting hashable objects
from collections import Counter
string_sequence="Hello"
# creates a counter object
count_obj=Counter(string_sequence)
print(count_obj)
#most_common([n]) return a list of the n most common
# retrieves the first tuple from that list
most_common, occurences=count_obj.most_common(1)[0]
print(f" The most common char is {most_common} , with {occurences} events.")
