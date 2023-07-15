words_after_cleaning = ['anything', 'kills', 'over', '10', 'million', 'people', 'in', 'the', 'next', 'few', 'decades']
complex_words = []
for word in words_after_cleaning:
    vowels = 'aeiou'
    sum1 = 0
    for char in word.lower():
        if char in vowels:
            sum1 += 1
    if sum1 > 2:
        complex_words.append(word)

print(complex_words)

    