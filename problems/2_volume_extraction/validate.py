from pedal import *

prevent_printing_functions()
ensure_functions_return()

ensure_function('calculate_area', parameters=[float], returns=float)
ensure_called_uniquely('calculate_area', 3)

if call('calculate_area', 1.0) == 3.14:
    explain("Your value for PI (3.14) is not precise enough. Please use 3.14159.", 
            label="low_precision_pi")

unit_test('calculate_area', 
            ([1.0], 3.14159), 
            ([2.0], 12.56636), 
            ([0.0], 0.0))

ensure_function('calculate_volume', parameters=[float, float], returns=float)
ensure_called_uniquely('calculate_volume', 4)

unit_test("calculate_volume",
            ([1.0, 2.0], 6.28318),
            ([5.0, 1.0], 78.53975),
            ([0.0, 10.0], 0.0))

volume_def = find_function_definition('calculate_volume')

if volume_def and not find_function_calls('calculate_area', root=volume_def):
    gently("You need to use `calculate_area` inside of `calculate_volume`.",
            label="not_using_area_in_volume")

ensure_coverage(.9)
ensure_bakery_tests(7)
