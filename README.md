[![Documentation Status](https://readthedocs.org/projects/sphinxdocs-demo/badge/?version=latest)](https://sphinxdocs-demo.readthedocs.io/zh_CN/latest/?badge=latest)

# 使用 Sphinx 创建说明文档

参考：[ReadtheDocs文档](https://docs.readthedocs.io/en/stable/index.html)、[Sphinx文档](https://www.sphinx-doc.org/zh_CN/master/usage/quickstart.html) 、[myst-parser文档](https://myst-parser.readthedocs.io/en/latest/)、[furo主题](https://pradyunsg.me/furo)

## 安装需求的库

```sh
pip install sphinx
# furo主题，非常漂亮
pip install furo
# markdown 支持
pip install myst-parser

# 自动预览工具
pip install sphinx-autobuild
```

## 创建项目

创建项目，在项目目录执行以下操作：

```sh
mkdir docs
cd docs
sphinx-quickstart

# 根据提示回答指定的问题
# language: zh_CN
```

## 实时预览

```sh
# 实时预览，地址
sphinx-autobuild source build/html
```

## 构建静态文件

```sh
# 构建静态网站文件
make html
```

## furo主题

采用furo主题的网站：

https://pip.pypa.io

https://setuptools.pypa.io

