#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows 系统下发送 toast 消息
"""

__author__ = 'kevin'
__date__ = '2022/12/10'

import argparse
import logging
import sys

from notifier._toast_tip import _toast


def main() -> None:
    # action='store'，默认为 store，所以可以省略；type=str，默认为字符串，也可以省略。
    arg_parser = argparse.ArgumentParser(prog=__package__, description=__doc__)
    arg_parser.add_argument('-i', '--info', metavar='通知消息', help='发送info通知')
    arg_parser.add_argument('-w', '--warning', metavar='警告消息', help='发送warning通知')
    arg_parser.add_argument('-e', '--error', metavar='错误消息', help='发送error通知')
    arg_parser.add_argument(
        '-t',
        '--expirationminutes',
        metavar='消息过期分钟数值',
        help='设置消息过期时间',
        type=int,
        default=60 * 24,
    )
    args = arg_parser.parse_args(args=None if len(sys.argv) > 1 else ['--help'])

    if args.info:  # 发送info通知
        notifier_type = 'Info'
        text = args.info
    elif args.warning:  # 发送warning通知
        notifier_type = 'Warning'
        text = args.warning
    elif args.error:  # 发送error通知
        notifier_type = 'Error'
        text = args.error
    else:
        notifier_type = 'Info'
        text = ''

    if text:
        expiration_minutes = args.expirationminutes if args.expirationminutes else 60 * 24
        _toast(text, icon=notifier_type, expiration_minutes=expiration_minutes)  # type: ignore


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    main()
