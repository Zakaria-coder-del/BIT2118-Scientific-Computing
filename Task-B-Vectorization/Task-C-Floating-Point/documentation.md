# TASK C: FLOATING-POINT ARITHMETIC AND NUMERICAL ERRORS

**Name:** Zakaria Sahal  
**Registration Number:** BSCCS/2025/40516

## 1. Problem Description

This task investigates how computers store decimal numbers and how limited numerical precision can affect calculations.

The modified real-world case examines numerical accuracy in a GPS-style navigation calculation using 32-bit and 64-bit floating-point numbers.

## 2. Assumptions

1. The approximate radius of the Earth is 6,371,000 metres.
2. The system needs to detect a position change of 0.01 metres (1 centimetre).
3. Both float32 and float64 data types are used for comparison.

## 3. Input Values

- Earth's radius: 6,371,000 metres.
- Position change: 0.01 metres.
- Floating-point types: float32 and float64.
- Repeated addition: 0.1 added ten times.

## 4. Mathematical Operations

1. Addition: adding 0.01 metres to the Earth's radius.
2. Precision comparison: comparing float32 and float64 results.
3. Repeated addition: adding 0.1 ten times.
4. Equality comparison: checking whether the calculated result equals the expected value.

## 5. Output and Interpretation

The float32 calculation produces the same value as the original radius. This means the 1-centimetre change is lost.

The float64 calculation preserves the 1-centimetre change.

When 0.1 is added ten times, the result is approximately 0.9999999999999999 instead of exactly 1.0.

These results demonstrate that computers can produce small numerical errors because decimal values are not always represented exactly in binary.

## 6. Changing an Input Parameter

The calculation was performed using two different floating-point types: float32 and float64.

With float32, the small position change is lost because its precision is insufficient at such a large numerical value.

With float64, the small change is detected because it provides greater precision.

## 7. Real-World Application

GPS and navigation systems require accurate position calculations. Small numerical errors can affect the accuracy of location measurements.

Using suitable numerical precision helps reduce these errors.

## 8. Conclusion

This task demonstrates the importance of floating-point precision in scientific computing. Float64 is more suitable than float32 when calculations require detecting very small changes in large numerical values.