"""
We are given an array asteroids of integers representing asteroids in a row.
The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
-----------
Results
Runtime: 3 ms - beats 93.75%
Memory: 19.05 MB - beats 18.14%
"""
import tester


def solution(asteroids: list[int]) -> list[int]:
    left = []
    right = []

    for a in asteroids:
        if a > 0:
            right.append(a)
        else:
            while len(right) > 0 and a:
                collision = right[-1]
                if collision <= -a:
                    # Right-moving astroid destroyed
                    right.pop()
                if collision >= -a:
                    # Left-moving astroid destroyed
                    a = 0
            if a:
                # if left-moving astroid still exists after all collisions
                left.append(a)

    return left + right


tester.test([[5,10,-5]], [5,10], solution)
tester.test([[8,-8]], [], solution)
tester.test([[10,2,-5]], [10], solution)
tester.test([[3,5,-6,2,-1,4]], [-6,2,4], solution)
