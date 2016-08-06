# mood-learning
###Explanation of distance function for nearest neighbor algorithm:

In order to calculate distance between two mood entries, we need a list of all possible activities. From here we can create a binary vector based on which activities were completed on a certain day and which activities were not.

All Activities | Run | Swim | Walk | Sleep
--------- | ----- |----- | ----- | ------
day1 | 0 | 1 | 1 | 1
day2 | 1 | 0 | 1 | 1

0 = activity not completed, 1 = activity completed

dist(day1, day2) = 1 + 1 + 0 + 0 = 2
