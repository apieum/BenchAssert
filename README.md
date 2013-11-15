Small Python Benchmark
===============

The aim is to bench the cost of null functions instead assert in guard clauses.

Results show it takes approximately:

With python 2.7.5

-  1.5x more times for lambda and def
-  2x more times for functor
-  2x more times for lambda and def in optimized mode
-  3x more times for functor in optimized mode

With python 3.3.2

-  1.5x more times for lambda and def
-  2x more times for functor
-  2x more times for lambda and def in optimized mode
-  3x more times for functor in optimized mode



If we consider the low usage of optimized mode (remove 'assert'), 

which rise the risk of having system errors shown to user in production

providing guards clauses wich are null functions by default should be interesting.
