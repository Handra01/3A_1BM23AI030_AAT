def twoStacks(x, a, b):
    sum_a = 0
    count_a = 0
    
    while count_a < len(a) and sum_a + a[count_a] <= x:
        sum_a += a[count_a]
        count_a += 1

    max_count = count_a
    sum_b = 0

    count_b = 0
    while count_b < len(b):
        sum_b += b[count_b]
        count_b += 1

        while sum_a + sum_b > x and count_a > 0:
            count_a -= 1
            sum_a -= a[count_a]

        if sum_a + sum_b <= x:
            max_count = max(max_count, count_a + count_b)

    return max_count


if __name__ == "__main__":
    g = int(input())
    for _ in range(g):
        n, m, x = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(twoStacks(x, a, b))
