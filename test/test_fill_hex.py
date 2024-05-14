from src.util.FillHex import FillHex

def test_fill_hex_with_zero():
    string_hex = '0123456789abcdeffedcba'
    result = FillHex.complete_hex_with_zero(string_hex)
    assert result == '0123456789abcdeffedcba00000000000000000000'