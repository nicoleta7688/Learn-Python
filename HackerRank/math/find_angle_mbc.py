import math

ab_side = int(input())
bc_side = int(input())

# Calculate the hypotenuse using the Pythagorean theorem
ac_side = math.sqrt(ab_side**2 + bc_side**2)

# M is the midpoint of AC, so BM = MC = AC / 2
bm_side = mc_side = ac_side / 2

# Calculate the angle using the Law of Cosines
angle = math.degrees(
    math.acos(
        (bm_side**2 + bc_side**2 - mc_side**2)
        / (2 * bm_side * bc_side)
    )
)

'''
ABC is a right triangle, 90° at B.
Therefore, ∠ABC = 90°.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find ∠MBC (angle θ°, as shown in the figure) in degrees.

Input Format:
The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
- 0 < AB <= 100
- 0 < BC <= 100
- Lengths AB and BC are natural numbers.

Output Format:
Output ∠MBC in degrees.
Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.
0° < θ < 90°

Sample Input:
10
10

Sample Output:
45°
'''