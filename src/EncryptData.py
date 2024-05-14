from colorama import Fore, Style
from AESEncryption import AESEncryption
import base64
class EncryptData:
    def __init__(self, plain_text: bytearray, key: bytearray, poly: str ) -> None:
        self.plain_text = plain_text
        self.key = key
        self.poly = poly
    def _change_bit(self, plain_text : bytearray):
        bit_list = [b for byte in plain_text for b in '{:08b}'.format(byte)]
        bit_index_to_change = 10
        bit_list[bit_index_to_change] = '1' if bit_list[bit_index_to_change] == '0' else '0'
        new_plaintext = bytearray(int(''.join(bit_list[i:i+8]), 2) for i in range(0, len(bit_list), 8))
        return new_plaintext
    def encrypt(self):
        encrypt = AESEncryption(self.poly)
        ciphertext = encrypt.aes_encryption(self.plain_text, self.key)
        ciphertext_hex = ' '.join('{:02x}'.format(byte) for byte in ciphertext)
        print(Fore.GREEN + '-------------------------------------------------------------')
        print(Fore.GREEN + '----------------------------HEX------------------------------\n')
        print(Fore.WHITE + ciphertext_hex.center(60))
        print(Fore.GREEN + '-------------------------------------------------------------\n', Style.RESET_ALL)
        base64_utf8 = base64.b64encode(bytes.fromhex(ciphertext_hex)).decode('utf-8')
        print(Fore.GREEN + '-------------------------------------------------------------')
        print(Fore.GREEN + '----------------------BASE64 - UTF-8-------------------------\n')
        print(Fore.WHITE + base64_utf8.center(60))
        print(Fore.GREEN + '-------------------------------------------------------------', Style.RESET_ALL)
    def avalanche(self):
        new_plain_text = self._change_bit(self.plain_text)
        print("Original plain text: ", self.plain_text, "\n")
        print("New plain text modify one bit: ", new_plain_text, "\n")
        encrypt1 = AESEncryption(self.poly)
        ciphertext = encrypt1.aes_encryption(self.plain_text, self.key)
        ciphertext_hex = ' '.join('{:02x}'.format(byte) for byte in ciphertext)
        encrypt2 = AESEncryption(self.poly)
        ciphertext2 = encrypt2.aes_encryption(new_plain_text, self.key)
        ciphertext_hex_2 = ' '.join('{:02x}'.format(byte) for byte in ciphertext2)
        print(Fore.GREEN + '-------------------------------------------------------------')
        print(Fore.GREEN + '----------------------------HEX------------------------------\n')
        print(ciphertext_hex,Fore.RED + " --------> ",Style.RESET_ALL,ciphertext_hex_2)
        print(Fore.GREEN + '-------------------------------------------------------------\n', Style.RESET_ALL)
        base64_utf8 = base64.b64encode(bytes.fromhex(ciphertext_hex)).decode('utf-8')
        base64_utf8_2 = base64.b64encode(bytes.fromhex(ciphertext_hex_2)).decode('utf-8')
        print(Fore.GREEN + '-------------------------------------------------------------')
        print(Fore.GREEN + '----------------------BASE64 - UTF-8-------------------------\n')
        print(base64_utf8,Fore.RED + " --------> ",Style.RESET_ALL,base64_utf8_2)
        print(Fore.GREEN + '-------------------------------------------------------------', Style.RESET_ALL)         
    