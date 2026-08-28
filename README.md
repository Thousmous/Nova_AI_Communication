# Nova AI Communication

基于小智ESP32服务器的智能语音交互系统

## 版本

| 版本 | 日期 | 说明 |
|------|------|------|
| V0.1.1 | 2026-08-28 | 初始版本，含语音识别、语音合成、AI对话、设备管理 |

## 目录结构

```
Nova_AI_Communication/
└── V0.1.1/                    # V0.1.1版本代码
    ├── app.py                  # 主程序入口
    ├── core/                   # 核心代码
    ├── config/                 # 配置模块
    ├── plugins_func/           # 插件功能
    ├── docker-compose_all.yml  # Docker部署配置
    ├── tutorial.html           # 使用教程
    └── ...
```

## 快速开始

1. 进入 [V0.1.1/](./V0.1.1/) 目录查看完整代码
2. 阅读 [使用教程](./V0.1.1/tutorial.html)
3. 下载 [语音识别模型](https://github.com/Thousmous/Nova_AI_Communication/releases/tag/model-backup-v1)

## 技术栈

- ASR：FunASR（本地SenseVoice模型）
- TTS：Minimax
- LLM：DeepSeek
- 部署：Docker Compose
- 服务器：腾讯云轻量应用服务器

## 相关链接

- [V0.1.1目录](./V0.1.1/)
- [使用教程](./V0.1.1/tutorial.html)
- [模型下载](https://github.com/Thousmous/Nova_AI_Communication/releases/tag/model-backup-v1)
- [小智ESP32开源项目](https://github.com/xinnan-tech/xiaozhi-esp32-server)

---
Last updated: 2026-08-28
