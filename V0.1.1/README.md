# Nova AI Communication
基于小智ESP32服务器的智能语音交互系统，部署于腾讯云轻量应用服务器。

当前版本：**V0.1.2**（2026-09-03）

📖 **[使用教程](./tutorial.html)** - 点击查看完整使用指南

## 项目结构


## 部署方式
通过 Docker Compose 部署，包含以下容器：

| 容器 | 端口 | 说明 |
|---|---|---|
| xiaozhi-esp32-server | 8000 (WS), 8003 (HTTP) | 小智服务器主程序 |
| xiaozhi-esp32-server-web | 8002 | 管理界面（智控台） |
| xiaozhi-esp32-server-db | 3306 | MySQL数据库 |
| xiaozhi-esp32-server-redis | 6379 | Redis缓存 |

## 环境配置
- 服务器：腾讯云轻量应用服务器（广州地域）
- 系统：Ubuntu 24.04 LTS
- CPU：2核 AMD EPYC 9754
- 内存：3.6G
- ASR：FunASR（本地 SenseVoice 模型）
- TTS：Minimax（粤语-Cantonese_GentleLady）
- LLM：DeepSeek

## 版本说明
版本功能清单和更新记录请查看 [CHANGELOG.md](./CHANGELOG.md)。

## 注意事项
-  含敏感配置（manager-api secret），已被  排除
- （893MB）已通过 Git LFS 备份到本仓库
-  目录（14MB音乐文件）已被  排除
- 容器内代码修改需手动同步到本仓库
- GitHub推送使用SSH方式（HTTPS国内不稳定）

## 相关链接
- [使用教程](./tutorial.html)
- [更新日志](./CHANGELOG.md)
- [小智ESP32开源项目](https://github.com/xinnan-tech/xiaozhi-esp32-server)
