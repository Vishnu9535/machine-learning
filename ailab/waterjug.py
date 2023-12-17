#8

def water_jug_problem(jug1_capacity, jug2_capacity, jug3_capacity, target_amount):
    jug1_current = 0
    jug2_current = 0
    jug3_current = 0
    
    while jug1_current != target_amount and jug2_current != target_amount and jug3_current != target_amount:
        print(f"Jug 1: {jug1_current} / {jug1_capacity}, Jug 2: {jug2_current} / {jug2_capacity}, Jug 3: {jug3_current} / {jug3_capacity}")
        
        if jug1_current == 0:
            jug1_current = jug1_capacity
        elif jug2_current == jug2_capacity:
            jug2_current = 0
        elif jug3_current == jug3_capacity:
            jug3_current = 0
        else:
            transfer_amount1 = min(jug1_current, jug2_capacity - jug2_current)
            transfer_amount2 = min(jug2_current, jug3_capacity - jug3_current)
            
            jug1_current -= transfer_amount1
            jug2_current += transfer_amount1
            jug2_current -= transfer_amount2
            jug3_current += transfer_amount2
            
        print(f"Jug 1: {jug1_current} / {jug1_capacity}, Jug 2: {jug2_current} / {jug2_capacity}, Jug 3: {jug3_current} / {jug3_capacity}")
        
    print("Target amount reached!")
    print(f"Jug 1: {jug1_current} / {jug1_capacity}, Jug 2: {jug2_current} / {jug2_capacity}, Jug 3: {jug3_current} / {jug3_capacity}")

def main():
    jug1_capacity = int(input("Enter the capacity of Jug 1: "))
    jug2_capacity = int(input("Enter the capacity of Jug 2: "))
    jug3_capacity = int(input("Enter the capacity of Jug 3: "))
    target_amount = int(input("Enter the target amount: "))
    
    water_jug_problem(jug1_capacity, jug2_capacity, jug3_capacity, target_amount)
main()