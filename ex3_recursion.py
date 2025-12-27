def reverse(s):
    if len(s)<=1:
        return s
    else:
        return reverse(s[1:])+s[0]

def remove_white(s):
    return s.replace(" ",'')

def is_pal(s):
    s= remove_white(s)
    if s == reverse(s):
        return True
    else:
        return False

print(is_pal("t o o t"))
