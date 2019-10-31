# Building a tree corresponding to the given Prüfer code
The program builds visualization of the graph corresponding to the Prüfer code (https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence) entered by user. The program takes as input a sequence of positive integers of length n, whose each element less or equal than n + 2. If the input is incorrect, the output text to the left of the field will change to “Invalid sequence”. The program displays the required tree when you click the "Final" button, or builds the tree step by step when you click the "Step" button. The complexity of our algorithm is O (n ^ 2), where n denotes the length of the input sequence. 

The program is created as part of the "Discrete analysis" course by A.M. Raigorodskiy at Moscow Institute of Physics and Technology. 
Website of the course: https://mipt.ru/education/chairs/dm/education/courses/common_courses/year2/diskretnyy-analiz-2017-18.php

Other existing related programs:
https://github.com/skswanke/pruferdecode - a similar implementation in javascript using web technologies \
https://github.com/skswanke/pruferdecode - an interactive jupyter notebook that implements tree building by code, and code by adjacency matrix. Authors - Akopyan Albert and Mazheika Michael, MIPT 2019 \
https://gist.github.com/forthright48/f403befb8c12ad18c38f21825ce98af6 - a console program for constructing an adjacency matrix by the code of the proliferator, implementation in C ++. \


Here are some examples of inputs and outputs. 

**input:** an empty string\
**output:** \
![Alt text](images/empty.png?raw=true "Title")

**input:** '1'\
**output:** \
![Alt text](images/1.png?raw=true "Title")

**input:** '1 2'\
**output:** \
![Alt text](images/1_2.png?raw=true "Title")

**input:** '1 2 1 1 7'\
**output:** \
![Alt text](images/1_2_1_1_7.png?raw=true "Title")

**input:** '1 2 1 1 7 3 6 1 4 5 3'\
**output:** \
![Alt text](images/1_2_1_1_7_3_6_1_4_5_3.png?raw=true "Title")


Author: Berdovskii Alexey
Date: 20.10.19
