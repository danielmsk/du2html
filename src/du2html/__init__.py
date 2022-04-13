from ._logging import get_logger
from ._options import get_options, print_option
from .main import DU2HTML


def cli():
    opt = get_options()
    print_option(opt)
    opt['log'] = get_logger(silence=False, debug=False, logfile='')
    d2h = DU2HTML(opt)
    d2h.run()
