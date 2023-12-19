<span style="font-family:Times New Roman; font-size:14pt;">
<h1 align="center"><b>Furness Method and its Python Implementation</b></h2>
</span>

<span style="font-family: Times New Roman; font-size: 13pt;">
The Furness method (1965), also known as Fratar method, holds a significant place in the domain of transportation planning, specifically in the crucial task of estimating trip generation within residential areas. Developed to predict the number of trips expected to occur between pairs of zones in residential settings, the Furness method plays a pivotal role in understanding travel patterns and optimizing transportation infrastructure. As a fundamental component of the broader Four-Step Travel Demand Model, which encompasses trip generation, distribution, mode choice, and assignment, the Furness method contributes valuable insights into the dynamics of human mobility, integrating factors such as land use, demographic considerations, and the existing transportation network.
</span>




<span style="font-family: Times New Roman; font-size: 13pt;">

## Overview of the Method

The Furness method offers an algorithmic approach to address the intricacies of the doubly constrained growth-factor problem in transportation planning, as elucidated by the formula and conditions delineated below:


$$T_{ij} = t_{ij} \cdot \tau_i \cdot \Gamma_j \cdot A_i \cdot B_j$$

The formula predicts the future number of trips ($T_{ij}$) from zone $i$ to zone $j$ based on various factors:

- $t_{ij}$: The current number of trips from zone $i$ to zone $j$.
- $\tau_i$: The growth rate for trip production in zone $i$.
- $\Gamma_j$: The growth rate for trip attraction in zone $j$.
- $A_i$: Balancing factor for zone $i$, influencing the prediction based on specific characteristics or conditions.
- $B_j$: Balancing factor for zone $j$, influencing the prediction based on specific characteristics or conditions.

This multiplicative relationship suggests that the future number of trips is influenced by the current trips, growth rates, and specific characteristics of the zones involved. 

We propose modifications to the formula, introducing intermediary variables as follows:

1. Define the trip production potential in zone $i$ as $a_i = \tau_i A_i$
2. Define the trip attraction potential in zone $j$ as $b_j = \Gamma_j B_j$

The modified formula for predicting the future number of trips ($T_{ij}$) is expressed as:

$$T_{ij} = t_{ij} \cdot a_i \cdot b_j$$

This adjusted formulation allows for a more nuanced representation of the trip dynamics, considering the individual growth rates and balancing factors associated with trip production and attraction in their respective zones.
The conditions for this problem are defined as follows:

1. For each zone $i$, the sum of future trips $T_{ij}$ over all zones $j$ must equal the total number of trips originated from zone $i$, denoted as $O_i$:
   
   $$\sum_{j} T_{ij} = O_i$$

2. For each zone $j$, the sum of future trips $T_{ij}$ over all zones $i$ must equal the total number of trips destined for zone $j$, denoted as $D_j$:
   
   $$\sum_{i} T_{ij} = D_j$$

2. The sum of the growth rates for trip production ($\tau_i$) across all zones $i$ multiplied by the sum of the current trip counts ($t_{ij}$) across all zones $j$ should equal the sum of the growth rates for trip attraction ($\Gamma_j$) across all zones $j$ multiplied by the current trip counts ($t_{ij}$) across all zones $i$, and this should be equal to the total number of trips $T$:
   
   $$\sum_{i} \tau_i \sum_{j} t_{ij} = \sum_{j} \Gamma_j \sum_{i} t_{ij} = T$$

These conditions capture the constraints imposed on the future trip distribution, ensuring that the total trips originated from each zone and destined for each zone align with the specified values, and that the growth rates and current trip counts are consistent across all zones. 

To address these conditions, the Furness method is employed, aiming to solve the problem through the iterative procedure described below:

1. **Initialization:** Set $b_j = 1$ as an initial condition.

2. **Trip Generation Constraint:** Solve for $a_i$ with the given $b_j$ to satisfy the trip generation constraint
   
3. **Trip Attraction Constraint:** With the determined $a_i$, solve for $b_j$ to satisfy the trip attraction constraint
   
5. **Update Matrix and Error Checking:** Update the matrix of $T_{ij}$ values and check for errors.

6. **Iterative Refinement:** Repeat steps 2 and 3 until convergence, adjusting $a_i$ and $b_j$ iteratively to improve the accuracy of the model.

This iterative procedure ensures that the trip distribution matrix adheres to the specified conditions, converging to a solution that satisfies both trip generation and attraction constraints. The Furness method provides a systematic approach to optimizing the distribution of trips, taking into account the growth rates and balancing factors associated with each zone.


## Code Script

In the implementation of the Furness method, a Python script has been developed to provide a computational realization of the algorithm. The script includes a function named "Furness," designed to scale an initial matrix iteratively while satisfying specified row and column sum constraints. This method is particularly useful in the context of solving the doubly constrained growth-factor problem in transportation planning.

The "Furness" function takes the following inputs:

