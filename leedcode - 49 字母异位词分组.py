'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建一个默认值为列表的字典
        # 当你访问字典中不存在的键时，会返回一个空列表作为默认值
        anagrams_dict = defaultdict(list)
        
        # 遍历字符串数组
        for word in strs:
            # 将单词按照字母顺序排序
            sorted_word = ''.join(sorted(word))
            # 将排序后的单词作为键，原始单词作为值存入字典
            anagrams_dict[sorted_word].append(word)
        
        # 返回字典的值，即为分组后的字母异位词列表
        return list(anagrams_dict.values())
