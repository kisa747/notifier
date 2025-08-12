#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 Windows.UI.Notifications 接口实现通知消息
"""

__author__ = 'kevin'
__date__ = '2022/11/18'

import logging
import platform
import subprocess
from pathlib import Path
from typing import Literal


def _toast(
    text: str,
    title: str = '',
    icon: Literal['Info', 'Warning', 'Error'] = 'Info',
    expiration_minutes: int = 24 * 60,
) -> int | None:
    """

    :param text: 内容
    :param title: 标题
    :param icon: 图标（默认为信息）
    :param expiration_minutes: 过期时间（默认24小时过期）
    :return: returncode
    """
    title = title or icon  # 如果未设置 title，就使用 icon 的名字
    ps_file = f'{Path(__file__).with_name("_toast_tip.ps1")}'
    if platform.system() == 'Windows':
        r = subprocess.run(
            [
                'powershell',
                '.',  # Dot-Sourcing 方法
                ps_file,
                ';',
                'New-DotNetToast',
                f"'{text}'",  # 避免传递的参数中包含空格，内层使用单引号
                f"'{title}'",
                icon,
                str(expiration_minutes),
            ],
            # shell=True,
        )
        return r.returncode
    else:
        logging.warning(f'{platform.system()} 系统下无法使用 Notifier')
        return None


def info(text: str, title: str = '', expiration_minutes: int = 24 * 60) -> int | None:
    return _toast(text, title, 'Info', expiration_minutes)


def warning(text: str, title: str = '', expiration_minutes: int = 24 * 60) -> int | None:
    return _toast(text, title, 'Warning', expiration_minutes)


def error(text: str, title: str = '', expiration_minutes: int = 24 * 60) -> int | None:
    return _toast(text, title, 'Error', expiration_minutes)


def _test():
    info('测试 ddd', 'tit le', 2)
    logging.info('处理完成！')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    _test()
