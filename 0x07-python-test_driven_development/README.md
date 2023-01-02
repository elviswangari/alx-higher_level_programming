## PYTHON TEST DRIVEN DEVELOPMENT

in this repo we'll use TDD for all our functions, classes, modules etc.  

TDD => is a development cycle where we write code /tests for our code to fail then write code to make the tests pass.  

In the development world TDD is important a we catch bugs even before production.

This repo contains all the code for production and a coresponding test case in */test/* directory  

all tests have bn tested using the doctest module in python using the followingcommand  

```
    python3 -m doctest ./tests/*
 ```

 All functions have been documented using the docstring and we can confirm using the following command  

 ```
    python3 -c 'print(__import__("my_module").__doc__)'
 ```

 <hr>
AUTHOR  

Elvis Wangari - (https://linkedin.com/in/elvis-wangari)
