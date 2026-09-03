import sys

path = "/opt/xiaozhi-esp32-server/core/handle/reportHandle.py"
with open(path, "r", encoding="utf-8") as f:
    src = f.read()

if "_decode_opus_frames" in src:
    print("already patched")
    sys.exit(0)

# 1. 还原 opus_to_wav 中的解码逻辑为原始的直拼处理
old_wav = '''        packets = pcm_data if isinstance(pcm_data, list) else [pcm_data]
        decoder = opuslib_next.Decoder(16000, 1)
        pcm_parts = []
        for pkt in packets:
            if not pkt:
                continue
            try:
                pcm_parts.append(decoder.decode(pkt, 960))
            except Exception:
                continue
        pcm_data_bytes = b"".join(pcm_parts)

        if not pcm_data_bytes:
            raise ValueError("没有有效的PCM数据")'''

new_wav = '''        if isinstance(pcm_data, list):
            pcm_data_bytes = b"".join(pcm_data)
        else:
            pcm_data_bytes = pcm_data

        if not pcm_data_bytes:
            raise ValueError("没有有效的PCM数据")'''

if old_wav not in src:
    print("wav block not found, abort")
    sys.exit(1)
src = src.replace(old_wav, new_wav, 1)

# 2. 在 report 中按类型区分：智能体回复(type=2)是Opus帧需解码，用户输入(type=1)已是PCM
old_report = '''        if opus_data:
            audio_data = opus_to_wav(conn, opus_data)
        else:
            audio_data = None'''

new_report = '''        if opus_data:
            if type == 2:
                # 智能体回复收集的是Opus压缩帧，需先解码为PCM
                packets = opus_data if isinstance(opus_data, list) else [opus_data]
                decoder = opuslib_next.Decoder(16000, 1)
                pcm_parts = []
                for pkt in packets:
                    if not pkt:
                        continue
                    try:
                        pcm_parts.append(decoder.decode(pkt, 960))
                    except Exception:
                        continue
                opus_data = b"".join(pcm_parts) if pcm_parts else None
            # 用户输入(type=1)的音频已是PCM，直接转换
            audio_data = opus_to_wav(conn, opus_data) if opus_data else None
        else:
            audio_data = None'''

if old_report not in src:
    print("report block not found, abort")
    sys.exit(1)
src = src.replace(old_report, new_report, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(src)
print("patched ok")
