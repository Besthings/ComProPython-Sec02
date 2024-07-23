print("-----------------")
print("KPH", "\t", "MPH")
print("-----------------")

for Kph in range(60, 131, 10):
    Mph = Kph * 0.6214
    print(Kph, "\t", format(Mph, ".2f"))

print("-----------------")