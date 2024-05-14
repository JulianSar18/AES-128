from IrreduciblePoly import IrreduciblePoly
class RoundConstant:
    @staticmethod
    def generate(polinomy: str):
        r_con_v = [0x00]*10
        r_con_v[0] = 0x01
        used_polinomial = IrreduciblePoly.to_hex(polinomy)
        for i in range(1,10):
            if r_con_v[i-1] < 0x80:
                r_con_v[i] = r_con_v[i-1] << 1
            else: 
                r_con_v[i] = (r_con_v[i-1] << 1) ^ used_polinomial
        r_con_hex_v: list[str] = [f'{x:02x}' for x in r_con_v]
        result_string = ''.join(hex_value for hex_value in r_con_hex_v)
        b_array_hex = bytearray.fromhex(result_string)
        return b_array_hex

# Ejemplo de uso:
#print(RoundConstant.generate("1 + x + x**3 + x**4 + x**8"))