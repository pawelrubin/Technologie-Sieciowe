import unittest as ut
import protocol as prot
import config as c
import random as rand

class TestStuffing(ut.TestCase):
    
    def test_stuffing(self):
        data = "0111111110111111011011"
        self.assertEqual(
            "011111011101111101011011",
            prot.bit_stuffing(data)
        )

    def test_reverse_stuffing(self):
        data = "0111111110111111011011"
        self.assertEqual(
            data,
            prot.reverse_bit_stuffing("011111011101111101011011")
        )

    def test_encoding(self):
        data = "0111111110111111011011"
        self.assertEqual(
            c.START_TERMINATOR + 
            prot.bit_stuffing(data + prot.do_crc(data)) 
            + c.END_TERMINATOR, 
            prot.encode_frame(data)
        )

    def test_decoding(self):
        data = "{0:b}".format(rand.randint(2^30, 2^32))
        self.assertEqual(
            data,
            prot.decode_frame(prot.encode_frame(data))
        )
        

if __name__ == '__main__':
    ut.main()
