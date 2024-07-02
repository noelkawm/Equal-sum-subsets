errorData = []
x = []

for i in range(9):
    errorData.append([])
lenghts = [8,16,32,64,128]
for arraySize in lenghts:
    errorDataPerEpoch = []
    for i in range(50):
        s = []
        for j in range(arraySize):
            s.append(random.randrange(90 * arraySize) + 10 * arraySize)
        if (arraySize <= 128):
            errorDataPerEpoch.append(abs(sum(algorithmI(s)[0]) - sum(s) // 2))
        errorData.append(np.mean(errorDataPerEpoch))
    x.append(arraySize)

#print(errorData)

labels = ["algorithmI"]

fig, ax = plt.subplots()

plt.yscale("log")
ax.errorbar(x, errorData[i], yerr= 0,ecolor='red',capsize=2)
ax.legend(labels)
plt.show()
