# music163_scripts

[![](https://img.shields.io/badge/version-python3.x-green?style=flat-square)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/stars/RRRoger/music163_scripts.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts)
[![GitHub issues](https://img.shields.io/github/issues/RRRoger/music163_scripts.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/RRRoger/music163_scripts.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts/commits/master)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts/blob/master/LICENSE)

## 网易云音乐脚本 / Cloud Music Scripts

- 获取关注用户数据导出至excel

## 使用`NeteaseCloudMusicApi`

> repo: https://github.com/Binaryify/NeteaseCloudMusicApi
> 
> Api Doc: https://binaryify.github.io/NeteaseCloudMusicApi

```bash
# Installation
git clone git@github.com:Binaryify/NeteaseCloudMusicApi.git
npm install

# Run
node app.js
```

## Init

```bash
pip install -r requirements.txt
```

## 获取关注用户数据导出至excel

```bash
# for help
python get_follows.py -h

# e.g.
python get_follows.py -o ~/Desktop -u 46304650
```
