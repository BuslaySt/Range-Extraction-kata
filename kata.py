# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

def solution(args):
    result = str(args[0])
    last = args[0]
    prev = args[0]
    for number in args[1:]:
        if number-prev > 1:
            if last == prev:
                result += ','+str(number)
            else:
                if prev - last > 1:
                    result += '-'+str(prev)+','+str(number)
                else:
                    result += ','+str(prev)+','+str(number)
            last = number
        prev = number
    if prev-last == 1:
        result += ','+str(args[-1])
    else:
        result += '-'+str(args[-1])

    return result

exam = solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
answer = "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
print(exam)


exam2 = solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
answer2 = "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
print(exam2)
