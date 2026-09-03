import sys

path = "/opt/xiaozhi-esp32-server/core/handle/reportHandle.py"
with open(path, "r", encoding="utf-8") as f:
    src = f.read()

if "opuslib_next.Decoder(16000, 1)" in src:
    print("already patched")
    sys.exit(0)

if "import opuslib_next" not in src:
    src = src.replace("import time", "import time\nimport opuslib_next", 1)

old = '''        if isinstance(pcm_data, list):
            pcm_data_bytes = b"".join(pcm_data)
        else:
            pcm_data_bytes = pcm_data

        if not pcm_data_bytes:
            raise ValueError("没有有效的PCM数据")'''

new = '''        packets = pcm_data if isinstance(pcm_data, list) else [pcm_data]
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

if old not in src:
    print("target block not found, abort")
    sys.exit(1)

src = src.replace(old, new, 1)
with open(path, "w", encoding="utf-8") as f:
    f.write(src)
print("patched ok")
