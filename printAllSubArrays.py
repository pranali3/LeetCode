def print_sub_arrays(arr):
    n = len(arr)
    subarr = []

    for start_point in range(n):
        for grps in range(start_point, n + 1):
            print(f"start {start_point} grps {grps}")
            l = arr[start_point:grps]
            if l:
                subarr.append(l)
            print()
    print(subarr)
    print(len(subarr))

    # res = left = 0
    # for right in range(len(arr)):
    #     res += right - left + 1
    # print(res)
    # return res


if __name__ == "__main__":
    arr_a = [1, 2, 3, 4, 5]
    print_sub_arrays(arr_a)
