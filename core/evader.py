class EvasionEngine:
    def encode_base64(self, payload):
        import base64
        return base64.b64encode(payload.encode()).decode()

    def hex_encode(self, payload):
        return ''.join(hex(ord(c))[2:] for c in payload)
