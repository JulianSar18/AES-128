from AESOperations import AESOperations
from SBox import SBox 
class StateOperations:      
    def __init__(self, poly: str) -> None:
        s_box_o = SBox() 
        self.poly = poly               
        self.s_box_int = s_box_o.generate(self.poly)
        self.s_box_string = s_box_o.s_box_string(self.s_box_int)
        self.s_box = bytearray.fromhex(self.s_box_string) 
        self.aes = AESOperations(self.poly)        
        
    def add_round_key(self, state: list[list[int]], key_schedule: list[list[list[int]]], round: int):
        round_key = key_schedule[round]
        for r in range(len(state)):
            state[r] = [state[r][c] ^ round_key[r][c] for c in range(len(state[0]))]

    
    def sub_bytes(self, state: list[list[int]]):
        for r in range(len(state)):
            state[r] = [self.s_box[state[r][c]] for c in range(len(state[0]))]

    
    def shift_rows(self, state: list[list[int]]):
    
        # [00, 10, 20, 30]     [00, 10, 20, 30]
        # [01, 11, 21, 31] --> [11, 21, 31, 01]
        # [02, 12, 22, 32]     [22, 32, 02, 12]
        # [03, 13, 23, 33]     [33, 03, 13, 23]

        state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]
    
    def _mix_column(self, col: list[int]):
        c_0 = col[0]
        all_xor = col[0] ^ col[1] ^ col[2] ^ col[3]
        #column 0
        col[0] ^= self.aes.xtime(col[0] ^ col[1]) ^ all_xor
        #column 1
        col[1] ^= self.aes.xtime(col[1] ^ col[2]) ^ all_xor
        #column 2
        col[2] ^= self.aes.xtime(col[2] ^ col[3]) ^ all_xor
        #column 3
        col[3] ^= all_xor ^ self.aes.xtime(c_0 ^ col[3])
    
    def mix_columns(self, state: list[list[int]]):
        for r in state:
            self._mix_column(r)

    