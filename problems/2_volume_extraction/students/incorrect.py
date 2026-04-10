from bakery import assert_equal

PI = 3.14 

def calculate_area(radius: float) -> float:
    return 3.14 * (radius ** 2)

def calculate_volume(radius: float, height: float) -> float:
    return 3.14 * radius * height

assert_equal(calculate_area(1.0), 3.14159)
assert_equal(calculate_area(2.0), 12.56636)
assert_equal(calculate_area(0.0), 0.0)
assert_equal(calculate_volume(1.0, 1.0), 3.14159)
assert_equal(calculate_volume(1.0, 2.0), 6.28318)
assert_equal(calculate_volume(2.0, 1.0), 12.56636)
assert_equal(calculate_volume(0.0, 5.0), 0.0)
