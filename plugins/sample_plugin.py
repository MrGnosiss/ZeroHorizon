```python
# plugins/sample_plugin.py
from core.plugin_base import PluginBase

class SamplePlugin(PluginBase):
    def name(self):
        return "Sample Exploit Plugin"

    def run(self, target):
        print(f"[+] Running sample plugin against {target}")
        return f"[+] Sample plugin executed on {target}"
```
