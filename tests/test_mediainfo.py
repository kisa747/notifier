#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试单元
"""
__author__ = 'kevin'
__date__ = '2022/10/31'

import logging
import unittest
from datetime import datetime
from pathlib import Path

from mediainfo.core import Media


class TestMediainfo(unittest.TestCase):
    def setUp(self):
        path = Path(r'E:\test\mediainfo\1.mov')
        self.m = Media(path)

    def test_creat_date(self):
        test_value = self.m.creat_date
        value = datetime.fromisoformat('2021-12-26 20:09:14')
        self.assertEqual(test_value, value)

    def test_creat_date_utc(self):
        test_value = self.m.creat_date_utc
        value = datetime.fromisoformat('2021-12-26 20:09:14+08:00')
        self.assertEqual(test_value, value)

    def test_media_tpye(self):
        test_value = self.m.media_tpye
        value = 'video'
        self.assertEqual(test_value, value)

    def tearDown(self):
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    unittest.main()
