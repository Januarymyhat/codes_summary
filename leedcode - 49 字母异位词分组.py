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
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
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

    

     # 相乘必定相同
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        map = {
            'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,
            'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101
        }
        resmap={}
        reslist = []
        for str in strs:
            m = 1
            for i in range(len(str)):
                m*=map[str[i]]
            if  not m in resmap:
                resmap[m]=[]
            resmap[m].append(str)
        print(resmap.values())
        return [j for j in resmap.values()]
