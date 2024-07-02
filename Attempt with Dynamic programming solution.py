def algorithmI(s):
    sm = sum(s)
    sm = (sm + 1) // 2
    dynamicProgrammingArray = []
    indexArray = []
    #Filling arrays with 0
    for i in range(sm + 1):
        dynamicProgrammingArray.append(0)
        indexArray.append(-1)
    #At start point we changing values, so when recreating sequence we won't get lost
    dynamicProgrammingArray[0] = 1
    indexArray[0] = -1
    #Counting all the possible sums
    for i in range(len(s)):
        for j in range(sm,s[i] - 1,-1):
            if dynamicProgrammingArray[j - s[i]] == 1 and dynamicProgrammingArray[j] == 0:
                dynamicProgrammingArray[j] = 1
                indexArray[j] = i
    s1 = []
    s2 = []
    i = sm
    #Finding the best sum for use
    while(i >= 0):
        if dynamicProgrammingArray[i] == 1:
            #Recreating sequence that lead us to this sum
            while(indexArray[i] != -1):
                s1.append(indexArray[i])
                i = i - s[indexArray[i]]
            for k in range(len(s)):
                if not(k in s1):
                    s2.append(s[k])
            for k in range(len(s1)):
                s1[k] = s[s1[k]]
            break
        i -= 1
    return [s1,s2]
