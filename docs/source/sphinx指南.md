# Sphinx指南

  参考：[Sphinx文档](https://www.sphinx-doc.org/zh_CN/master/usage/quickstart.html) 、[myst-parser文档](https://myst-parser.readthedocs.io/en/latest/) 、<https://pradyunsg.me/furo>

安装需求的库：

```sh
pip install sphinx
# furo主题，非常漂亮
pip install furo
# markdown 支持
pip install myst-parser

# 自动预览工具
pip install sphinx-autobuild
```

创建项目

```sh
mkdir docs
cd docs
sphinx-quickstart

# 根据提示回答指定的问题
> Separate source and build directories (y/n) [n]: y
> Project name: sphinxdocs
> Author name(s): kevin
> Project release []: latest
> Project language [en]: zh_CN
```

项目结构：

```sh
E:\sphinxdocs
│  .readthedocs.yaml       # ReadtheDocs主配置文件。需要自己手动创建。
│
└─docs
    │  make.cmd            # 生成静态网站
    │  Makefile
    │  requirements.txt    # 创建文档需要的依赖，发布至 ReadtheDocs必须
    │  serve.cmd           # 预览文档
    │
    ├─build                # 使用 make.bat 生成静态网站的目录
    └─source               # 文档 md 源码目录
        │  api.md
        │  conf.py         # sphinx 主配置文件，必须放在 md 源码目录下       
        │  index.md
        │  usage.md
        │  写作指南.md
        │
        ├─_static           # 文档图标等静态文件
        │      favicon.png
        │      logo.png
        │
        └─_templates        # 文档模板目录，一般空着就行
```

实时预览

```sh
# 实时预览，地址，可以把此命令写到 serve.cmd 文件里，方便使用。
sphinx-autobuild source build/html
```

构建

```sh
# 构建静态网站文件
make html
```

## furo主题

采用furo主题的网站：

<https://pip.pypa.io>

<https://setuptools.pypa.io>

### 自动生成 API 文档

Sphinx 使用 `autodoc` 插件生成 API 文档，参考：

> 踩坑记，使用 `autodoc` 插件生成 API 文档，需要注意两点：
>
> <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-config.html#autodoc-configuration>
>
> * 如果设置了 Separate source and build directories，需要修改 `.readthedocs.yaml`
>
> ```yaml
> # .readthedocs.yaml
> sphinx:
>    configuration: docs/source/conf.py
> ```
>
> * 必须在 `conf.py` 中指定 Python 源码目录，`conf.py` 必须在`source` 目录下。
>
> ```python
> # docs/source/conf.py
> import sys
> from pathlib import Path
> 
> sys.path.insert(0, str(Path(__file__).parents[2] / 'src'))
> ```

Python 的 `docstring` 书写可以参考：<https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>

### 其它插件

复制按钮：[sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/)

折叠代码：[sphinx-togglebutton](https://sphinx-togglebutton.readthedocs.io/)

代码标签：[sphinx-panels](https://sphinx-panels.readthedocs.io/en/latest/)
