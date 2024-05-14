class IrreduciblePoly:
    @staticmethod
    def to_hex(polinomy: str) -> int:
        try:
            replace_x = polinomy.replace('x', '10')
            binary_representation = eval(replace_x, {'x': 10})
            poly_hex_representation = int(str(binary_representation), 2)
        except: 
            print('Polinomio irreducible no válido')
            return
        return poly_hex_representation

# 
# print(IrreduciblePoly.to_hex("1+x+x**3+x**4+x**8"))



