import sys

path = "/opt/xiaozhi-esp32-server/core/providers/tts/minimax_httpstream.py"
with open(path, "r", encoding="utf-8") as f:
    src = f.read()

old = '"voice_setting": self.voice_setting,'
new = '"voice_setting": ({k: v for k, v in self.voice_setting.items() if v not in ("", None)} if isinstance(self.voice_setting, dict) else self.voice_setting),'

if new in src:
    print("already patched")
    sys.exit(0)
if old not in src:
    print("target line not found, abort")
    sys.exit(1)

src = src.replace(old, new, 1)
with open(path, "w", encoding="utf-8") as f:
    f.write(src)
print("patched ok")
