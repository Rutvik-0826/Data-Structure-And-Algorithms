# Autocomplete with Tries
# Author: Jitendra Bhamare

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.word_finished = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = '', suffix_list = None):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if suffix_list == None:
            suffix_list = []

        ## When node is empty, it's leaf node, append it and return
        if self.children.keys() == []:
            suffix_list.append(suffix)
            return

        ## if append it to suffix_list if we find a word.
        if self.word_finished == True:
            suffix_list.append(suffix)
        
        ## Recursively call 'suffixes' (DFS) and form string from children keys 
        for key in self.children.keys():
            self.children[key].suffixes(suffix+key, suffix_list)
        
        ## Remove an empty string from list
        suffix_list = ' '.join(suffix_list).split()
        return suffix_list
        #print("my suff: {}".format(self.suffix_list))



## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.word_finished = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return current_node


## Testcase ##########

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word) 

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

## Call function f
prefix_list = ['f', 'a', 'an', 'tr', 't', '', 'q']

for prefix in prefix_list:
    print("input_text: {}".format(prefix))
    print("output: ")
    f(prefix)
    print("\n")