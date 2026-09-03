# 版本更新记录

## V0.1.2 (2026-09-03)

### 修复内容
- 修复设备无声音问题：Minimax TTS 请求携带空 emotion 参数导致接口返回 2013 错误、不返回音频
  - `core/providers/tts/minimax_httpstream.py`：发送请求前过滤 voice_setting 中的空值参数
- 修复历史记录音频沙沙声：智能体回复收集的 Opus 压缩帧未解码直接写入 WAV
  - `core/handle/reportHandle.py`：写入 WAV 前先解码 Opus 为 PCM
- 修复用户输入记录丢失：用户输入音频（PCM）被误当 Opus 解码导致上报失败
  - `core/handle/reportHandle.py`：按上报类型区分处理（智能体回复解码 Opus，用户输入直接转换）

### 新增内容
- `patches/server/` 目录：三个补丁脚本及使用说明，适用于官方镜像部署场景下容器重建后重新应用

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
- GitHub HTTPS推送在国内服务器上不稳定，建议使用SSH方式
- models目录（901MB）和music目录（14MB）未纳入git仓库
- 和风天气插件 API Key 认证失败（待处理）
- 聊天标题保存报 Agent not found（待处理）
