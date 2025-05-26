with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

from collections import deque

def gear_system_solver(target, max_steps=8):
    start = (3, 3, 3)
    visited = set()
    queue = deque()
    queue.append((start, []))

    # Karok hatásai
    levers = {
        "left": [1, 1, 0],
        "right": [0, 1, 1]
    }

    def rotate(state, lever):
        return tuple((state[i] + levers[lever][i] - 1) % 3 + 1 for i in range(3))

    while queue:
        state, actions = queue.popleft()
        if list(state) == target:
            print(' '.join(actions))
            return
        if len(actions) >= max_steps:
            continue
        for lever in ["left", "right"]:
            new_state = rotate(state, lever)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, actions + [lever]))
    
    print("Megoldhatatlan")

gear_system_solver(input)
