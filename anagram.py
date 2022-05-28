



def find_anagrams(s,t):
    # [assignment] Add your code here
    s, t = s.replace(" ", ""), t.replace(" ", "")
    if len(s) != len(t):
        return False
    x = {}
    for i in s:
        if i not in x:
            x[i]= 1
        else:
            x[i] += 1
    for j in t:
        if j in x :
            x[j] -= 1
            if x[j] == 0:
                del x[j]
    return len(x) == 0   

print(find_anagrams("able", "be al"))