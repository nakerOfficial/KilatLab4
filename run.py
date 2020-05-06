text = "1"

calcs = 0
for a in text:
    calcs += ord(a) * len(text)

while len(str(calcs)) < 32:
    calcs *= calcs

result = str(calcs)[0:32]

print("Result: ", result)
