class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #Making count Array
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1

        #Rebuilding the people array to arrange it in ascending order
        idx = 0
        i = 1
        while(idx < len(people)):
            while(count[i] == 0):
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1

        #Two Pointer Technique
        left = 0
        right = len(people) - 1
        boats = 0

        while(left <= right):
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            boats += 1
        return boats