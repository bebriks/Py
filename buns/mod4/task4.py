def is_palindrome(word):
    return word == word[::-1]
def make_palindrome(word):
    palindrome = ""
    for i in range(len(word)):
        palindrome += word[i]
    for i in range(len(word) - 1, -1, -1):
        palindrome += word[i]
    return palindrome
word = input("Введите слово: ")
if is_palindrome(word):
    print(f"Слово {word} является палиндромом.")
else:
    palindrome = make_palindrome(word)
    print(f"Палиндром, составленный из слова {word},: {palindrome}")



