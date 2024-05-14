from RoundConstant import RoundConstant
from SBox import SBox
from IrreduciblePoly import IrreduciblePoly

class AESOperations:
    def __init__(self, poly: str) -> None:
        s_box_o = SBox()  
        self.poly = poly      
        self.s_box_int = s_box_o.generate(self.poly)
        self.s_box_string = s_box_o.s_box_string(self.s_box_int)
        self.s_box = bytearray.fromhex(self.s_box_string) 
        pass
    def state_from_bytes(self, data :bytes) -> list[list[int]]:
        state = [data[i*4:(i+1)*4] for i in range(len(data)//4)]
        return state
    
    def rot_word(self, word: int):
        return word[1:] + word[:1]

    
    def sub_word(self, word: list[int]) -> bytes:        
        substituted_word = bytes(self.s_box[i] for i in word)
        return substituted_word

    
    def rcon(self, i: int) -> bytes:
        rcon_lookup = RoundConstant.generate("1 + x + x**3 + x**4 + x**8")
        rcon_value = bytes([rcon_lookup[i-1], 0, 0, 0])
        return rcon_value

    
    def xor_bytes(self,a: bytes, b: bytes):
        return bytes([x ^ y for (x, y) in zip(a, b)])
    
    
    def xtime(self, a: int) -> int:
        polynomial = IrreduciblePoly()
        if a & 0x80:
            return((a<<1)^ polynomial.to_hex("1 + x + x**3 + x**4 + x**8")) & 0xff
        return a << 1
    
    
    def bytes_from_state(self, state: list[list[int]]) -> bytes:
        cipher = bytes(state[0] + state[1] + state[2] + state[3])
        return cipher
