from bakery import assert_equal

PI = 3.1 

def calculate_area(radius: float) -> float:
    return PI * radius 

def calculate_volume(radius: float, height: float) -> float:
    return 3.1 * radius * height

assert_equal(calculate_area(1.), 3.14159)
assert_equal(calculate_volume(1., 2.), 6.28318)
