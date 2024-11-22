import square
import circle

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'circle': 1,
    'square': 1
}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}. Available figures: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}. Available functions: {funcs}")
    if len(size) != sizes[fig]:
        raise ValueError(f"Invalid size for {fig}. Expected {sizes[fig]} arguments.")

    module = globals()[fig]
    method = getattr(module, func)
    result = method(*size)

    return round(result, 2) if isinstance(result, float) else result


if __name__ == "__main__":
    fig = ''
    func = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes[fig]:
        size = list(
            map(
                int,
                input(
                    f"Input figure sizes separated by space, {sizes[fig]} for {fig}\n"
                ).split(' ')
            )
        )

    result = calc(fig, func, size)




