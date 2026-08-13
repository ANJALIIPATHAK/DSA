class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitMap = defaultdict(int)
        maxFruits = 0
        fruitSum = 0
        left = 0
        for right in range(0, len(fruits)):
            fruitMap[fruits[right]] += 1
            fruitSum += 1
            while(len(fruitMap) > 2):
                fruitSum -= 1
                fruitMap[fruits[left]] -= 1
                if fruitMap[fruits[left]] == 0:
                    del fruitMap[fruits[left]]
                left += 1
            maxFruits = max(maxFruits, fruitSum)
        return maxFruits        