from EncryptData import EncryptData
from util.FillHex import FillHex
if __name__ == "__main__":       
    # NIST AES-128 test vector 1 (Ch. C.1, p. 35) generic polynomial   
    generic_polynomial = '1+x+x**3+x**4+x**8'
    plaintext_fill_16 = FillHex.complete_hex_with_zero('00112233445566778899aabbccddeeff')   
    plaintext = bytearray.fromhex(plaintext_fill_16)
    key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f')
    encrypt1 = EncryptData(plaintext, key, generic_polynomial)
    encrypt1.encrypt()
    encrypt1.avalanche()
    # message to be encode proposed by the activity
    our_own_polynomial = '1+x+x**5+x**6+x**8'
    #Fill Hex 16 bytes
    proposed_message_fill_16 = FillHex.complete_hex_with_zero('0123456789abcdeffedcba')
    proposed_message = bytearray.fromhex(proposed_message_fill_16)
    proposed_key = bytearray.fromhex('01010101010101010101010101010101')
    encrypt2 = EncryptData(proposed_message, proposed_key, our_own_polynomial)
    encrypt2.encrypt()
    encrypt2.avalanche()
    #First message
    first_message_hex = 'fedcba9876543210ff'
    first_message_fill = FillHex.complete_hex_with_zero(first_message_hex)
    first_message = bytearray.fromhex(first_message_fill)
    encrypt_fisrt_message = EncryptData(first_message, proposed_key, our_own_polynomial)  
    encrypt_fisrt_message.encrypt()  
    #Second message
    second_message_hex = '1100111100111100'
    second_message_fill = FillHex.complete_hex_with_zero(second_message_hex)
    second_message = bytearray.fromhex(second_message_fill)
    encrypt_second_message = EncryptData(second_message, proposed_key, our_own_polynomial)
    encrypt_second_message.encrypt() 
    #Third message
    third_message_hex = 'bbffaa55aaff0055aa'
    third_message_fill = FillHex.complete_hex_with_zero(third_message_hex)
    third_message = bytearray.fromhex(third_message_fill)
    encrypt_third_message = EncryptData(third_message, proposed_key, our_own_polynomial)
    encrypt_third_message.encrypt()
    #Fourth message
    fourth_message_hex = 'aa88dd00ff5500aa77'
    fourth_message_fill = FillHex.complete_hex_with_zero(fourth_message_hex)
    fourth_message = bytearray.fromhex(fourth_message_fill)
    encrypt_fourth_message = EncryptData(fourth_message, proposed_key, our_own_polynomial)
    encrypt_fourth_message.encrypt()
    #Fifth message
    fifth_message_hex = 'fedcba9876543210ff'
    fifth_message_fill = FillHex.complete_hex_with_zero(fifth_message_hex)
    fifth_message = bytearray.fromhex(fifth_message_fill)
    encrypt_fifth_message = EncryptData(fifth_message, proposed_key, our_own_polynomial) 
    encrypt_fifth_message.encrypt()
