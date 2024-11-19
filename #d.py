#AR 2024
# Determine the most frequently occurring string in the sequence
#far-fetched solution
def create_set(data:str)-> set:
    return set(data)
string_sequence="Hello"
set_sequence=create_set(string_sequence)
copy_sequence=set_sequence.copy()
count_list=[]
while bool(set_sequence):
    count=0
    evaluate_char=set_sequence.pop()
    for i in string_sequence:
        if i==evaluate_char:
            count+=1
        else:
            count+=0
    else:count_list.append(count)
print (count_list)
control=count_list.index((max(count_list)))
value=copy_sequence
print(f" In the {value} set, look at the {control} element to see the most frequent character in the string (start count 0).")

