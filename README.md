# FlowFree
This is a script for solving Flow Free Android Game 

### Python and C++

#### Algorithm
After reading the game status, 

we create a list of pairs [x1, y1, x2, y2] cell[x1, y1] and cell[x2, y2] have same color

and we want to find a path between cell [x1, y1] and cell [x2, y2] 

without conflict between any other path or pass throw a colored cell except cells ([x1, y1], [x2, y2]) 

We just run a standard backtrack algorithm and try all possible paths 


https://user-images.githubusercontent.com/32108759/222773216-18a27c19-3eac-4553-9870-792076a6b7c5.mp4

