


def flatten(x):
    if isinstance(x, tuple | list):
        for a in x:
            yield from flatten(a)
    else:
        yield x