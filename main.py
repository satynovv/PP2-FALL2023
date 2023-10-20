def solve(numheads, numlegs):
    if numheads == 0 or numlegs == 0:
        return "No solution"
    y = (numlegs - (2 * numheads)) / 2
    x = numheads - y

    if x >= 0 and y >= 0 and int(x) == x and int(y) == y:
        return int(x), int(y)
    else:
        return "No solution"
numheads = int(input())
numlegs = int(input())

result = solve(numheads, numlegs)
if result == "No solution":
    print("No solution found.")
else:
    rabbits, chickens = result
    print(f"Number of rabbits: {rabbits}")
    print(f"Number of chickens: {chickens}")
