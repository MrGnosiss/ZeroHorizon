### `core/plugin_base.py`
```python
# core/plugin_base.py
from abc import ABC, abstractmethod

class PluginBase(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def run(self, target):
        pass
```
