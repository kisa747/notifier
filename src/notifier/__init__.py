#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 windows 原生的 System.Windows.Forms.NotifyIcon 对象，创建通知消息。
"""

__author__ = 'kevin'
__date__ = '2022/11/18'

from .toast_tip import error, info, warning

__all__ = ('info', 'warning', 'error')
