import string
def reverse(text):
    return  text[::-1]

def is_palindrome(text):

    text = text.lower()
    text = text.replace(' ','')
    for char in string.punctuation:
        text = text.replace(char,'')
    return text == reverse(text)

def main():
    something = input('enter text:')
    if is_palindrome(something)==1:
        print("yes, {0} is a palindrome".format(something))
    else:
        print("no, {0} is not a palindrome".format(something))

if __name__ == '__main__':
    main()
else:
    print("io_string.py was imported")

