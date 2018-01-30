input = [1,3,6,2,-1,2,8,-2,9]
output = []
input.sort() #sorting the list
r=len(input)-1
for i in range(len(input)-2):
    l = i + 1  # we don't want l and i to be the same value.
               # for each value of i, l starts one greater
               # and increments from there.
    while (l < r):
        sum_ = input[i] + input[l] + input[r]
        if (sum_ < 0):
            l = l + 1
        if (sum_ > 0):
            r = r - 1
        if not sum_:  # 0 is False in a boolean context
            output.append([input[i],input[l],input[r]])
            l = l + 1  # increment l when we find a combination that works
print(output)