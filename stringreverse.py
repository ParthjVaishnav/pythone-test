# def reverse(s1,size):
#   if size == 0:
#       return s1[0]
#   return s1[size] + reverse(s1,size-1)
#
# s1='hello'
# size=len(s1)-1
# ans=reverse(s1,size)
# print(ans)
#
def factorail(num):
    if num == 0:
        return 1
    return num * factorail(num-1)

print(factorail(7))
