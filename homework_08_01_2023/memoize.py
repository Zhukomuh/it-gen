def fibo():
    fibo_line = [1, 1]

    def next(n):
        if len(fibo_line) >= n:
            return fibo_line[n - 1]
        while len(fibo_line) < n:
            fibo_line.append(sum(fibo_line[-2:]))
        return fibo_line[n - 1]

    return next


f = fibo()
print(f(5))
print(f(5))
print(f(3))
