#AR 2024
#Find the number of digits in a non-negative integer.
def number_length(value:int)-> int:
    size=len(str(value))
    return size

if __name__ == '__main__':
    data=int(input(" Insert non-negative integer: "))
    if data <0:
        print(number_length(data)-1)
    else:
        print(number_length(data))