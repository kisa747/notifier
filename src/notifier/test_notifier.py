#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试
"""

__author__ = 'kevin'
__date__ = '2022/11/18'

import logging

from notifier.balloontip import info as balloontip_info
from notifier.toast_tip import info as toast_info


def test_balloontip():
    _ = balloontip_info('处理完成', 'balloontip')
    logging.info('--> balloontip_info 处理完成！')


def test_toast():
    _ = toast_info('处理完成', '', 1)
    logging.info('--> toast_info 处理完成！')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    test_balloontip()
    test_toast()
