# 回文 使用切片功能翻转文本
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text ==reverse(text)

something = input("enter text: ")
if is_palindrome(something)==1:
    print("yes, it is a palindrome")
else:
    print("no, it is not a palindrome")
"""

enter text: 121
yes, it is a palindrome
enter text: i am yy
no, it is not a palindrome

"""

