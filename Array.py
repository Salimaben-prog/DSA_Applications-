#Finding a char in the list

class Solution():
        def findWordsCountaining(self,my_list,x):
            #Creating an empty list to store the indexes of the words containing the x
            Index=[]
            for i in range(len(my_list)):
                if x in my_list[i]:
                    #Append the indexes to the Index list
                    Index.append(i)
            return Index


# Example usage
my_list=["Salima","Maroc","china","Welcome"]
x='a'
solution=Solution()
res=solution.findWordsCountaining(my_list,x)
print(res)
