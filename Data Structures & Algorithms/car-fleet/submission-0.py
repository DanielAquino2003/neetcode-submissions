class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        fleet = 0

        for pos, speed in cars:
            time = (target - pos) / speed
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)