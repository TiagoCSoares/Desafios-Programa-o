from typing import List

def d2i(y, m, d, h, M):
    k = (y - 2013) * 365 * 24 * 60
    md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y == 2016:
        md[2] += 1
    for i in range(1, 13):
        md[i] += md[i - 1]
    d += md[m - 1]
    return k + d * 24 * 60 + h * 60 + M

def solve(t, logs):
    for i in range(t):
        b, c = logs[i][0], logs[i][1]
        in_arr = []
        out_arr = []
        for j in range(b):
            y1, m1, d1, h1, M1, y2, m2, d2, h2, M2 = logs[i][2][j]
            in_arr.append(d2i(y1, m1, d1, h1, M1))
            out_arr.append(d2i(y2, m2, d2, h2, M2))
        in_arr.sort()
        out_arr.sort()
        i = 0
        j = 0
        k = 0
        m = 0
        while i < b:
            if out_arr[j] + c <= in_arr[i]:
                j += 1
                k -= 1
            else:
                i += 1
                k += 1
                m = max(m, k)
        print(m)

if __name__ == '__main__':
    t = int(input().strip())
    logs = []
    for i in range(t):
        b, c = map(int, input().strip().split())
        logs_ = []
        for j in range(b):
            log = input().strip().split()
            y1, m1, d1 = map(int, log[1].split('-'))
            h1, M1 = map(int, log[2].split(':'))
            y2, m2, d2 = map(int, log[3].split('-'))
            h2, M2 = map(int, log[4].split(':'))
            logs_.append((y1, m1, d1, h1, M1, y2, m2, d2, h2, M2))
        logs.append((b, c, logs_))
    solve(t, logs)
