class FillHex:
    @staticmethod
    def complete_hex_with_zero(hex_string: str):
        currently_length = len(hex_string.replace(" ", ""))
        missing_bytes = 32 - currently_length
        complete_hex = hex_string + "0" * missing_bytes
        return complete_hex