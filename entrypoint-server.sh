#!/bin/bash
# 修复model.pt目录问题：删除目录，从挂载的临时路径复制真实文件
MODEL_TARGET="/opt/xiaozhi-esp32-server/models/SenseVoiceSmall/model.pt"
MODEL_SOURCE="/host-models/SenseVoiceSmall/model.pt"
if [ -d "$MODEL_TARGET" ]; then
    rm -rf "$MODEL_TARGET"
fi
if [ -f "$MODEL_SOURCE" ]; then
    cp "$MODEL_SOURCE" "$MODEL_TARGET"
    echo "模型文件已从挂载路径复制到 $MODEL_TARGET"
fi
# 执行原始启动命令
exec "$@"
