def IsPalindrome(pal):
    def isChar(hell):
        meow = hell.lower()
        ans = ''
        for c in meow:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c

        return IsPal(ans)

    def IsPal(ans):
        if len(ans) <= 1:
            return True
        else:
            return ans[0] == ans[-1] and IsPal(ans[1:-1])

    return isChar(pal)

sentence = input("Enter a string: ")
print(IsPalindrome(sentence))


