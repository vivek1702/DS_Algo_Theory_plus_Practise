# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6


def most_word_found(sentences):
    count = 0
    for i in range(len(sentences)):
        a = len(sentences[i].split())
        count = max(a, count)

    return count


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(most_word_found(sentences))