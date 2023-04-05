# Week 1.4: Generators and Map-Reduce

## Introduction

This week, we are going to work with generators and [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). During the theoretical session, we have seen how we can replace the creation of lists in a for-loop with list-comprehensions. That makes our code more readable, more maintainable, and more pythonic. We have also seen how we can make of generators and iterables to hide the exact implementation of our collection while we are iterating over it.

## Exercise 1: refactoring your own code.

As a warming up exercise, you are asked to replace the for-loops in your elaboration of [the exercise of last week](week1.3.md) with list comprehensions, if you have not already done that. Especially in the consuming classes, it would make sense to use list comprehensions for either the vertical or the horizontal data aggregation. Make sure you know when to use list comprehension and when to use a standard for-loop: both have their place and function in your program, and you should not use comprehensions for the sake of it.

 Before doing the refactoring, make sure you have pushed your current code to github. While refactoring, make sure your code keeps on working (make use of `assert` statements where possible).

## Exercise 2: functions with data

Create a function that has two parameters: one for data (you can assume this to be a list) and one for the function to be applied to that data. Let the function return a list with new values that are created by applying the function to all the values. 

For example, when I give a list `[1,2,3,4,5]` as a first parameter to this function, and a function to multiply all values of a list by two as a second parameter, the return value of this function should be `[2,4,6,8,10]`. 

Now enhance your function so that it can take in an arbitrary number of functions that all need to be applied to the given data. In this second version, the function returns a list of lists: for every application of a given function, there's a list in this return value. So if I were to give two functions to this function, it should return a list of two lists.

Make use of list comprehensions in your elaboration.


## Exercise 3: refactoring other people's code.

Download [the code for this exercise](files/webcrawler.py). This is a script that crawls [a website with sport clubs in the city Groningen](https://sport050.nl/sportaanbieders/alle-aanbieders/). It generates a csv-file with the url, phone-number and email-address of 414 sport clubs. Run the script for a few moments to see what it does (make sure to exit it using `CTRL-C`, otherwise it will take too long).

```shell
baba@host% python webcrawler.py 
fetch urls
getting sub-urls
extracting the data
414 sub-urls
https://sport050.nl/sportaanbieders/3x3-unites/ ;  06-23929416 ; a.einolhagh@live.nl
https://sport050.nl/sportaanbieders/40up-fitness/ ; 06-81484254 ; info@40upfitness.nl
https://sport050.nl/sportaanbieders/5ersport/ ;  ; 5ersporten@gmail.com?subject=Bericht%20via%20Sport050.nl%20
https://sport050.nl/sportaanbieders/s-exstudiantes/ ;  ; 
https://sport050.nl/sportaanbieders/agsr-gyas/ ;  + 050 526 7445 ;
```

### Step 1: Simple refactor improvements

At the moment, all of the code is working within the global namespace. This is bad for maintainability and re-useability. Create a class `Crawler` in which you copy the code as it now is. Make a method `crawl_site()` within this class in which you put the main loop (the one that starts at line 102). Remember to add `self` as a first parameter to most method of this new class (at least one of the methods can be changed into a `@staticmethod`...).

Now create a second file `main.py` in which you import the `Crawler`-class. Make a new instance of this class and call the main loop method (`crawl_site`) that you have created. If all goes well, the result should be the same as before. Again, make sure to exit the program with `CTRL-C` after a few runs.

At four places at the code, there are lambda expressions; there are even lambda expressions *within* list comprehension. Remove all of these, so that we only have list comprehensions in the end. Do *not* replace the main loop with a list comprehension, as we will be changing this method later on.

### Step 2: Change the loop into an iterator

Until now, we had to stop the execution of the code by hand (by hitting `CTRL-C`). This is because the main loop (in `crawl_site`) runs for all the sub-sites it has found on the site itself. This is, of course, fine if you don't want to do anything else as long as this loop runs, but in order to have more control over the flow of the crawler, it would be better if we were to control the number of sites it needs to parse.

Change the method `crawl_site()` so that it makes use of an internal pointer of the instance (which you need to initialize when you create an instance of the `Crawler` class). Have a look at the `iterator.py`-example that [you can find via this link](files/iterator.py) to get an idea of how this needs to be done. Note: you need to refactor the loop in `crawl_site()` in order to make this work.

If your implementation is correct, you should be able to run the test-code below without errors:

```python
    crawler = Crawler()
    for x in range(5):
        print (str(next(crawler)))
    #Result: five lines of data
```

When you have completed this refactoring, commit your code to git.

### Step 3: Make use of a generator

During the theoretical session, we have talked about the use of `__iter__()` and `__next__()` methods. Implement the `__iter__()` method in `Crawler` so that this creates a generator to loop over the crawled websites. Have every call to this iterator return the next crawled website. Have a look at `generator.py`, that you can find [via this link](files/generator.py) in order to get an idea of how this is to be done.

Next, device test code that you can use to have only a few calls to the `__iter__()` method of the `Crawler`. You can use `zip` to accomplish this.


### Step 4: Come up with enhancements

If you look at the code and you think back about the SOLID principles we discussed during our first session, what other refactoring candidates can you spot in this code? Add a small piece of text to your repo in which you analyse this code.
