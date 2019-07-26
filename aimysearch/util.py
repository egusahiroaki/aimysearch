# pylint: disable=C0111,C0103


def n_gram(target, n):
    return [{"text": target[index:index + n], "index": index, "length": n}
            for index in range(len(target) - n + 1)]
