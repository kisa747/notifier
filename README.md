# Notifier 说明文档

[![Documentation Status](https://readthedocs.org/projects/notifier-docs/badge/?version=latest)](https://notifier-docs.readthedocs.io/?badge=latest)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

官方文档：<https://notifier-docs.readthedocs.io/>

## Quik Start

### 1、安装

```sh
# 使用pip安装最新版本
python -m pip install git+https://github.com/kisa747/notifier
# 虚拟环境推荐使用 uv 安装
uv add git+https://github.com/kisa747/notifier@
```

### 2、命令行使用

```sh
# 弹出一条消息
notifier -i "这是一条信息"
notifier -w "这是一条警告"
notifier -e "这是一条错误"

# 设置10分钟后消息过期（默认24小时）
notifier -w "这是一条警告" -t 10
```

### 3、python程序中使用

```python
import notifier

notifier.info('这是一条信息', '信息', 10)
notifier.warning('这是一条警告', '警告', 10)
notifier.info('这是一条错误', '错误', 10)
```
