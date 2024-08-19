class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vio = ['a', 'e', 'i', 'o', 'u']
        return (len([i for i in range(left, right + 1) if words[i][0] in vio and words[i][-1] in vio]))
