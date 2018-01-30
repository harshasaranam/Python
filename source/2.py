sentence=input("enter the sentence: ")
final=sentence.split(' ')
index=len(final)
mid=int(index/2)
if index==2:
    print("no middle word")
if index%2==0 :
    print("Middle words are:",final[mid-1:mid+1])
else :
    print("Middle word is:",final[mid])


def findlong(final) :
    longest_word=' '
    longest_length=0
    for word in final:
        if len(word)>longest_length:
            longest_word=word
            longest_length=len(word)

    print("longest word:", longest_word)
findlong(final)

print("reversed sentence is:", sentence[::-1])