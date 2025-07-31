#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notifier使用示例
"""

__author__ = "kevin"
__date__ = "2024/7/5"


import notifier


def main() -> None:
    notifier.info("这是一条 notifier 消息测试", "标题", 1)


if __name__ == "__main__":
    main()
