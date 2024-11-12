# returns a number of uniquely visited positions
def count_unique_positions(x, y, commands):
    path_segments = calculate_path_segments(x, y, commands)
    segments_count = len(path_segments)
    unique_positions_count = 0

    # how many points on this path segment will be cleaned by other path segment in the "future"
    for i in range(0, segments_count):
        this = path_segments[i]
        unique_points = calculate_segment_points(this)
        for j in range(i + 1, segments_count):
            other = path_segments[j]
            unique_points -= count_intersection_points(this, other)

        unique_positions_count += unique_points

    return unique_positions_count


def count_intersection_points(seg1, seg2):
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    # seg1 and seg2 are horizontal
    if y1 == y2 and y3 == y4:
        if y1 == y3:  # and on the same y coordinate
            return count_point_intersections_one_axis((x1, x2), (x3, x4))
        else:
            return 0

    # seg1 and seg2 are vertical
    if x1 == x2 and x3 == x4:
        if x1 == x3:  # and on the same x coordinate
            return count_point_intersections_one_axis((y1, y2), (y3, y4))
        else:
            return 0

    # seg1 horizontal, seg2 vertical
    if y1 == y2 and x3 == x4:
        return int(min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4))

    # seg1 vertical, seg2 horizontal
    if x1 == x2 and y3 == y4:
        return int(min(y1, y2) <= y3 <= max(y1, y2) and min(x3, x4) <= x1 <= max(x3, x4))

    return 0


def count_point_intersections_one_axis(seg1, seg2):
    a1, a2 = seg1
    a3, a4 = seg2
    first_bound = max(min(a1, a2), min(a3, a4))
    second_bound = min(max(a1, a2), max(a3, a4))

    if first_bound <= second_bound:
        return abs(first_bound - second_bound) + 1
    else:
        return 0


# calculates a number of points in the path segment
def calculate_segment_points(segment):
    (x1, y1), (x2, y2) = segment
    if x1 == x2:
        return abs(y2 - y1) + 1
    elif y1 == y2:
        return abs(x2 - x1) + 1


# returns list of all visited segments.
# segment is represent by the start and end point
def calculate_path_segments(x, y, commands):
    path_segments = []
    current_position = (x, y)

    for command in commands:
        new_position = move(current_position, command)
        path_segments.append((current_position, new_position))
        current_position = new_position

    return path_segments


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
