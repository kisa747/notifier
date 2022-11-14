#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档
"""
__author__ = 'kevin'
__date__ = '2021/12/28'

import logging
import re
from pathlib import Path

from .core import Media


def _rename_media(img_path: Path, img_creat_date):
    """
    内部方法

    命名规则:
    照片使用拍摄日期，视频转换为东八区时间
    IMG_0001_293.HEIC  -->  2021-11-05_195612.heic
    如果重名后面添加 1 位序列号：
    IMG_0001_293.HEIC  -->  2021-11-05_195612_1.heic
    :param img_path:
    :param img_creat_date:
    :return:
    """
    img_path = img_path if isinstance(img_path, Path) else Path(img_path)
    # img_creat_date = Media(img_path).creat_date
    img_new_stem = img_creat_date.strftime('%Y-%m-%d_%H%M%S')
    suffix = img_path.suffix.lower()  # 使用小写的文件后缀名
    img_new = img_path.with_name(f'{img_new_stem}{suffix}')

    if re.match(r'\d{4}-\d{2}-\d{2}_\d{6}(_\d+)?$', img_path.stem):
        logging.info(f'--> No Change: {img_path.name}')
    else:
        # 有时候照片连拍，多张照片的时间信息一样，需要在后面添加自增序号
        if img_new.exists():
            n = 0
            while True:
                n += 1
                img_new = img_path.with_name(f'{img_new_stem}_{n}{suffix}')
                if not img_new.exists():
                    break
        img_path.rename(img_new)
        logging.info(f'--> Done: {img_path.name} --> {img_new.name}')


def rename_media_dir(media_dir: str | Path, recursive: bool = False):
    media_dir = Path(media_dir) if isinstance(media_dir, str) else media_dir
    if recursive:
        lis = media_dir.rglob('*.*')  # 递归模式获取目录下所有文件
    else:
        lis = media_dir.glob('*.*')  # 非递归模式获取目录下所有文件
    for media in lis:
        if re.match(r'\.jpg|\.heic|\.png|\.nef|\.cr2|\.mov|\.mp4', media.suffix, re.I):
            med = Media(media)
            img_creat_date = med.creat_date
            if img_creat_date:
                _rename_media(media, img_creat_date)
            else:
                raise ValueError('媒体时间信息缺失！')


def _test():
    rename_media_dir(Path(r'E:\test\mediainfo\118APPLE'))
    logging.info('--> 处理完成！')
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    _test()
