def water_3jug(jug1_cap,jug2_cap,jug3_cap, target):
    j1_curr = 0
    j2_curr = 0
    j3_curr = 0
    while(j1_curr != target and j2_curr != target and j3_curr != target):
        if(j1_curr == 0):
            j1_curr = jug1_cap
        elif(j2_curr == jug2_cap):
            j2_curr=0
        elif(j3_curr == jug3_cap):
             j3_curr = 0
        else:
            amt1 = min(j1_curr,jug2_cap - j2_curr)
            amt2 = min(j2_curr,jug3_cap - j3_curr)
            j1_curr = j1_curr - amt1
            j2_curr = j2_curr - amt2
            j2_curr = j2_curr+amt1
            j3_curr = j3_curr + amt2
        print(f"jug1 : {j1_curr}/{jug1_cap} jug2 : {j2_curr}/{jug2_cap} jug3 : {j3_curr}/{jug3_cap}")

    print("task completed")
    print(f"jug1 : {j1_curr}/{jug1_cap} jug2 : {j2_curr}/{jug2_cap} jug3 : {j3_curr}/{jug3_cap}")

water_3jug(5,7,6,2)