

def water_jug_problem():
    print("Initial State: (4-gallon = 0, 3-gallon = 0)")


    print("Step 1: Fill the 4-gallon jug completely.")
    x, y = 4, 0
    print(f"State: (4-gallon = {x}, 3-gallon = {y})")

   
    print("Step 2: Pour water from 4-gallon into 3-gallon jug.")
    x, y = 1, 3
    print(f"State: (4-gallon = {x}, 3-gallon = {y})")


    print("Step 3: Empty the 3-gallon jug.")
    x, y = 1, 0
    print(f"State: (4-gallon = {x}, 3-gallon = {y})")


    print("Step 4: Pour remaining water from 4-gallon into 3-gallon.")
    x, y = 0, 1
    print(f"State: (4-gallon = {x}, 3-gallon = {y})")


    print("Step 5: Fill the 4-gallon jug again.")
    x, y = 4, 1
    print(f"State: (4-gallon = {x}, 3-gallon = {y})")

   
    print("Step 6: Pour water from 4-gallon to 3-gallon until 3-gallon is full.")
    x, y = 2, 3
    print(f"State: (4-gallon = {x}, 3-gallon = {y})")

    print("\nGoal Achieved: 4-gallon jug has exactly 2 gallons of water!")

water_jug_problem()
