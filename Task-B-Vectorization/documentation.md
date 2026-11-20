# BIT 2118: SCIENTIFIC COMPUTING

**Name:** Zakaria Sahal  
**Registration Number:** BSCCS/2025/40516

## TASK B: Mathematical Functions and Vectorization

### 1. Modified Real-World Problem
A temperature monitoring system uses sensors to measure voltage and convert it into temperature readings using NumPy vectorization.

### 2. Assumptions
- The sensor produces 10 mV per degree Celsius.
- Temperature is calculated using voltage × 100.
- Voltage readings range between 0.05 V and 0.40 V.
- One million readings are generated.

### 3. Input Values
- Random seed: 42.
- Minimum voltage: 0.05 V.
- Maximum voltage: 0.40 V.
- Number of readings: 1,000,000.

### 4. Mathematical Operations
The main operation is multiplication:

Temperature (°C) = Voltage × 100

NumPy performs this operation on all one million readings simultaneously.

### 5. Output and Interpretation
The first five temperatures are approximately:

[32.09, 20.36, 35.05, 29.41, 8.30] °C.

Mean temperature: approximately 22.50 °C.

All temperatures fall between 5 °C and 40 °C, as expected from the voltage range.

### 6. Changing an Input
The maximum voltage was increased from 0.40 V to 0.50 V.

This increases the possible maximum temperature from 40 °C to 50 °C. The average temperature also increases.

### 7. Conclusion
Vectorization allows NumPy to process large amounts of data efficiently. It makes temperature conversion faster and reduces the need for repetitive loops.