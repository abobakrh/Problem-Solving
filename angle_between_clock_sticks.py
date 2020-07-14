class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(((hour%12 + minutes/60) * 30 ) - (minutes*6))
        if angle > 180:
            return 360 - angle
        return angle