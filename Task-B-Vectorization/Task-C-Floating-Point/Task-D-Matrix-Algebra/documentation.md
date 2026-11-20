# TASK D: MATRIX ALGEBRA AND MATRIX OPERATIONS

**Name:** Zakaria Sahal  
**Registration Number:** BSCCS/2025/40516

## 1. Problem Description

This task demonstrates how matrix algebra can be used to transform two-dimensional coordinates.

The modified real-world case involves rotating and scaling a floor plan of a rectangular room. The program uses NumPy matrix operations to change the position and size of the room on a drawing.

## 2. Assumptions

1. The room measures 4 metres by 3 metres.
2. The room is represented by its four corner coordinates.
3. The floor plan is rotated by 30 degrees.
4. The drawing is reduced to half its original size.
5. All transformations are performed using matrix multiplication.

## 3. Input Values

The original coordinates are:

- (0, 0)
- (4, 0)
- (4, 3)
- (0, 3)

Other input parameters:

- Rotation angle: 30 degrees.
- Horizontal scaling factor: 0.5.
- Vertical scaling factor: 0.5.

## 4. Mathematical Operations

1. Matrix creation: storing the four room corners in a NumPy array.
2. Rotation: using sine and cosine to construct a rotation matrix.
3. Scaling: creating a matrix that reduces both dimensions by half.
4. Matrix multiplication: combining the rotation and scaling matrices.
5. Coordinate transformation: multiplying the original points by the transpose of the transformation matrix.
6. Determinant calculation: checking whether the transformation can be reversed.

## 5. Output and Interpretation

The program produces a transformation matrix and the new coordinates of the four corners.

The transformed coordinates are approximately:

- (0, 0)
- (1.7321, 1.0000)
- (0.9821, 2.2990)
- (-0.7500, 1.2990)

The determinant is approximately 0.25.

This means the floor plan's area is reduced to one-quarter of its original area. The room retains its rectangular shape but becomes smaller and is rotated.

## 6. Changing an Input Parameter

The rotation angle was changed from 30 degrees to 45 degrees.

This changes the orientation of the floor plan and produces different transformed coordinates.

However, the determinant remains 0.25 because changing the rotation angle does not change the