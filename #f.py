#AR 2024
def count_digits(text: str) -> int:
    l_count=0
    for letters in text:
        if letters in ["0","1","2","3","4","5","6", "7", "8", "9"]:
            l_count+=1
    return l_count

evaluate=input("Enter the phrase: ")
print(count_digits(evaluate))