#AR 2024
#The number of zeros that a given number has at the end.
# function
def end_zeros(a: int) -> int:
    k=len(str(a))
    zero_count=0
    for l in range(k):
        if a%10==0:
            zero_count+=1
            a=a//10
    return zero_count
# calling the function
evaluate=int(input("Enter a number: "))
print(end_zeros(evaluate))