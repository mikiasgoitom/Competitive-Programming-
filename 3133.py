import math
def minEnd(n: int, x: int) -> int:
        """ nums = [x]
        i = x
        while(len(nums) < n):
            i += 1
            if i & x == x:
                nums.append(i)
        return nums[-1] """
        # we change x to string of binary and determine the pos of the 0s
        # we determine the number of zeros we need by log n base 2
        # we count the 0s in x, if it is less than the zeros of the above computation we add 0s infront of x
        # we take binary form of n - 1 and substitute into the zeros we added to x
        binary_x = list(bin(x)[2:][::-1])
        last_n = list(bin(n-1)[2:][::-1])
        zeros = math.ceil(math.log2(n))
        zero_count = 0
        for i in range(len(binary_x)):
                if binary_x[i] == '0':
                      zero_count += 1
        if zero_count < zeros:
                for i in range(zeros - zero_count):
                        binary_x.append(0)
        binary_x = binary_x[::-1]
        last_n = last_n[::-1]
        j = 0
        for i in range(len(binary_x)):
                if len(last_n) < j:
                        break
                if binary_x[-i] == '0':
                        binary_x[i] = last_n[j]
                        j+=1
                        
        return int("".join(binary_x),2)
                        
                  
        

n, x =6715154, 7193485
# n,x =3,4
print(minEnd(n,x))