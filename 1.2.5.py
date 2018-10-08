"""1.2.5
"""
def factor(n):
    if n == 0 or n == 1:
        return(1)
    else:
        for each in range(1, n):
            n *= each
        return(n)

if __name__ == '__main__':
    print(factor(4))
