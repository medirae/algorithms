# Category: algorithms
# Level: Medium
# Percent: 69.77413%



# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
# 
# Implement the Trie class:
# 
# 
# 	Trie() Initializes the trie object.
# 	void insert(String word) Inserts the string word into the trie.
# 	boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# 	boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# 
# 
#  
# Example 1:
# 
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# 
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= word.length, prefix.length <= 2000
# 	word and prefix consist only of lowercase English letters.
# 	At most 3 * 10⁴ calls in total will be made to insert, search, and startsWith.
# 
 

# CODE-START
class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        d: dict | None = self.trie
        for c in word:
            d = d.setdefault(c, dict())

        d[''] = True

    def search(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False

            d = d[c]

        return '' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for c in prefix:
            if c not in d:
                return False

            d = d[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# CODE-END
