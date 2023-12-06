class recursion:   
    @ staticmethod  
    def factorial(n:int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number; for example, 6

        Returns:
            int: computed factorial
        """  
        # stopping case  
        if n == 1:
            return n
        else:
            # general rule that includes the recursive call
            return n * recursion.factorial(n-1)
        
    @ staticmethod
    def power(number: int, power: int):
        """Takes a specified number to a specified power

        Args:
            number (int): specified number, for example 2
            power (int): specified power, for example 5

        Returns:
            int: computed power
        """      
        if power == 0:
            return 1
        else:
            return number * recursion.power(number, (power-1))
        
    @staticmethod
    def computeMin(nums, i:int, min:int):
        """Finds the minimum number is a specified list of numbers.

        Args:
            nums : Specified list

        Returns:
            int: minimum number
        """  
        # this is the stopping case for recursion
        if i == len(nums):
            return min
        else:
            if nums[i] <= min:
                min = nums[i]
            return recursion.computeMin(nums, i + 1, min)


    @staticmethod
    def reverse(s: str, i: int):
        """Displays a specified string in reverse.

        Args:
            s (str): specified string
        """   
        if i == 0:
            print(" is the reverse of %s using recursion." % (s))
        else: 
            print(s[i - 1], end ='')
            recursion.reverse(s, i - 1)
       

        
