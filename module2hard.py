password = []
for number_one in range(3, 20):
    for i in range(1, 100):
        for j in range(1, 100):
            if number_one % (i + j) == 0:
                password.append((number_one, (i, j)))
            else:
                continue
print(password)
