class Solution:
    def isPalindrome(self, number: int) -> bool:
        #If the integer is negativ it cant be a palindrom
        if number < 0:
            return False
        else:
            #we create a string of the integer and read every element into a list
            strint = str(number)
            listofint = [str(digit) for digit in strint]
            #we reverse the list with the .reverse() function
            listofint.reverse()
            #create a new string with the join() function and look if the old and
            #new string are the same which returns true and if not it returns false
            newstrint = ''.join(listofint)
            if newstrint == strint:
                return True
            else:
                return False
            
