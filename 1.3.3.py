def square_root_2():
    c = 10.0
    i = 0
    m_max = c
    m_min = 0.0
    g = (m_min + m_max) / 2
    while abs(g * g - c) > 0.01:
        print(g)
        if g * g < c:
            m_min = g
        else:
            m_max = g
        i += 1
        g = (m_min + m_max) / 2
        print('%d:%.3f' % (i, g))

square_root_2()
