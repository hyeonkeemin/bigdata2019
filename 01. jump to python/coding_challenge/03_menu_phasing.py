def menu_phasing():
    m = int(input('총 건수 : '))
    n = int(input('한 페이지에 필요한 게시물 수 : '))
    result = []
    if m == 0:
        result = 1
    elif m != 0:
        if m % n == 0:
            result = m // n
        elif n % m != 0:
            result = (m // n) + 1
    print(m, n, result)
    return result

menu_phasing()