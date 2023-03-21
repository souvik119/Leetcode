'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# Sort the array based on first element to get initial starting list
# Then compare the 2nd element with next item

def merge_overlapping_intervals(intervals):
    # sort the input array so O(nlogn)
    intervals.sort(key = lambda i : i[0])
    # initiatlized to first element of sorted array because we want starting element
    output = [intervals[0]]

    for start, end in intervals[1:]:
        # getting the end value of most recent interval
        lastEnd = output[-1][1]
        # compare last ending with current starting
        if start <= lastEnd:
            # this means we can merge the interval
            output[-1][1] = max(lastEnd, end)
        else:
            # not mergable
            output.append([start, end])

    return output

if __name__ == '__main__':
    print(merge_overlapping_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_overlapping_intervals([[1,4],[4,5]]))
