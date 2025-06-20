import definitions._args as ARGS
import definitions._todo as TODO
from  definitions._general import TODAY

def get_arg(args, flag):
    if any([
        isinstance(args.__dict__[flag], list),
        isinstance(args.__dict__[flag], tuple),
        isinstance(args.__dict__[flag], set),
        isinstance(args.__dict__[flag], dict),
    ]):
        return args.__dict__[flag][0]
    else:
        return args.__dict__[flag]