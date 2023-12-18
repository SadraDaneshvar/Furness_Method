## Developed by Sadra Daneshvar
### Dec 18, 2023

import numpy as np
import pandas as pd


def Furness(original_matrix, future_row_sums, future_col_sums, tolerance=0.01):
    # Set an initial error value greater than the tolerance to ensure the loop starts
    normalized_error = 1.1

    # Get the size of the square matrix
    original_matrix_size = original_matrix.shape[0]

    # Generate column and row names
    original_column_names = [f"Zone {i}" for i in range(1, original_matrix_size + 1)]

    # Convert the matrix into a DataFrame
    original_data = pd.DataFrame(
        original_matrix, columns=original_column_names, index=original_column_names
    )

    # Add column sums
    original_data["Origin"] = original_data.sum(axis=1)

    # Add row sums
    original_data.loc["Destination"] = original_data.sum()

    while normalized_error > tolerance:
        # Calculate the current row sums
        current_row_sums = np.sum(original_matrix, axis=1)

        # Calculate the scaling factors for rows
        row_scaling_factors = future_row_sums / current_row_sums

        # Scale the original matrix based on row factors
        scaled_matrix = row_scaling_factors[:, np.newaxis] * original_matrix

        # Calculate the column sums of the scaled matrix
        scaled_col_sums = np.sum(scaled_matrix, axis=0)

        # Calculate the scaling factors for columns
        col_scaling_factors = future_col_sums / scaled_col_sums

        # Scale the matrix again based on column factors
        final_scaled_matrix = col_scaling_factors * scaled_matrix

        # Calculate the final row and column sums
        final_col_sums = np.sum(final_scaled_matrix, axis=0)
        final_row_sums = np.sum(final_scaled_matrix, axis=1)

        # Calculate the error between desired and final sums
        error = np.sum(np.abs(final_col_sums - future_col_sums)) + np.sum(
            np.abs(final_row_sums - future_row_sums)
        )

        # Normalize the error by dividing it by the sum of desired row sums
        normalized_error = error / np.sum(future_row_sums)

        # Update the original matrix for the next iteration
        original_matrix = final_scaled_matrix

    # Get the size of the square matrix
    final_scaled_matrix_size = final_scaled_matrix.shape[0]

    # Generate column and row names
    final_scaled_column_names = [
        f"Zone {i}" for i in range(1, final_scaled_matrix_size + 1)
    ]

    # Convert the matrix into a DataFrame
    final_scaled_data = pd.DataFrame(
        final_scaled_matrix,
        columns=final_scaled_column_names,
        index=final_scaled_column_names,
    )

    # Add column sums
    final_scaled_data["Origin"] = final_scaled_data.sum(axis=1)

    # Add row sums
    final_scaled_data.loc["Destination"] = final_scaled_data.sum()

    final_scaled_data = final_scaled_data.round(3)

    # Set display options to show all columns and increase the width
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 100)

    # Display the final results
    print("Original OD Matrix:")
    print(original_data)
    print("\nFuture OD Matrix:")
    print(final_scaled_data)
    print("\nNormalized Error: {:.2%}".format(normalized_error))
