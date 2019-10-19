# Building a tree according to the code of Prüfer
A program that builds visualization on the graph plane corresponding to the entered Preffer code (https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence). The program takes as input a sequence of positive integers of length n, each number of which is less than n + 2. If the input is incorrect, the text to the left of the field will change to “Invalid sequence”. The program displays the drawn graph when you click on the "Final" button, or step by step builds a tree when you click on the "Step" button. The complexity of this algorithm is O (n ^ 3), where n denotes the length of the input sequence.
Here are some examples of inputs and outputs. 

**input:** an empty string\
**output:** ![Alt text](images/empty.png?raw=true "Title")

**input:** '1'\
**output:** ![Alt text](images/1.png?raw=true "Title")

**input:** '1 2'\
**output:** ![Alt text](images/1_2.png?raw=true "Title")

**input:** '1 2 1 1 7'\
**output:** ![Alt text](images/1_2_1_1_7.png?raw=true "Title")

**input:** '1 2 1 1 7 3 6 1 4 5 3'\
**output:** ![Alt text](images/1_2_1_1_7_3_6_1_4_5_3.png?raw=true "Title")
