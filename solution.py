def solution(num):
    if num < 0:
        return 0

    multiples = []
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    return sum(multiples)
