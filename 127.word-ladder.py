#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        l = len(beginWord)

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(l):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()      
            for i in range(l):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
# @lc code=end

