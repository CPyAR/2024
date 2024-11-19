#AR 2024
# Ascertain whether all elements in the given sequence are equal.
# assumption integer type
sequence=int(input("Insert a numerical sequence."))
while sequence!=0:
    mul=10
    last=sequence%mul
    sequence//=mul
    if sequence!=0:
        last_shifted=sequence%mul
        if last!=last_shifted:
            print("there is at least one element that is different ")
            break
    else:
        print(" All elements in the given sequence are equal.") 

    

       