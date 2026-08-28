# Nova AI Communication

> 基于小智ESP32的智能语音交互系统 | 部署于腾讯云轻量应用服务器

## 简介

Nova AI Communication 是一套完整的智能语音交互系统，基于小智ESP32开源项目构建。系统支持本地语音识别、语音合成、AI对话、IoT设备控制等功能，可通过WebSocket与ESP32设备实时通信，实现语音交互。

## 功能特性

- 语音识别（ASR）：本地FunASR + SenseVoice模型，支持中文/日语/韩语/英语/粤语
- 语音合成（TTS）：Minimax语音合成，支持多种音色
- AI对话（LLM）：DeepSeek大语言模型，支持上下文记忆
- 语音活动检测（VAD）：SileroVAD，自动检测说话开始和结束
- 设备管理：多设备绑定、在线状态、OTA升级
- 插件系统：天气查询、音乐播放、网页搜索、智能家居控制
- MCP工具调用：支持IoT控制、MCP端点、服务端插件

## 系统架构

| 组件 | 技术 | 说明 |
|------|------|------|
| 语音识别 | FunASR / SenseVoice | 本地部署，893MB模型 |
| 语音合成 | Minimax | 粤语女声 |
| 大语言模型 | DeepSeek | API调用 |
| 语音检测 | SileroVAD | 本地部署 |
| 数据库 | MySQL | 设备/用户/对话记录 |
| 缓存 | Redis | 会话缓存 |
| 部署 | Docker Compose | 4容器编排 |

## 服务端口

| 端口 | 协议 | 用途 |
|------|------|------|
| 8000 | WebSocket | ESP32设备语音通信 |
| 8002 | HTTP | 管理后台（智控台） |
| 8003 | HTTP | 视觉分析API |
| 3306 | TCP | MySQL（仅内部） |
| 6379 | TCP | Redis（仅内部） |

## 部署环境

| 项目 | 配置 |
|------|------|
| 服务器 | 腾讯云轻量应用服务器 |
| 地域 | 广州 |
| CPU | 2核 AMD EPYC 9754 |
| 内存 | 3.6G |
| 系统 | Ubuntu 24.04 LTS |
| Docker | Docker Compose |

## 目录结构

```
Nova_AI_Communication/
├── README.md                # 本文件
└── V0.1.1/                  # V0.1.1 版本代码
    ├── app.py               # 主程序入口
    ├── core/                # 核心代码
    │   ├── providers/       # ASR/TTS/LLM/VAD/Memory/Tools
    │   ├── handle/          # 消息处理器
    │   ├── utils/           # 工具类
    │   └── api/             # HTTP API
    ├── config/              # 配置模块 + 音频资源
    ├── plugins_func/        # 插件（天气/音乐/搜索/智能家居）
    ├── performance_tester/  # 性能测试工具
    ├── docker-compose_all.yml
    ├── config.yaml
    ├── tutorial.html        # 使用教程
    └── ...
```

## 快速开始

1. 进入 [V0.1.1/](./V0.1.1/) 目录查看完整源代码
2. 阅读 [使用教程](./V0.1.1/tutorial.html)
3. 下载语音识别模型：[model.pt (892MB)](https://github.com/Thousmous/Nova_AI_Communication/releases/tag/model-backup-v1)
4. 参考docker-compose_all.yml部署Docker容器

## 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| V0.1.1 | 2026-08-28 | 初始版本 |

## 相关链接

- [V0.1.1 源代码](./V0.1.1/)
- [使用教程](./V0.1.1/tutorial.html)
- [模型下载](https://github.com/Thousmous/Nova_AI_Communication/releases/tag/model-backup-v1)
- [更新日志](./V0.1.1/CHANGELOG.md)
- [小智ESP32开源项目](https://github.com/xinnan-tech/xiaozhi-esp32-server)

---
© 2026 Thousmous | Last updated: 2026-08-28
