def combi(candidates, target):
    ans = []
    for each in candidates:
        temp = []
        if target - each >= 0:
           temp.append(each)
        if target - each in candidates:
            





    return



candidates = [2,3,6,7]
target = 7
combi(candidates, target)