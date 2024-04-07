#My Programm has a while loop that judges if the number has been able to get divided by 3,5 or 7. If yes the number got passed into the solution_list.
#After going through all the int`s we go through the list and add up all the elements in the list, store this number into the variable solution  and return it.

class Solution:
    def sumOfMultiples(self, intput: int) -> int:
        solution_list = []
        counter = 0
        while counter < intput:
            counter = counter + 1
            if counter % 3 == 0:
                solution_list.append(counter)
            else:
                if counter % 5 == 0:
                    solution_list.append(counter)
                else:
                    if counter % 7 == 0:
                        solution_list.append(counter)
                    else:
                        continue
        
        solution = 0
        for element in solution_list:
            solution = element + solution
        
        return solution
