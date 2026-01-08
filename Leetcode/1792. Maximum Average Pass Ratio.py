import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        # Function to calculate the gain of adding one student
        def gain(p, t):
            return (p + 1) / float(t + 1) - p / float(t)

        # Max heap (store negative since Python heapq is min-heap)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Distribute extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average ratio
        total_ratio = sum(p / float(t) for _, p, t in heap)
        return total_ratio / len(classes)
