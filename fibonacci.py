def fibonacci(num):
    if num <= 0:
        return -1
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    print(fibonacci(5))
