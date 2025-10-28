
facts = ["vertebrate('duck')", "flying('duck')", "mammal('cat')"]


rules = {
    "vertebrate(A)": ["mammal(A)"],
    "animal(A)": ["vertebrate(A)"],
    "bird(A)": ["vertebrate(A)", "flying(A)"]
}


def backward(goal):
    print("\nTrying to prove:", goal)

    
    if goal in facts:
        print(goal, "is a known fact.")
        return True

    
    for conclusion in rules:
  
        if conclusion.split("(")[0] == goal.split("(")[0]:
            print("Using rule to prove:", conclusion)
            premises = rules[conclusion]
            all_true = True

          
            value = goal.split("(")[1].split(")")[0]

            for pre in premises:
                new_goal = pre.replace("A", value)
                if not backward(new_goal):
                    all_true = False
                    break

            if all_true:
                print(goal, "can be derived!")
                facts.append(goal)
                return True

    print(goal, "cannot be derived.")
    return False



goal = input("Enter goal (e.g., animal('duck')): ")

if backward(goal):
    print("\n Goal", goal, "CAN be derived from the knowledge base.")
else:
    print("\n Goal", goal, "CANNOT be derived from the knowledge base.")


