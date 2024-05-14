class FillHex:
    @staticmethod
    def complete_hex_with_zero(hex_string : str):
        currently_length = len(hex_string.replace(" ", ""))
        missing_bytes = (16 - (currently_length % 16)) % 16
        complete_hex = hex_string + "00" * missing_bytes
        return complete_hex