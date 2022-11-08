import heapq

class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.right = None
        self.left = None


class HuffmanCoding:

    def __init__(self, path):
        self.path = path
        self._heap = []

    def _buildheap(self, freq_dict):
        pass

    def __make_frequency_dict(self, text):
        freq_dict = {}
        for i in text:
            if i not in freq_dict:
                freq_dict[i] = 0
            freq_dict[i] += 1

        return freq_dict





    def compress(self):
    # get file from path
    # read text from file
        text = "jsbfabgjbgbskjbgjsdbgd"
        freq_dict = self.__make_frequency_dict(text)
        

    

    #make frequency dictinoary from text

    #construct heap from frequency Dict

    #construct the binary tree from haap

    #Construct the code from binary tree

    #Creating the encode text using the codes

    #Put this encoded text into binary file

    #return this binary file as output


