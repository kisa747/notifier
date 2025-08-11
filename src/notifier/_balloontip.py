#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 System.Windows.Forms.NotifyIcon 接口实现通知消息
"""

__author__ = 'kevin'
__date__ = '2022/11/18'

import subprocess
from pathlib import Path
from typing import Literal


def _balloontip(
    text: str,
    title: str = 'Information',
    icon: Literal['None', 'Info', 'Warning', 'Error'] = 'Info',
) -> int:
    ps_file = f'{Path(__file__).with_name("_balloontip.ps1")}'
    r = subprocess.run(
        [
            'powershell',
            '-ExecutionPolicy',
            'RemoteSigned',
            '-File',
            ps_file,
            text,
            title,
            icon,
        ],
        shell=True,
    )
    return r.returncode


def info(text: str, title: str = 'Information') -> int:
    return _balloontip(text, title, 'Info')


def warning(text: str, title: str = 'Information') -> int:
    return _balloontip(text, title, 'Warning')


def error(text: str, title: str = 'Information') -> int:
    return _balloontip(text, title, 'Error')
