
# Solution


from collections import defaultdict



def sm(n):
    return n * (n + 1) // 2


def solve():
    n = int(input())

    cnt = defaultdict(int)

    arr = list(map(int, input().split()))

    for a in arr:
        cnt[a] += 1

    ans = 0

    for value in cnt.values():
        ans += sm(value - 1)

    print(ans)


def solve2():
    n = int(input())

    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if a[j] == a[i]:
                ans += 1

    print(ans)


solve2()
