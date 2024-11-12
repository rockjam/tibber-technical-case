from tibber_technical_case.path_calculation import calculate_path, count_unique_positions, perpendicular_cross

easy_path = [
    {"direction": "east", "steps": 2},
    {"direction": "north", "steps": 1},
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
    assert perpendicular_cross(
        ((1, 3), (3, 3)),
        ((2, 2), (2, 4))
    ) == True
    assert perpendicular_cross(
        ((2, 2), (2, 4)),
        ((1, 3), (3, 3))
    ) == True


def test_perpendicular_cross_intersection_ends():
    assert perpendicular_cross(
        ((1, 1), (1, 3)),
        ((1, 1), (3, 1))
    ) == True
    assert perpendicular_cross(
        ((1, 1), (3, 1)),
        ((1, 1), (1, 3))
    ) == True


def test_perpendicular_cross_no_intersection():
    assert perpendicular_cross(
        ((1, 1), (1, 3)),
        ((2, 1), (3, 1))
    ) == False
    assert perpendicular_cross(
        ((2, 1), (3, 1)),
        ((1, 1), (1, 3))
    ) == False
