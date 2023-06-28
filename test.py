class F:
    # Implementation Omitted
    pass

class G(F):
    # Implementation Omitted
    pass

class H(F):
    # Implementation Omitted
    pass

if __name__ == '__main__':
    f = F()
    g = G()
    h = H()

print(isinstance(h, F))
print(type(f))
print(type(g))