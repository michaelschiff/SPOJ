import math

def next_pallindrome(num):
    digits = list(int(d) for d in str(num))
    pallindromes = []
    for i in range(len(digits)/2):
        left, right = digits

def digit_at_place(num, i):
    return (num % (i*10)) / i

def num_digits(num):
    return int(math.log10(num))+1

def is_pallindrome(num):
    for i in range(num_digits(num)/2):
        left = digit_at_place(num, 10**i)
        right = digit_at_place(num, 10**(num_digits(num)-i-1))
        if left != right: return False
    return True
    
