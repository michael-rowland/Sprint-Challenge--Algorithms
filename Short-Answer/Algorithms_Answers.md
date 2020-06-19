#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)**. Since the `while` loop contains `n*n*n`, it appears this might be 
quadratic however since, `a` is being incremented by `n*n`, this reduces to a 
linear O(n) runtime.


b) **O(n log n)**. The `for i in range(n)` line evaluates to O(n) as we must 
loop through all numbers in range n. Then a `while` loop is run within each 
iteration of the for loop `while j < n` which include `j *= 2` which amounts to 
a log<sub>2</sub>(n) calculation. So an O(log n) computation is added to the 
runtime


c) **O(n)**. The function `bunnyEars` is called recursively, decrementing 
bunnies by 1, until the base case of `bunnies == 0` is met. So `bunnyEars` is 
called for the same number of times as `bunnies` - or n number of times, so 
O(n). 

## Exercise II

The important aspect of this exercise to notice is that our search strategy is 
trying to minimize both the number of eggs dropped as well as the number of 
eggs broken. If we didn't care about the number of eggs dropped, we could just 
start from the bottom floor and work up, one floor at a time, until the egg 
broke. However we also need to minimize the number of eggs dropped, meaning we 
will need to be willing to risk a few broken eggs, in order to eliminate a 
greater number of floors/guesses ("You have to crack a few eggs to make an 
omelette" if you will!). 

By first dropping an egg off of the middle floor, we will eliminate half of the 
building. Either the egg will break, in which case we will know we can't go any 
higher. Or the egg will *not* break, meaning we know to move up and not search 
any lower.

Once we eliminate half of the building, we find a new midpoint inside the new 
unknown section of the building and repeat this process until we find the 
correct floor.

Speaking programatically: Since floors are incremented, 1 to n, we can treat 
the floors as an ordered list and use a binary search method to determine the 
"correct" floor.

**Psuedocode**
```
# DO THIS PROCESS UNTIL LOW/HIGH CONVERGE
    # FIND A MIDPOINT
    # DROP EGG AT MIDPOINT
    # IF IT BREAKS, TOO HIGH
        # OUR NEW HIGH (TOP FLOOR) IS THE MID
    # IF IT DOESN'T BREAK, TOO LOW
        # NEW LOW (BOTTOM FLOOR) IS THE MID
```

Since we are "halving" our possible guesses each drop, this is a 
log<sub>2</sub>(n) runtime

**Runtime Complexity: O(log n)**