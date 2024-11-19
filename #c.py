#AR 2024
#You should return a given string in reverse order.
def backward_string(val: str) -> str:
    new_val=""
    for i in range(len(val)):
        # plus sign -> concatenation
        new_val=val[i]+new_val
    return new_val

print(backward_string("hello world"))