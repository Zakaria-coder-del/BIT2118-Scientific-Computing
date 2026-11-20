import numpy as np

print("GPS NUMERICAL PRECISION ANALYSIS")

# Earth's approximate radius in metres
earth_radius = 6371000

# Add a 1 cm position change using float32
radius_32 = np.float32(earth_radius)
change_32 = np.float32(0.01)
result_32 = radius_32 + change_32

print("\nFLOAT32 RESULT")
print("Original radius:", radius_32)
print("After adding 1 cm:", result_32)
print("Was the change detected?", result_32 != radius_32)

# Repeat using float64
radius_64 = np.float64(earth_radius)
change_64 = np.float64(0.01)
result_64 = radius_64 + change_64

print("\nFLOAT64 RESULT")
print("Original radius:", radius_64)
print("After adding 1 cm:", result_64)
print("Was the change detected?", result_64 != radius_64)

# Demonstrate repeated floating-point addition
total = 0.0

for i in range(10):
    total += 0.1

print("\nREPEATED ADDITION")
print("Adding 0.1 ten times gives:", total)
print("Is the result exactly 1.0?", total == 1.0)