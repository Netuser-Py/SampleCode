#!python

# The Art+Logic Programming Challenge
# Part 1: encode and decode

# Encode:
# input 14-bit range [-8192..+8191]
# 4 char string
# 1. Add 8192 to the raw value, so its range is translated to [0..16383]
# 2. Pack that value into two bytes such that the most significant bit
#   of each is cleared
#   Unencoded intermediate value (as a 16-bit integer): 00HHHHHH HLLLLLLL
#   Encoded value: 0HHHHHHH 0LLLLLLL
# 3. Format the two bytes as a single 4-character hexadecimal string and
#   return it.

# Decode:
# accept two bytes on input, both in the range [0x00..0x7F] and recombine
# them to return the corresponding integer between [-8192..+8191]


def encode(ivalue):
    w_val = ivalue + 8192
    return str('{:02x}'.format(int('{:014b}'.format(w_val)[:7], 2)) +
               '{:02x}'.format(int('{:014b}'.format(w_val)[7:], 2))).upper()


def decode(ivalue):
    return (int('{:07b}'.format(int('0x' + ivalue[:2], 16)) +
            '{:07b}'.format(int('0x' + ivalue[2:], 16)), 2) - 8192)


def test_encode(ivalue, res_value):
    if encode(ivalue) != res_value.upper():
        print("Error encoding: ", ivalue)
    else:
        print(ivalue, encode(ivalue))


def test_decode(ivalue, res_value):
    if decode(ivalue.upper()) != res_value:
        print("Error decoding: ", ivalue)
    else:
        print(ivalue, decode(ivalue))


# print(encode test Values
def main():
    print('encode tests')
    test_encode(0, '4000')
    test_encode(-8192, '0000')
    test_encode(8191, '7F7F')
    test_encode(2048, '5000')
    test_encode(-4096, '2000')

    print('decode tests')
    test_decode('4000', 0)
    test_decode('0000', -8192)
    test_decode('7F7F', 8191)
    test_decode('5000', 2048)
    test_decode('2000', -4096)
    test_decode('0A05', -6907)
    test_decode('5500', 2688)

    # test encode from file input
    fp_i = open(r'encode_test_in.txt', 'r')
    fp_o = open(r'ConvertedData.txt', 'w')
    fp_o.write('Encode Tests:\n')
    for txt_in in fp_i:
        print(encode(int(txt_in)))
        fp_o.write(encode(int(txt_in)) + '\n')
    fp_i.close()
    # test decode from file input
    fp_o.write('Decode Tests:\n')
    fp_i = open(r'decode_test_in.txt', 'r')
    for txt_in in fp_i:
        print(decode(txt_in))
        fp_o.write(str(decode(txt_in)) + '\n')
    fp_i.close()
    fp_o.close()

    return


if __name__ == '__main__':
    main()
