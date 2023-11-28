class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = defaultdict(int)
        max_freq = 0
        max_count = 0

        for task in tasks:
            count = task_counts[task] + 1
            task_counts[task] = count
            max_freq = max(max_freq, count)

        for key in task_counts:
            if task_counts[key] == max_freq:
                max_count += 1

        partitions = max_freq - 1
        available = partitions * (n - (max_count - 1))
        pending = len(tasks) - (max_freq * max_count)
        idle = max(0, available - pending)

        return len(tasks) + idle

