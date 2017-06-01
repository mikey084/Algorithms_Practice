def cumulative_sum(n):
    if n == 0:
        return 0

    else:
        print(n)
        return n + cumulative_sum(n-1)


print(cumulative_sum(5))