from tibber_technical_case.path_calculation import calculate_path, count_unique_positions, count_intersection_points

easy_path = [
    {"direction": "east", "steps": 2},
    {"direction": "north", "steps": 1},
]

crossing_path = [
    {"direction": "east", "steps": 2},
    {"direction": "south", "steps": 2},
    {"direction": "west", "steps": 1},
    {"direction": "north", "steps": 3},
]

repeated_path = [
    {"direction": "east", "steps": 2},
    {"direction": "north", "steps": 1},
    {"direction": "south", "steps": 2},
]

back_forth_path = [
    {"direction": "north", "steps": 1},
    {"direction": "south", "steps": 1},
    {"direction": "north", "steps": 1},
    {"direction": "south", "steps": 1},
    {"direction": "north", "steps": 1},
    {"direction": "south", "steps": 1},
]


def test_calculate_easy_path():
    assert calculate_path(10, 22, easy_path) == [
        ((10, 22), (12, 22)),
        ((12, 22), (12, 21))
    ]


def test_count_easy_path():
    assert count_unique_positions(10, 22, easy_path) == 4


def test_calculate_crossing_path():
    assert calculate_path(10, 22, crossing_path) == [
        ((10, 22), (12, 22)),
        ((12, 22), (12, 24)),
        ((12, 24), (11, 24)),
        ((11, 24), (11, 21)),
    ]


def test_count_crossing_path():
    assert count_unique_positions(10, 22, crossing_path) == 8


def test_calculate_repeated_path():
    assert calculate_path(10, 22, repeated_path) == [
        ((10, 22), (12, 22)),
        ((12, 22), (12, 21)),
        ((12, 21), (12, 23))
    ]


def test_count_repeated_path():
    assert count_unique_positions(10, 22, repeated_path) == 5


def test_calculate_back_forth_path():
    assert calculate_path(10, 22, back_forth_path) == [
        ((10, 22), (10, 21)),
        ((10, 21), (10, 22)),
        ((10, 22), (10, 21)),
        ((10, 21), (10, 22)),
        ((10, 22), (10, 21)),
        ((10, 21), (10, 22))
    ]


def test_count_back_forth_path():
    assert count_unique_positions(10, 22, back_forth_path) == 2


def test_perpendicular_cross_intersection_middle():
    assert count_intersection_points(
        ((1, 3), (3, 3)),
        ((2, 2), (2, 4))
    ) == 1
    assert count_intersection_points(
        ((2, 2), (2, 4)),
        ((1, 3), (3, 3))
    ) == 1


def test_perpendicular_cross_intersection_ends():
    assert count_intersection_points(
        ((1, 1), (1, 3)),
        ((1, 1), (3, 1))
    ) == 1
    assert count_intersection_points(
        ((1, 1), (3, 1)),
        ((1, 1), (1, 3))
    ) == 1


def test_perpendicular_cross_no_intersection():
    assert count_intersection_points(
        ((1, 1), (1, 3)),
        ((2, 1), (3, 1))
    ) == 0
    assert count_intersection_points(
        ((2, 1), (3, 1)),
        ((1, 1), (1, 3))
    ) == 0


def test_parallel_cross_horizontal():
    assert count_intersection_points(
        ((0, 0), (3, 0)),
        ((5, 0), (8, 0)),
    ) == 0
    assert count_intersection_points(
        ((0, 0), (8, 0)),
        ((3, 0), (6, 0)),
    ) == 4
    assert count_intersection_points(
        ((0, 0), (5, 0)),
        ((4, 0), (8, 0)),
    ) == 2
    assert count_intersection_points(
        ((3, 0), (6, 0)),
        ((0, 0), (8, 0)),
    ) == 4


def test_parallel_cross_vertical():
    assert count_intersection_points(
        ((0, 0), (0, 3)),
        ((0, 5), (0, 8)),
    ) == 0
    assert count_intersection_points(
        ((0, 0), (0, 8)),
        ((0, 3), (0, 6)),
    ) == 4
    assert count_intersection_points(
        ((0, 0), (0, 5)),
        ((0, 4), (0, 8)),
    ) == 2
    assert count_intersection_points(
        ((0, 3), (0, 6)),
        ((0, 0), (0, 8)),
    ) == 4
