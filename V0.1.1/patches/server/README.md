# 服务端补丁使用说明

> 更新时间：2026-09-03

## 补丁列表

| 补丁脚本 | 修复问题 | 修改文件 |
|------|------|------|
| patch_minimax.py | Minimax TTS 请求携带空 emotion 参数导致接口返回 2013 错误、设备无声音 | core/providers/tts/minimax_httpstream.py |
| patch_report.py | 历史记录音频沙沙声：Opus 压缩帧未解码直接写入 WAV | core/handle/reportHandle.py |
| patch_report2.py | 用户输入记录丢失：修正 patch_report 对 PCM 数据误做 Opus 解码的问题 | core/handle/reportHandle.py |

## 重要说明

1. **V0.1.2 及以后的代码已包含全部修复**，源码部署无需再打补丁
2. 补丁仅适用于**使用官方镜像（server_latest）且通过 docker compose 部署**的场景，在容器重建（down/up、pull 新镜像）后需要重新应用
3. **应用顺序必须为：patch_minimax.py → patch_report.py → patch_report2.py**（patch_report2 依赖 patch_report 的修改）
4. 补丁可重复执行，已应用过会提示 already patched 并安全退出

## 使用方法

在宿主机上执行（假设仓库已克隆到本地，工作目录为仓库根目录）：

```bash
# 1. 确保容器已启动
cd /path/to/deploy-dir
sudo docker compose -f docker-compose_all.yml up -d

# 2. 复制补丁到容器
sudo docker cp V0.1.1/patches/server/patch_minimax.py xiaozhi-esp32-server:/tmp/
sudo docker cp V0.1.1/patches/server/patch_report.py xiaozhi-esp32-server:/tmp/
sudo docker cp V0.1.1/patches/server/patch_report2.py xiaozhi-esp32-server:/tmp/

# 3. 按顺序执行补丁
sudo docker exec xiaozhi-esp32-server python3 /tmp/patch_minimax.py
sudo docker exec xiaozhi-esp32-server python3 /tmp/patch_report.py
sudo docker exec xiaozhi-esp32-server python3 /tmp/patch_report2.py

# 4. 重启容器使补丁生效
sudo docker compose -f docker-compose_all.yml restart xiaozhi-esp32-server
```

## 验证补丁是否生效

```bash
# 应返回 1
sudo docker exec xiaozhi-esp32-server grep -c 'k: v for k, v in self.voice_setting' /opt/xiaozhi-esp32-server/core/providers/tts/minimax_httpstream.py
sudo docker exec xiaozhi-esp32-server grep -c 'if type == 2' /opt/xiaozhi-esp32-server/core/handle/reportHandle.py
```

功能验证：对设备说一句话，确认有语音回复、智控台历史记录中输入输出都正常、音频不是沙沙声。
