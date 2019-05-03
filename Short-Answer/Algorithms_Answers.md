Add your answers to the Algorithms exercises here.

Exercise I:
a)  a = 0
    while (a < n * n * n):                 #O(n^3) 
      a = a + n * n                     ===> n^2

    If we take n = 2 then the loop will only run 2 times, if we take n = 3 then loop will run 3 twices that means the loop will only run n times because the n^2 inside the loop negates the n^3 outside(start of loop). So, answer is O(n). 


b)  sum = 0
    for i in range(n):                      #O(n)
      i += 1
      for j in range(i + 1, n):             #O(n)
        j += 1
        for k in range(j + 1, n):           #O(n)
          k += 1
          for l in range(k + 1, 10 + k):    #O(9)
            l += 1
            sum += 1 
    
    O(n) * O(n) * O(n) * O(1) = O(n^3) 
    So, answer is O(n^3). 


c)  def bunnyEars(bunnies): 
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)       #O(n)

    So, answer is O(n). 


Exercise-II:

I would implement binary search to solve this problem.
1. Find middle floor of that n-story building and have top, middle, lower floors
2. Then throw a egg from that middle floor if egg breaks,
    then find middle floor of lower floors and then throw egg from that floor,
    and keep finding until you find a floor from where egg doesn't break, 
3. Otherwise, if egg doesn't break, 
    then find middle floor of top floors and then throw egg from that floor, 
    if egg doesn't break from that floor then again repeat dividing and testing 
    until you find a floor from where egg breaks.
4. Step 2 and 3 will repeat until we find right floor. 
