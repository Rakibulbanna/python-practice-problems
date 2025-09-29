# Problem-1: Longest Word in a Sentence


def longest_word_in_sentence(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word


sentence = input("Enter a sentence: ")
# sentence = "Machine learning is fascinating"
print(longest_word_in_sentence(sentence))
