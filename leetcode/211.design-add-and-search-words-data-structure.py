# Category: algorithms
# Level: Medium
# Percent: 48.75392%



# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# 
# Implement the WordDictionary class:
# 
# 
# 	WordDictionary() Initializes the object.
# 	void addWord(word) Adds word to the data structure, it can be matched later.
# 	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# 
# 
#  
# Example:
# 
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= word.length <= 25
# 	word in addWord consists of lowercase English letters.
# 	word in search consist of '.' or lowercase English letters.
# 	There will be at most 2 dots in word for search queries.
# 	At most 10⁴ calls will be made to addWord and search.
# 
 

# CODE-START
class WordDictionary:
    def __init__(self):
        self.t = dict()

    def addWord(self, word: str) -> None:
        d = self.t
        for c in word:
            if c not in d:
                d[c] = dict()
            
            d = d[c]
        
        d[None] = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, d):
            while i < n and word[i] != '.':
                if word[i] not in d:
                    return False
                d = d[word[i]]
                i += 1
            
            if i == n:
                return None in d
            
            return any(c is not None and dfs(i + 1, d[c]) for c in d)
        
        return dfs(0, self.t)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# CODE-END
