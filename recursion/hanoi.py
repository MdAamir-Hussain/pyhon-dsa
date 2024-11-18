def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n-1, auxiliary, target, source)

# Example usage:
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')  # A, B, and C are the names of the towers
