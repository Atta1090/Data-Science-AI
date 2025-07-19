# Nested loops
color = ["red", "green", "blue"]
items = ['book', 'pen', 'copy']

for c in color:
    for i in items:
        print(f"{c} {i}")
    
# Nested While Loop:
i = 0
while i < 5:
    j = 0
    while j < 5:
        print(f"({i}, {j})")
        j += 1
    i = i+1

# for loop inside while loop
i = 0
while i < 5:
    for j in range(5):
        print(f"({i}, {j})")
    i = i + 1

# while loop inside for loop
for i in range(5):
    j = 0
    while j < 5:
        print(f"({i}, {j})")
        j = j+1