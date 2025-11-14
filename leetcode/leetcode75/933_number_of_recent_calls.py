"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter()
Initializes the counter with zero recent requests.

int ping(int t)
Adds a new request at time t,
where t represents some time in milliseconds,
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Constraints:
1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
-----------
Results
Runtime: 32 ms - beats 77.39%
Memory: 23.18 MB - beats 41.57%
"""
import tester
from collections import deque

class RecentCounter:

    def __init__(self):
        self.pings = deque()

    def ping(self, t: int) -> int:
        target = t - 3000
        while self.pings and self.pings[0] < target:
            self.pings.popleft()
        self.pings.append(t)
        return len(self.pings)


def solution(pings: list[int]) -> list[None|int]:
    counter = RecentCounter()
    return [counter.ping(i) for i in pings]


tester.test([[1,100,3001,3002]], [1, 2, 3, 3], solution)
