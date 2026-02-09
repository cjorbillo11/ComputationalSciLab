Using the Volume of a Cylinder formula ($V = \pi r^2 h$), I compared Truncation vs. Rounding to see which method minimizes error. This shows $\pi$ as a fundamental constant in engineering and volume calculation, not just basic circles.

![Lab Results](result.png)

For the Terminal Table (The Grid of Numbers)
This table compares Truncation and Rounding side-by-side across the 20th, 40th, 60th, and 100th decimal places. By comparing the results, you can see exactly where the two methods diverge. The smaller error values at higher decimal counts prove that rounding the input of $\pi$ leads to a more precise calculation of the cylinder's volume than simply cutting the number off.

For the Error Analysis (The Scale of Difference)
Since the differences in precision are too small to see on a standard linear scale, we look at the results in scientific notation (like `1.00e-20`). This visualizes the "residual error." The massive jump in precision between 20 and 100 digits represents the exponential increase in accuracy as more decimals are added. Comparing the two methods confirms that the **Rounding** method consistently maintains a lower error margin than simple Truncation.
