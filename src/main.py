from EncryptData import EncryptData

if __name__ == "__main__":  
    generic_polynomial = '1+x+x**3+x**4+x**8'
    plaintext = bytearray.fromhex('00112233445566778899aabbccddeeff')
    key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f')
    encrypt1 = EncryptData(plaintext, key, generic_polynomial)
    encrypt1.encrypt()
    encrypt1.avalanche()