import zlib
import config

def do_crc(s):
    crc = "{0:b}".format(zlib.crc32(s.encode()))
    deficit = config.CRC_SIZE - len(crc)
    return '0' * deficit + crc

def bit_stuffing(s):
    output = ""
    one_counter = 0
    for c in s:
        if c == '1':
            one_counter += 1
            output += c
            if one_counter == config.STUFFING_TRESHOLD:
                output += '0'
                one_counter = 0
        else:
            one_counter = 0
            output += c
    return output

def reverse_bit_stuffing(s):
    output = ""
    one_counter = 0
    for c in s:
        if c == '1':
            one_counter += 1
            output += c
        else:
            if one_counter < config.STUFFING_TRESHOLD:
                output += c
            one_counter = 0            
    return output

def add_terminators(s):
    return config.START_TERMINATOR + s + config.END_TERMINATOR

def delete_terminators(s):
    return s[len(config.START_TERMINATOR):(len(s) - len(config.END_TERMINATOR))]

def encode_frame(s):
    return add_terminators(bit_stuffing(s + do_crc(s)))

def decode_frame(s):
    decoded = reverse_bit_stuffing(delete_terminators(s))
    data = decoded[:len(decoded) - config.CRC_SIZE]
    crc = decoded[len(decoded) - config.CRC_SIZE:]
    if (do_crc(data) == crc):
        return data
    else:
        return ""
