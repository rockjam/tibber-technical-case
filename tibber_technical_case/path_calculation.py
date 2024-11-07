# returns a number of uniquely visited positions
def count_unique_positions(x, y, commands):
    positions = calculate_path(x, y, commands)
    return len(set(positions))


# returns a list of all visited position, including positions visited several times
def calculate_path(x, y, commands):
    position_history = [(x, y)]

    for command in commands:
        move(position_history, command)

    return position_history


def move(position_history, command):
    x, y = position_history[-1]
    direction = command["direction"]
    steps = command["steps"]

    for _ in range(steps):
        match direction:
            case "north":
                y -= 1
            case "east":
                x += 1
            case "south":
                y += 1
            case "west":
                x -= 1
        position_history.append((x, y))
