import numpy as np

# Generate one million temperature sensor voltage readings
rng = np.random.default_rng(42)
volts = rng.uniform(0.05, 0.40, 1_000_000)

# Convert voltage into temperature
temperature_c = volts * 100

# Calculate average temperature
mean_temperature = np.mean(temperature_c)

print("TEMPERATURE SENSOR ANALYSIS")
print("First five temperatures:", temperature_c[:5])
print(f"Mean temperature: {mean_temperature:.2f} °C")

# Change the maximum voltage from 0.40 V to 0.50 V
new_volts = rng.uniform(0.05, 0.50, 1_000_000)
new_temperature = new_volts * 100

print(f"New mean temperature: {np.mean(new_temperature):.2f} °C")