l = [1, 2, 3, 4, 5, 2, 3]
sm_fr = 0
sm_wh = 0

ss = sum(l)
print(ss)

for i in range(len(l)):
    sm_fr += l[i]
print(sm_fr) 

k = len(l)
while k > 0:
    k -= 1
    sm_wh += l[k]  
print(sm_wh)