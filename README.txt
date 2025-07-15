the program makes use of a mathematical trick i discorbered through youtube 

1. Generate a point at a random position inside a triangle
3. calculate the midpoint between that point and a randomly selected vertex on the triangle 
4. append it to the csv file
5. repeat steps 2,3 for the midpoint generated in the last loop

1. i do step by generating a random x and y coordinate withing the max and min height and width of the triangle, then it plug the x coord of the point into a procedure to calculate the y coord of the line of the triangle, the program then compares the value of the y coord of the random point and the one it found that lies on the line of the triangle. If the  y coord on the line is less than randomly generated y coord that must mean the coordinate point falls outside the bounds of the triangle 



3. use basic math formulas to calculate the midpoint

4. appends the coord to a new line on the csv file, im not sure how i would make it deletes everything previously entered in the csv file and initialize new heading and coords in stead of only adding 

when all those points are graphed in R you will find they form a Sierpiński triangle
