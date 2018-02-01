sentence=input("enter the sentence: ")              #inputing the sentence
final=sentence.split(' ')                           #splitting the sentence with blank space stored in final
revWords = [word[::-1] for word in final]
newSentence = " ".join(revWords)
index=len(final)                                    #finding the length of the final
mid=int(index/2)
if index==2:                                        #if the length is resulted as 2, we can conclude theres no middle word
    print("no middle word")
if index%2==0 :                                     #if the length is even nuumber, then the sentence contains 2 middle words
    print("Middle words are:",final[mid-1:mid+1])
else :                                              #if odd, prints the middle word, pointing with mid value
    print("Middle word is:",final[mid])


def findlong(final) :                               #to find the longest in sentence
    longest_word=' '
    longest_length=0
    for word in final:                              #for every word in final list, we r gonna find the longest
        if len(word)>longest_length:
            longest_word=word
            longest_length=len(word)

    print("longest word:", longest_word)
findlong(final)


print("reversed sentence is:", newSentence)      #printing the given sentence in reverse order