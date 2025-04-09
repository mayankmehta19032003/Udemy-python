
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

encode = ""
decode = ""

if direction == "encode":
    for letter in text:
        index = alphabets.index(letter)
        encode = encode + alphabets[(index+shift) % 26]
    print(encode)
elif direction == "decode":
    for letter in text:
        index = alphabets.index(letter)
        decode = decode + alphabets[(index-shift) % 26]
    print(decode)
else:
    print("Enter valid direction")
