def combination(n, k):
    if k < 0 or n <= 0 or k > n:
        print('error')
    elif k == 0:
        print('1x^0')
    else:
        X = 1
        Y = 1
        for i in range(n - k + 1, n + 1):
            X = X * i
        for j in range(1, k + 1):
            Y = Y * j
        print('%dx^%d' % (X/Y, k))

if __name__ == '__main__':
    n = 4
    for i in range(n+1):
        combination(n, i)