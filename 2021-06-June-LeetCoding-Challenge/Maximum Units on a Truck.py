from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort by number of units per box
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_boxes = 0  # Total boxes loaded in the truck
        total_units = 0  # Corresponding number of units to loaded boxes

        for n_boxes, units in boxTypes:
            # Try to load all boxes
            if total_boxes + n_boxes <= truckSize:
                total_boxes += n_boxes
                total_units += (n_boxes * units)
            # Fill up remaining space
            else:
                remaining_space = truckSize - total_boxes
                total_units += (remaining_space * units)
                break
        return total_units


if __name__ == '__main__':
    obj = Solution()

    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    assert obj.maximumUnits(boxTypes, truckSize) == 8

    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    assert obj.maximumUnits(boxTypes, truckSize) == 91
