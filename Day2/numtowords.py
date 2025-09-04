#number to word printing
def num_word(n):
    words=[]
    nums=["one","two","three","four","five","six","seven","eight","nine"]
    if n==0:
        print("zero")
        return
    while(n>0):
        digit=n%10
        words.append(nums[digit-1])
        n//=10
    print(" ".join(reversed(words))) 

num=int(input("Enter a number"))
num_word(num)

