# finding python
sentence = 'Learning Python is so easy! Python is now my favourite programming language.'

print('Does the word "Python" appear in the sentence?', 'Python' in sentence)
print('The first occurrence of "Python" is at index', sentence.find('Python'))
print('The last occurrence of "Python" is at index', sentence.rfind('Python'))
print('"Python" appears', sentence.count('Python'), 'times in the sentence')

print(sentence.split())
for word in sentence.split():
    print(word)

print(sentence.replace('Python', 'Ruby'))
