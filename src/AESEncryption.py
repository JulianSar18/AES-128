from AESOperations import AESOperations
from KeyExpansion import KeyExpansion
from StateOperations import StateOperations
class AESEncryption:    
    def __init__(self, poly: str) -> None:
        self.poly = poly
    def aes_encryption(self, data: bytes, key: bytes) -> bytes:
        aes = AESOperations(self.poly)
        key_expansion = KeyExpansion(self.poly)
        state_operations = StateOperations(self.poly)
        state = aes.state_from_bytes(data)
        key_schedule = key_expansion.generate_key(key)
        state_operations.add_round_key(state, key_schedule, round=0)
        for round in range(1,10):
            state_operations.sub_bytes(state)
            state_operations.shift_rows(state)
            state_operations.mix_columns(state)
            state_operations.add_round_key(state, key_schedule, round)
        state_operations.sub_bytes(state)
        state_operations.shift_rows(state)
        state_operations.add_round_key(state, key_schedule, round=10)
        cipher = aes.bytes_from_state(state)
        return cipher