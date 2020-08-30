def gen_next(s2):
    k = -1
    n = len(s2)
    j = 0
    nextArr = [0] * n
    nextArr[0] = -1  # next数组初始值为-1
    while j < n - 1:
        if k == -1 or s2[k] == s2[j]:
            k += 1
            j += 1
            nextArr[j] = k  # 如果相等 则next[j+1] = k
        else:
            k = nextArr[k]  # 如果不等，则将next[k]的值给k
        print(k, s2[k], j, s2[j], nextArr)
    return nextArr


def match(s1, s2, next_list):
    ans = -1
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] == s2[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next_list[j]
        if j == len(s2):
            ans = i - len(s2)
            break
    return ans


if __name__ == '__main__':
    s1 = 'ababababac'
    s2 = 'abcabea'
    next_list = gen_next(s2)
    print(next_list)
    print(match(s1, s2, next_list))
