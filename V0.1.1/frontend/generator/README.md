# 语音盒子主题自定义

## 项目概述

本目录包含从 [xiaozhi-assets-generator](https://github.com/xinnan-tech/xiaozhi-assets-generator) 项目打包的静态文件，用于语音盒子主题的在线自定义与生成。用户可以通过此工具配置唤醒词、字体、表情和聊天背景等元素，并导出为 `assets.bin` 文件。

## 目录结构

```
generator/
├── assets/              # 构建生成的资源文件
│   ├── ft_render-ByO_jG18.js
│   ├── index-CYcyz9xb.js
│   └── index-NXxBVrod.css
├── static/              # 静态资源目录
│   ├── charsets/        # 字符集文件
│   │   ├── deepseek.txt
│   │   ├── gb2312.txt
│   │   ├── latin1.txt
│   │   └── qwen18409.txt
│   ├── fonts/           # 字体资源
│   │   ├── font_noto_qwen_14_1.bin
│   │   ├── font_noto_qwen_16_4.bin
│   │   ├── font_noto_qwen_20_4.bin
│   │   ├── font_noto_qwen_30_4.bin
│   │   ├── font_puhui_deepseek_14_1.bin
│   │   ├── font_puhui_deepseek_16_4.bin
│   │   ├── font_puhui_deepseek_20_4.bin
│   │   ├── font_puhui_deepseek_30_4.bin
│   │   ├── noto_qwen.ttf
│   │   └── puhui_deepseek.ttf
│   ├── multinet_model/  # 自定义唤醒词模型
│   │   ├── fst/
│   │   ├── mn6_cn/
│   │   ├── mn6_en/
│   │   ├── mn7_cn/
│   │   └── mn7_en/
│   ├── twemoji32/       # 32x32 表情图片
│   ├── twemoji64/       # 64x64 表情图片
│   ├── wakenet_model/   # 预设唤醒词模型
│   └── README.md        # 静态资源说明
├── index.html           # 主页面
└── README.md            # 项目说明文档
```

## 主要功能

### 1. 芯片与屏幕配置
- 支持多种芯片型号：ESP32-S3、ESP32-C3、ESP32-P4、ESP32-C6
- 灵活的屏幕分辨率设置
- 支持 RGB565 颜色格式

### 2. 唤醒词配置
- **预设唤醒词**：基于不同芯片支持的 WakeNet 模型
- **自定义唤醒词**：支持中文和英文命令词，可配置阈值和超时时间

### 3. 字体配置
- 预设多种字体：阿里巴巴普惠体、Noto Qwen 等
- 支持上传自定义 TTF/WOFF 字体文件
- 可配置字号和颜色深度（bpp）

### 4. 表情集合
- 提供 21 种基础表情的预设方案（32x32 和 64x64 两种尺寸）
- 支持自定义表情上传

### 5. 聊天背景
- 支持浅色/深色模式切换
- 可配置纯色背景或图片背景
- 自动适配屏幕分辨率

## 使用方法

1. 以服务方式启动 `index.html` 文件
2. 选择芯片型号和屏幕配置
3. 通过不同标签页配置主题元素
4. 点击生成按钮查看资源清单
5. 确认后生成并下载 `assets.bin` 文件

## 技术说明

- 构建后的静态资源位于 `assets/` 目录
- 原始模型和资源文件位于 `static/` 目录
- 支持离线使用，无需额外依赖

## 注意事项

- 本工具为离线使用设计，所有资源已包含在目录中
- 生成的 `assets.bin` 文件需要与语音盒子硬件配合使用
- 自定义资源需注意文件格式和大小限制，以确保兼容