the program makes use of a mathematical trick i discorbered through youtube called the chaos game 
the amount of points it calculates depends on the value "accuracy" 


# how its done
1. Generate a point at a random position inside a square whose dementions are the maximum width and height of the triangle 
2. use the x coordinate point from the the random point and the formula of the line of one side of the triangle depending if the x coordinate is on the left or the right. if the randomly generated is less than or equal to the one calculated it must mean it is either on or below the line of the triangle and if the y cor is greater than the calculated one it just repeats the loop until its less
3. calculate the midpoint between that point and a randomly selected vertex of the triangle  using ((X_1 + X_2)/2, (Y_1 + Y_2)/2)
4. append the x and y coordinates to individual lists 
5. repeat step 3 and 4 for the midpoint generated in the last loop
6. plots all the x and y cor using matplotlib 


when all those points are graphed in you will find they form a Sierpiński triangle

# room for improvement
- i think i could probly improve the way the first point is generated possibly by only generating an x coordinate because that would be garunteed to be in the triangle, then use that with the equation of the line and then randomly generate a y cor using that line cor as the upper limit 
- i could also probobly make the code more modular and maybe more objcet orrientated

#what i learnt
- this small project helped me hone my problem solving as well as allowing me to apply skills i've learnt in school  (equation of a line, procedures)
- i learnt about various new python libraries like matplotlib math as well as how to utilize them within code.
- how to use procedures to make code more modular and efficient
- the maths phenomenon that is the cause of the points forming a serpinski triangle 
