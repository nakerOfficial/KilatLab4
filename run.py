text = 'abcc'

def getHex_32(number):
    hexList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    hexList = hexList + hexList[::-1]

    while number >= 32:
        number -= 32

    return str(hexList[number])

def hashCalc(text):
    length = len(text)
    result = ''

    Hash = 0
    for a in text:
        Hash = (Hash + length * ord(a))

    Hash = Hash // length
    for a in range(32):
        Hash = Hash + length
        result += getHex_32(Hash)

    return result

print(hashCalc(text))

# 'abcd' ed95126aed95126aed95126aed95126a
# 'abcc' dea62159dea62159dea62159dea62159