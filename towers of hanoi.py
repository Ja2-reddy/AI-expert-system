def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, source, target)

# Main Program
n = int(input("Enter the number of disks: "))
print("The sequence of moves to solve the Towers of Hanoi:")
hanoi(n, 'A', 'B', 'C')










