#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档
"""
__author__ = 'kevin'
__date__ = '2022/10/31'

import datetime
import json
import logging
from pathlib import Path

from pymediainfo import MediaInfo


class Media:
    """
    照片（包括RAW相机文件）、视频文件的对象，使用 MediaInfo 工具获取媒体的信息。
    将这些信息封装成一个可以方便使用的对象。
    """

    def __init__(self, media_path: Path):
        self._media_path = (
            media_path if isinstance(media_path, Path) else Path(media_path)
        )
        self.media_info_json = self._get_mediainfo_json()
        self.format = self.media_info_json.get('Format')

    def _get_mediainfo_json(self) -> dict:
        media_info = MediaInfo.parse(self._media_path, output="JSON")
        media_info_dict = json.loads(media_info)['media']["track"][0]
        return media_info_dict

    @property
    def creat_date(self) -> datetime.datetime:
        # '2021-12-26 20:09:14.000'
        c_date_str = self.media_info_json['File_Modified_Date_Local']
        # c_date = datetime.datetime.strptime(c_date_str, '%Y-%m-%d %H:%M:%S.%f')
        c_date = datetime.datetime.fromisoformat(c_date_str)
        return c_date

    @property
    def creat_date_utc(self) -> datetime.datetime:
        # c_date_str_orig='UTC 2021-12-26 12:09:14.000'
        # ISO的标准应该是：'2021-12-26 12:09:14.000+00:00'
        # Python3.11支持 '2021-12-26T12:09:14.000Z'
        c_date_str_orig = self.media_info_json['File_Modified_Date']
        # c_date_str: '2021-12-26 12:09:14.000'
        _, c_date_str = c_date_str_orig.split(' ', 1)
        c_date = datetime.datetime.fromisoformat(c_date_str)
        c_date_utc = c_date.replace(tzinfo=datetime.timezone.utc)  # 强制设置时区为UTC
        # 也可以使用以下方法直接生成带时区信息的datetime对象
        # c_date_str = ''.join([c_date_str_orig.split(' ', 1)[1], '+00:00'])
        # c_date = datetime.datetime.fromisoformat(c_date_str)
        return c_date_utc

    @property
    def media_tpye(self):
        """
        媒体类型 video'或'image
        :return: ['video'|'image']
        """
        m_tpye_str = self.media_info_json.get('InternetMediaType')
        m_tpye = m_tpye_str.split('/')[0]
        return m_tpye
