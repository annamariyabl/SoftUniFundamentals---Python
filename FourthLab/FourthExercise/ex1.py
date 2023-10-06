a = int(input())
b = int(input())
c = int(input())

def min_value (a, b, c):
    m_value = a
    if m_value > b:
        m_value = b
    if m_value > c:
        m_value = c
    return m_value

print(min_value(a, b, c))