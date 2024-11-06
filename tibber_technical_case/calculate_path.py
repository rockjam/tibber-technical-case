# returns a number of uniquely visited positions
def count_unique_positions(x, y, commands):
    positions = calculate_path(x, y, commands)
    return len(set(positions))


# returns a list of all visited position, even position visited several times
def calculate_path(x, y, commands):
    position_history = [(x, y)]

    for command in commands:
        positions = move(position_history[-1], command)
        position_history.extend(positions)

    return position_history


def move(current_position, command):
    x, y = current_position
    direction = command["direction"]
    steps = command["steps"]
    history = []

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
        history.append((x, y))
    return history
