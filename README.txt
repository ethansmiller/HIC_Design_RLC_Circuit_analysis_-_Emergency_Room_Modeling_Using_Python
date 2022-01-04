README:

*FOR CODE TO RUN, IT MIGHT BE REQUIRED TO RUN 'pip install GEKKO' IN THE ANACONDA POWERSHELL

After running the Python file provided, please follow along with what is printed in the console, and view the plots for each task under the 'Plots' tab above the console. 

tasks #1 and #4 were rather difficult and required assistance from classmates to acquire accurate results as well as the leverage of code and equations provided in lecture and the cited websites.

classmates: Ethan, Michael, Sean, Matt

#1 - Numerical Integration - HIC

Functionally determine the Head Injury Criterion of a Mercedes Benz given equations from: https://www.intmath.com/applications-integration/hic-part2.php

By integrating over a given time, with the equations from the site mentioned above, we replicate the HIC value of approximately 310. Because our plot shown ('Mercedes Benz Airbag') is very similar to our expected result, we consider this task a success.

#2 - Numerical Integration - Work

Similarly to the first task, we will follow the equations provided from: https://www.intmath.com/applications-integration/8-electric-charges.php

The goal being to determine the work done in separating two electrons, we used the equations given above and in the module project ideas document to integrate and solve for our expected value of 1.728E-16 J. No plot is needed and the result of the integration is printed within the console.

#3 - Differential Equation - RLC

This task had us create an RLC circuit, in which we can define a differential equation and after performing an integration over a given time, plot the resulting voltage. Leveraged from: https://dwightreid.com/blog/education-2/differential-equations-python/second-order-differential-equations-python/

The plot of the voltage output can be viewed in the plots tab of the console. The resulting plot gives us a heavily damped voltage result that reaches 1V over a given time.

#4 - Differential Equation - Hospital ER

This task had us optimize the efficiency of a hospital emergency room based on factors such as the rate of flow of patients into the ERU and ICU, the size of the ERU and ICU, and was optimized accordingly to provide a consistent and efficient flow. The code was leveraged from: http://apmonitor.com/che263/index.php/Main/PythonDynamicSim

Though this is a real-world example, the resulting outputs seen in the plot 'Hospital ER: ERU vs ICU' are very ideal. We can see that as time goes on, the patients entering the ERU is optimized as to not cramp either the ERU or the ICU. As the goal is to not experience the max capacity for either the ERU or ICU over a given time frame, we can assume our prediction is a successful model.