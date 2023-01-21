funcs_ref = []


def deco_reference(func):
    """Adds references to the function that was called
    by this decorator in list(funcs_ref)"""
    funcs_ref.append(func)
    return func


@deco_reference
def add(x, y):
    return x + y


@deco_reference
def div(x, y):
    return x / y


if __name__ == '__main__':
    div(5, 6)
    add(6, 5)
    print(funcs_ref)
