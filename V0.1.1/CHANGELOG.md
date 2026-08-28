# 版本更新记录

## V0.1.1 (2026-08-21)

### 功能清单

- 语音识别（ASR）：基于FunASR本地识别，支持语言检测和情绪识别
- 语音合成（TTS）：Minimax粤语语音合成（Cantonese_GentleLady）
- 大语言模型（LLM）：DeepSeek对话生成
- 语音活动检测（VAD）：Silero VAD
- 记忆模块：支持nomem/mem_report_only/mem_local_short三种模式
- 工具调用：天气查询、新闻获取、音乐播放、农历查询、退出意图处理
- 声纹识别：支持说话人身份识别（可选启用）
- 管理界面：智控台Web管理（端口8002），支持设备管理、聊天记录查看
- Docker部署：四容器架构（server/web/mysql/redis）
- 配置热重载：支持运行时TTS/LLM/prompt配置变更
- 视觉分析接口：HTTP端口8003

### 修复内容

- 修复记忆界面用户输入缺失问题：
  - `reportHandle.py`：音频转换失败不再阻止文本上报；新增WAV格式检测
  - `asr/base.py`：上报内容从JSON改为纯文本；上报音频从PCM改为WAV格式
  - `enqueue_asr_report`：移除错误的TTS音频缓存逻辑

### 已知限制

- 用户输入语音音频的Opus转WAV在某些场景下仍可能失败，此时仅上报文本
- GitHub HTTPS推送在国内服务器上不稳定，建议使用SSH方式
- models目录（901MB）和music目录（14MB）未纳入git仓库
