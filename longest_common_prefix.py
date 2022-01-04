def longest_common_prefix(strs):
    strs.sort()
    count = 0
    res = ""

    if len(strs) == 1 or strs[0] == "":
        return strs[0]

    while True:
        for x in range(1, len(strs)):
            if strs[0][count] == strs[x][count] and x == len(strs)-1:
                res = strs[0][0:count+1]
                count = count + 1
                if count == len(strs[0]):
                    return res

            if strs[0][count] == strs[x][count]:
                continue

            else:
                return res
            
    return res
                
print(longest_common_prefix(["flower","flow","flight"]))