- `original_matrix`: The initial Origin-Destination (OD) matrix, representing the $t_{ij}$ values, should be provided in the form of a square NumPy array (`np.array`).
- `future_row_sums`: An array, in `np.array` format, representing the future number of trips originated from each zone.
- `future_col_sums`: An array, in `np.array` format, representing the future number of trips destined for each zone.
- `tolerance` (Optional): The tolerance level for the normalized error. The algorithm iterates until the normalized error falls below this threshold. The default value is set to 0.01, providing flexibility for users to adjust the convergence criteria.

This script serves as a practical tool for applying the Furness method, enabling users to implement the algorithm with ease and flexibility while addressing the specific constraints associated with the transportation problem at hand.

> [!IMPORTANT]
> Integrate this function into your codebase using the following snippet, providing enhanced accessibility from any location. This approach needs an Internet connection. 

``` py
import requests

# The URL of the raw Python file on GitHub
github_url = "https://raw.githubusercontent.com/SadraDaneshvar/Furness_Method/main/furness_method.py"

# Specify the local filename to save the file in the current working directory
local_filename = "furness_method.py"

# Download the file from GitHub with explicit encoding
response = requests.get(github_url)
with open(local_filename, 'w', encoding='utf-8') as file:
    file.write(response.text)

# Execute the code to make the functions/classes available in the notebook
exec(compile(response.text, local_filename, 'exec'))

# Now, you can import the module in your notebook
from furness_method import Furness
```
Below is an example showcasing the proper usage of this function with appropriate input formats:

> [!WARNING]
> Ensure that the `original_matrix`, `future_row_sums`, and `future_col_sums` parameters are provided as NumPy arrays for proper function execution. Using arrays of other types may result in unexpected behavior.

```py
input_OD_matrix = np.array([[5, 50, 100, 200],
                           [50, 5, 100, 300],
                           [50, 100, 5, 100],
                           [100, 200, 250, 20]])

future_origin_sum = np.array([400, 460, 400, 702])
future_destination_sum = np.array(260, 400, 500, 802)

tolerance = 0.001

Furness(input_OD_matrix, 
        future_origin_sum, 
        future_destination_sum, 
        tolerance)
```
Example output:
```
Original OD Matrix:
             Zone 1  Zone 2  Zone 3  Zone 4  Origin
Zone 1            5      50     100     200     355
Zone 2           50       5     100     300     455
Zone 3           50     100       5     100     255
Zone 4          100     200     250      20     570
Destination     205     355     455     620    1635

Future OD Matrix:
              Zone 1  Zone 2   Zone 3   Zone 4    Origin
Zone 1         5.213   43.77   97.536  254.092   400.610
Zone 2        44.901    3.77   84.014  328.298   460.983
Zone 3        76.800  128.97    7.185  187.175   400.129
Zone 4       133.086  223.49  311.266   32.435   700.277
Destination  260.000  400.00  500.000  802.000  1962.000

Normalized Error: 0.18%
```


> [!TIP]
> For interactive usage, you can employ the following code snippet, allowing users to input the necessary data dynamically:


```py
# Take user input for the matrix
rows = int(input("Number of zones: "))

input_OD_matrix = []
for i in range(rows):
    row = list(map(int,
            input("Number of trips from zone " +
                  str(i+1) +
                  " to other zones including itself (seprated by comma):").split(",")))
    input_OD_matrix.append(row)

input_OD_matrix = np.array(input_OD_matrix)

# Take user input for future row sums and column sums
future_origin_sum = np.array(list(map(int,
   input("Number of future trips originated from each zone (seperated by comma): ").split(","))))
future_destination_sum = np.array(list(map(int,
   input("Number of future trips with destinations in each zone (separated by comma): ").split(","))))

# Take user input for tolerance
tolerance = float(input("Tolerance (as a decimal, e.g., 0.01): "))

Furness(input_OD_matrix, future_origin_sum, future_destination_sum, tolerance)
```

And a sample output would be:

```
# User inputs:
## Number of zones: 3
## Number of trips from zone 1 to other zones including itself (seprated by comma):20,30,28
## Number of trips from zone 2 to other zones including itself (seprated by comma):36,32,24
## Number of trips from zone 3 to other zones including itself (seprated by comma):22,34,26
## Number of future trips originated from each zone (seperated by comma): 98,106,122
## Number of future trips with destinations in each zone (separated by comma): 102,118,106
## Tolerance (as a decimal, e.g., 0.01): 0.005

Original OD Matrix:
             Zone 1  Zone 2  Zone 3  Origin
Zone 1           20      30      28      78
Zone 2           36      32      24      92
Zone 3           22      34      26      82
Destination      78      96      78     252

Future OD Matrix:
              Zone 1   Zone 2   Zone 3   Origin
Zone 1        25.802   35.540   36.734   98.075
Zone 2        42.590   34.764   28.874  106.228
Zone 3        33.609   47.696   40.392  121.697
Destination  102.000  118.000  106.000  326.000

Normalized Error: 0.19%
```

If you have any feedback, please reach out to me at dsadra80@gmail.com

## License

[MIT LICENSE](LICENSE)
