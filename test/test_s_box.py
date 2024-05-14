import sys
import os
sys.path.append(os.path.abspath('src'))
from SBox import SBox

def test_sbox_int(mocker):
        mock_result = mocker.patch('src.IrreduciblePoly.IrreduciblePoly.to_hex')
        mock_result.return_value = 0x11b
        result = SBox.generate("1 + x + x**3 + x**4 + x**8")
        assert result[0] == 99