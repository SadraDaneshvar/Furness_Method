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

- **original_matrix:** The initial square matrix that requires scaling.
- **future_row_sums:** An array representing the desired row sums for the resulting scaled matrix.
- **future_col_sums:** An array representing the desired column sums for the resulting scaled matrix.
- **tolerance:** (Optional) The tolerance level for the normalized error. The algorithm iterates until the normalized error falls below this threshold. The default value is set to 0.01, providing flexibility for users to adjust the convergence criteria.

This script serves as a practical tool for applying the Furness method, enabling users to implement the algorithm with ease and flexibility while addressing the specific constraints associated with the transportation problem at hand.

