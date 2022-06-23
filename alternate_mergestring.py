S1 = "thinkpad"
S2 = "lenevo"

def merge(S1,S2):
    result=""
    i=0
    while (i < len(S1)) or (i< len(S2)):
        if (i < len(S1)):
            result += S1[i]
        if (i < len(S2)):
            result += S2[i]
        i += 1
    return result

print(merge(S1,S2))
