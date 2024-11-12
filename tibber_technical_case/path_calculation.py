# returns a number of uniquely visited positions
def count_unique_positions(x, y, commands):
    path_segments = calculate_path(x, y, commands)
    unique_positions_count = 0

    # how many points on this segment are cleaned by other path
    # only consider paths that are after this one
    for i, this in enumerate(path_segments):
        segment_unique_points = calculate_segment_points(this)
        for j, other in enumerate(path_segments):
            if i > j and perpendicular_cross(this, other):
                segment_unique_points -= 1
        unique_positions_count += segment_unique_points

    return unique_positions_count


# TODO: maybe it should return a number of intersections(0 or 1)
def perpendicular_cross(seg1, seg2):
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    # seg1 horizontal, seg2 vertical
    if y1 == y2 and x3 == x4:
        return min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4)

    # seg1 vertical, seg2 horizontal
    if x1 == x2 and y3 == y4:
        return min(y1, y2) <= y3 <= max(y1, y2) and min(x3, x4) <= x1 <= max(x3, x4)

    return False


# calculates a number of points in the path segment
def calculate_segment_points(segment):
    (x1, y1), (x2, y2) = segment
    if x1 == x2:
        return abs(y2 - y1) + 1
    elif y1 == y2:
        return abs(x2 - x1) + 1


# returns a list of all visited position, including positions visited several times
def calculate_path(x, y, commands):
    path_history = []
    current_position = (x, y)

    for command in commands:
        new_position = move(current_position, command)
        path_history.append((current_position, new_position))
        current_position = new_position

    return path_history


def move(current_position, command):
    direction = command["direction"]
    steps = command["steps"]

    x, y = current_position
    match direction:
        case "north":
            return x, y - steps
        case "east":
            return x + steps, y
        case "south":
            return x, y + steps
        case "west":
            return x - steps, y
