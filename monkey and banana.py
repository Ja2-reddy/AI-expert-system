# Initial positions
monkey_pos = "door"
box_pos = "center"
banana_pos = "center"
monkey_has_banana = False

print("Initial State:")
print(f"Monkey: {monkey_pos}, Box: {box_pos}, Banana: {banana_pos}\n")

# Step 1: Monkey moves to the box
print("Step 1: Monkey moves to the box.")
monkey_pos = box_pos

# Step 2: Monkey pushes the box under the bananas
print("Step 2: Monkey pushes the box under the bananas.")
box_pos = banana_pos
monkey_pos = banana_pos

# Step 3: Monkey climbs on the box
print("Step 3: Monkey climbs on the box.")

# Step 4: Monkey takes the bananas
print("Step 4: Monkey takes the bananas.")
monkey_has_banana = True

# Final state
print("\nFinal State:")
print(f"Monkey: {monkey_pos}, Box: {box_pos}, Banana: {banana_pos}")
print("Monkey has banana:", monkey_has_banana)