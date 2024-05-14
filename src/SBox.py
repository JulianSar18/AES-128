from IrreduciblePoly import IrreduciblePoly

class SBox:
    @staticmethod
    def generate(polinomy: str):
        used_polinomial = IrreduciblePoly.to_hex(polinomy)
        t = [0] * 256
        for i in range(256):
            x = 1
            for _ in range(i):
                x ^= (x << 1) ^ ((x >> 7) * used_polinomial)
            t[i] = x
        s_box_int = [0] * 256
        s_box_int[0] = 0x63
        for i in range(255):
            x = t[255 - i]
            x |= x << 8
            x ^= (x >> 4) ^ (x >> 5) ^ (x >> 6) ^ (x >> 7)
            s_box_int[t[i]] = (x ^ 0x63) & 0xFF
        return s_box_int

    @staticmethod
    def s_box_string(s_box_int: list[int]):
        list_hex = [f'0x{val:02x}' for val in s_box_int]
        s_box_string = ''.join(val_hex[2:] for val_hex in list_hex)
        return s_box_string
#
#s_box = SBox.generate("1 + x + x**3 + x**4 + x**8")
#s_box_String = SBox.s_box_string(s_box)
#print(s_box_String)