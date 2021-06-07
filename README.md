# 网易云音乐脚本 / Netease Cloud Music Scripts

[![](https://img.shields.io/badge/version-python3.x-green?style=flat-square)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/stars/RRRoger/music163_scripts.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts)
[![GitHub issues](https://img.shields.io/github/issues/RRRoger/music163_scripts.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/RRRoger/music163_scripts.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts/commits/master)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](https://github.com/RRRoger/music163_scripts/blob/master/LICENSE)

## Features

- [获取关注用户数据导出至excel](https://github.com/RRRoger/music163_scripts#%E8%8E%B7%E5%8F%96%E5%85%B3%E6%B3%A8%E7%94%A8%E6%88%B7%E6%95%B0%E6%8D%AE%E5%AF%BC%E5%87%BA%E8%87%B3excel)

- [获取粉丝数据导出至excel](https://github.com/RRRoger/music163_scripts#%E8%8E%B7%E5%8F%96%E7%B2%89%E4%B8%9D%E6%95%B0%E6%8D%AE%E5%AF%BC%E5%87%BA%E8%87%B3excel)

## Use API `NeteaseCloudMusicApi`

> Repo: https://github.com/Binaryify/NeteaseCloudMusicApi
> 
> Api Doc: https://binaryify.github.io/NeteaseCloudMusicApi

```bash
# Installation
git clone git@github.com:Binaryify/NeteaseCloudMusicApi.git
npm install

# Run
node app.js
```

- [调用前须知](https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=调用前须知)
- [登录](https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=登录)
- [获取用户关注列表](https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=获取用户关注列表)
- [获取用户粉丝列表](https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=获取用户粉丝列表)
- [关注/取消关注用户](https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=关注取消关注用户)

## Init

```bash
pip install -r requirements.txt
```

## 获取`关注用户`数据导出至excel

```bash
# for help
python get_follows.py -h

# e.g.
python get_follows.py -o ~/Desktop -u 46304650
```

## 获取`粉丝`数据导出至excel

```bash
# for help
python get_followeds.py -h

# e.g.
python get_followeds.py -o ~/Desktop -u 46304650
```

