def is_colorful(num):
    num_s = str(num)
    n = len(num_s)
    digit_set = set()

    for start_point in range(n):
        for group_size in range(start_point, n + 1):
            sub = num_s[start_point:group_size]
            if sub:
                prod = get_product(int(sub))
                if prod in digit_set:
                    return False
                else:
                    digit_set.add(prod)
    return True

def get_product(num):
    if num < 10:
        return num

    prod = 1
    while num > 0:
        prod *= num % 10
        num //= 10
    return prod


if __name__ == "__main__":
    print("326 Colorful -", is_colorful(326))
    print("3245 Colorful -", is_colorful(3245))
