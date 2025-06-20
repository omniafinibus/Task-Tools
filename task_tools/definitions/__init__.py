import definitions._args as ARGS
import definitions._todo as TODO
from  definitions._general import TODAY

def get_arg(args, flag):
    return args.__dict__[flag][0]