import collections
import math
#converting the hexadecimal ciphertext
ciphertext = bytes.fromhex(''.join([
    'F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE89',
    '23CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE12',
    '9A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1D',
    'D35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5B',
    'DE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D',
    '732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84C',
    'DF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D',
    '673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B',
    '9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D',
    '730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A',
    '963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D',
    '73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF47',
    '9A7AF0C13AA14794']))

#using kasiski examination to find the key length
#kasiski examination is a method of finding the key length by finding the GCD of the distances between repeated sequences of characters in the ciphertext
def kasiski_examination(ciphertext):
    distances = []
    for i in range(len(ciphertext) - 3):
        for j in range(i + 3, len(ciphertext)):
            if ciphertext[i:i+3] == ciphertext[j:j+3]:
                distances.append(j - i)
    return distances

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_key_length(distances):
    key_lengths = []
    for i in range(2, len(distances)):
        for j in range(i, len(distances)):
            gcd_val = gcd(distances[i-1], distances[j-1])
            if gcd_val > 1:
                key_lengths.append(gcd_val)
    return collections.Counter(key_lengths).most_common(1)[0][0]

distances = kasiski_examination(ciphertext)
key_length = find_key_length(distances)
print(f"\nKey length: {key_length}")

#### We obtain key length =7

#defining function for frequency analysis to obtain the possible keys for different positions
def frequency_analysis(ciphertext, key_length):
    keys = []
    for i in range(key_length):
        l1 = ciphertext[i::key_length]
        data = [0] * 256
        for sft in range(256):
            l11 = [j ^ sft for j in l1]
            d = l11.count(101) / len(l11)
            if 32 <= min(l11) < 48 and 57 < max(l11) <= 127:
                data[sft] = d
        possible = sorted(range(len(data)), key=lambda k: data[k], reverse=True)
        print(f"Possible keys for position {i}: {possible[:7]}")  
        keys.append(possible[0])
    return keys
#finding and printing the possible keys
possible_keys=frequency_analysis(ciphertext, 7)

## manually finding the correct combination of keys at different positions
key = [186, 31, 145, 178, 83, 205, 62]

#decrypt function to decipher the text using bytewise XOR
def decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    for i in range(len(ciphertext)):
        key_byte = key[i % key_length]
        plaintext_byte = ciphertext[i] ^ key_byte
        plaintext.append(plaintext_byte)
    return bytes(plaintext)

# decrypting with the most possible key
plaintext = decrypt(ciphertext, key)
print("Decrypted text:")
print(plaintext.decode('utf-8'))


