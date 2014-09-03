import math

def next_pallindrome(num):
    fringe = [num]
    pallindromes = []

    # iterate through fringe

    for i in range(num_digits(num)/2):
        left_place = 10**i
        left = digit_at_place(num, left_place)

        right_place = 10**(num_digits(num)-i-1)
        right = digit_at_place(num, right_place) 

        smaller, larger = math.min(left, right), math.max(left, right)

        for j in range(smaller, larger+1):
            left_diff = (j - left) * left_place
            right_diff = (j - right) * right_place
            new_num = num
            new_num += left_diff
            new_num += right_diff
            if is_pallindrome(new_num):
                pallindromes.appned(new_num)
            else:
                fringe.append(new_num)



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


