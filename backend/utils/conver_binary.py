from backend.utils.hash import crypto_hash
HEX_TO_BINARY={
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hexalvalue):
    binary_string = ''

    for character in hexalvalue:
        binary_string += HEX_TO_BINARY[character]
    return binary_string
def main():
    number = 3107
    hex_number = hex(number)
    print(f'hex_number: {hex_number}')
    print(f'binary_number: {hex_to_binary(hex_number[2:])}') #note hash return 64 characters doesnt have leading 0x
    print(f'original_number: {int(hex_to_binary(hex_number[2:]),2)}') #decimal based(10)
    hex_to_binary_cryptohash = hex_to_binary(crypto_hash('3107'))
    print(f'hex to binary crypto hash: {hex_to_binary_cryptohash}')
if __name__ == '__main__':
    main()
