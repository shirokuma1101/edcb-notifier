import argparse
import json
import os

from edcbnotifier.engc import ENGC
from edcbnotifier.enutil import ENUtil


def main():

    with open('../config.json', 'r') as f:
        config = json.load(f)

    parser = argparse.ArgumentParser(description='edcb-notifier')
    parser.add_argument('-a', '--PostAddReserve', action='store_true', help='Add Reserve')
    parser.add_argument('-c', '--PostChgReserve', action='store_true', help='Change Reserve')
    parser.add_argument('-n', '--PostNotify', action='store_true', help='Notify')
    parser.add_argument('-e', '--PostRecEnd', action='store_true', help='Recording End')
    parser.add_argument('-s', '--PostRecStart', action='store_true', help='Recording Start')
    args = parser.parse_args()

    macros = ENUtil.getMacro(os.environ)

    if args.PostAddReserve:
        engc = ENGC(config['calendar-id'])
        engc.add_event(macros)


if __name__ == '__main__':
    main()

