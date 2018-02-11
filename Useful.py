import inspect

def notafunction():
    pass


def call(f, args):
    # Get Function Args
    f_args = inspect.getfullargspec(f).args
    to_pass = []
    # Add to to_pass all the args requested
    for i in f_args:
        to_pass.append(args[i])
    return f(*to_pass)


def default_start(chat, bot):
    pass


def default_help(chat, bot):
    pass
