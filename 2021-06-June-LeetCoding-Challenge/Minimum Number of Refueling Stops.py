from typing import List
from heapq import heappop, heappush


class Solution:
    def minRefuelStops(self, target: int, startFuel: int,
                       stations: List[List[int]]) -> int:
        """
        Strategy: Travel until fuel runs out. If target is not reached, refuel
        at station with maximum fuel load from visited stations so far.
        Uses the heap data structure to maintain station with maximum fuel.
        Time Complexity: O(n*logn)

        Parameters
        ----------
        target : int
            Destination.
        startFuel : int
            Inital fuel level.
        stations : List[List[int]]
            Stations are denoted as [position, fuel]

        Returns
        -------
        int
            Minimum number of refuelling stops.
            -1 if it is not possible to reach destination.
        """
        # Add starting and ending points to list of stations
        stations = [[0, 0]] + stations + [[target, 0]]

        # Initializations
        fuel = startFuel
        heap = []
        fuel_stops = 0

        for i in range(1, len(stations)):
            # Fuel used to travel so far
            fuel -= stations[i][0] - stations[i-1][0]

            # If fuel is negative, refuelling is required
            while heap and fuel < 0:
                fuel -= heappop(heap)
                fuel_stops += 1

            # After fully fueling, target cannot be reached
            if fuel < 0:
                return -1

            # Update heap with fuel of current station
            heappush(heap, -stations[i][1])

        return fuel_stops


if __name__ == '__main__':
    obj = Solution()

    target = 1
    startFuel = 1
    stations = []
    assert obj.minRefuelStops(target, startFuel, stations) == 0

    target = 100
    startFuel = 1
    stations = [[10, 100]]
    assert obj.minRefuelStops(target, startFuel, stations) == -1

    target = 100
    startFuel = 10
    stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    assert obj.minRefuelStops(target, startFuel, stations) == 2

    target = 100
    startFuel = 50
    stations = [[25, 25], [50, 50]]
    assert obj.minRefuelStops(target, startFuel, stations) == 1
