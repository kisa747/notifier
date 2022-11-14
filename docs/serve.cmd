@echo off
chcp 65001 >NUL

rem 实时预览
sphinx-autobuild source build/html
