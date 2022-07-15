def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = num * factorial(num - 1)
    print(result)
    return result


print(factorial(10))