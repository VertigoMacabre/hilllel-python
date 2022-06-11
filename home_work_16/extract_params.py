def extract_args(args, index):
    try:
        args[index]
    except IndexError:
        return ''
    else:
        return args[index]
