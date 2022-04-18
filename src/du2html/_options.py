
import argparse
import sys
import os
from . import util
import textwrap


def loading_config(opt):
    for line in open(opt['conf']):
        line = line.strip()
        if len(line) > 0 and line[0] != "#":
            arr = line.split("=")
            k1 = arr[0].strip().lower()
            v1 = arr[1].strip()
            if len(k1) > 0:
                opt[k1] = v1
    return opt
    

def print_option(opt):
    global NOPRINTOPTLIST
    # print("=======option=======")
    # for k1 in sorted(opt.keys()):
    #     if k1 not in NOPRINTOPTLIST:
    #         if k1 == "poslist" and len(opt[k1]) >= 4:
    #             print('-' + k1 + " : " + str(len(opt[k1])) + " variants")
    #         else:
    #             print('-' + k1 + " : " + str(opt[k1]))
    # print("====================")
    pass


def convert_valuetype(typestr):
    rsttype = None
    if typestr is not None:
        if typestr == "int":
            rsttype = int
        if typestr == "float":
            rsttype = float
    return rsttype


def get_options():
    global OPT
    # OPT = util.load_json(util.getDataPath('conf.json'))

    parser = argparse.ArgumentParser(usage='%(prog)s <sub-command> [options]',
                                    description='%(prog)s ver' + OPT['VERSION'] + " (" + OPT['VERSION_DATE'] + ")" + ': convert du result to html')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ver' + OPT['VERSION'] + " (" + OPT['VERSION_DATE'] + ")")

    for a1 in OPT['options']:
        # valuetype = convert_valuetype(a1['type'])
        valuetype = a1['type']
        if a1['action'] is not None:
            parser.add_argument('-' + a1['param_a'], '--' + a1['param'], default=a1['default'], help=a1['help'], action=a1['action'])
        else:
            parser.add_argument('-' + a1['param_a'], '--' + a1['param'], default=a1['default'],
                                help=textwrap.dedent(a1['help']), nargs=a1['nargs'], type=valuetype)

    # parser.add_argument('-silence', dest='silence', action="store_true", default=False, help='don\'t print any log.')

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1][0] != '-'):
        sys.argv.append('-h')
    opt = vars(parser.parse_args())

    if 'conf' in opt.keys() and opt['conf'] is not None and util.is_exist(opt['conf']):
        opt = loading_config(opt)

    opt['cmd'] = " ".join(sys.argv)
    

    return opt


### OPTION ####
OPT = {
  "TITLE": "du2html",
  "VERSION": "0.0.6",
  "VERSION_DATE": "2022-04-18",
  "PROG": "du2html",
  "options": [
    { "param_a": "i", "param": "in", "default": None, "nargs": None, "action": None, "choices": None, "type": None, "help": "input du result file" },
    { "param_a": "t", "param": "totalsize", "default": None, "nargs": None, "action": None, "choices": None, "type": None, "help": "total hard disk size (ex: 32t, 100G, 200g)" },
    { "param_a": "o", "param": "out", "default": "", "nargs": None, "action": None, "choices": None, "type": None, "help": "output html file" },
    { "param_a": "n", "param": "innerpath", "default": False, "nargs": None, "action": "store_true", "choices": None, "type": None, "help": "relative path for css and js" },
    # { "param_a": "p", "param": "path", "default": None, "nargs": None, "action": None, "choices": None, "type": None, "help": "path for input files" },
  ]
}
