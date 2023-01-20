from random import randint


def user_func(item):
    return item * 2


def sum_list(data: list, predicate):
    return sum(predicate(item) for item in data)


if __name__ == '__main__':
    num_data = [randint(1, 100) for i in range(20)]
    print(sum_list(num_data, user_func))
