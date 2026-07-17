# **String Analyzer**: Count characters, words, and vowels in a sentence.


sentence=input("Enter a sentence: ")

character_count=len(sentence)
word_cont=sentence.split()
word_count=len(word_cont)

vowels_count=0  
for char in sentence.lower():
    if char in "aeiou":
        vowels_count+=1   

print("Character count:", character_count)
print("Word count:", word_count)
print("Vowel count:", vowels_count)
