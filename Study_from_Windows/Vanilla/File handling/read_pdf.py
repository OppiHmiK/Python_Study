with open("Mastering-Pandas.pdf", "rb") as data:
    pdf = data.readlines()
print(data)

with open("pandas.txt", "wb") as data2:
    data2.write(pdf)
