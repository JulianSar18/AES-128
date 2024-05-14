from src.IrreduciblePoly import IrreduciblePoly

def test_policy_hex():
    irreducible_poly_instance = IrreduciblePoly().to_hex("1+x+x**3+x**4+x**8")
    result = irreducible_poly_instance
    assert result == 0x11b
