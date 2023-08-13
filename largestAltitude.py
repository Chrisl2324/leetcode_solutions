class Solution(object):
    def largestAltitude(self, gain):
        current_gain = 0
        for i in range(len(gain)):
            current_gain += gain[i]
            gain[i] = current_gain
        gain.append(0)
        return max(gain) 


