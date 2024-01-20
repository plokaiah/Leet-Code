class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    stack = []
                    while count > 0:
                        stack.append(str(count % 10))
                        count //= 10
                    while stack:
                        chars[i] = stack.pop()
                        i += 1
                count = 1  # Reset count for the next group
        return i
