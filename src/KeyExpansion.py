from AESOperations import AESOperations

class KeyExpansion:
    def __init__(self, poly: str) -> None:
        self.poly = poly
    def generate_key(self, key: bytes, nb: int = 4) -> list[list[list[int]]]:
        aes = AESOperations(self.poly) 
        nk = len(key) // 4    
        w = aes.state_from_bytes(key)
        for i in range(nk, nb * (10 + 1)):
            temp = w[i-1]
            if i % nk == 0:
                temp = aes.xor_bytes(aes.sub_word(aes.rot_word(temp)), aes.rcon(i // nk))
            elif nk > 6 and i % nk == 4:
                temp = aes.sub_word(temp)
            w.append(aes.xor_bytes(w[i - nk], temp))           
        return [w[i*4:(i+1)*4] for i in range(len(w)//4)]

# 
# key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f')
# print(KeyExpansion.generate_key(key))
