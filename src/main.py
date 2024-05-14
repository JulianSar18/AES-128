from AESEncryption import AESEncryption

if __name__ == "__main__":    
    # NIST AES-128 test vector 1 (Ch. C.1, p. 35)
    encrypt = AESEncryption()
    plaintext = bytearray.fromhex('00112233445566778899aabbccddeeff')
    key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f')
    expected_ciphertext = bytearray.fromhex('69c4e0d86a7b0430d8cdb78070b4c55a')
    ciphertext = encrypt.aes_encryption(plaintext, key)        
    print(ciphertext, " aleluya ", expected_ciphertext)
