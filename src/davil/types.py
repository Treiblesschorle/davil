def is_list(thing):
    return isinstance(thing, list)


def is_tuple(thing):
    return isinstance(thing, tuple)


def is_iterable(thing):
    try:
        thing_iterator = iter(thing)
        return True
    except TypeError:
        return False
