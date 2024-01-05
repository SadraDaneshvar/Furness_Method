## Developed by Sadra Daneshvar
### Updated: Jan 05, 2024

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def Furness(original_matrix, future_row_sums, future_col_sums, tolerance=0.01):
    normalized_error = 1.1  # Initial error value greater than the tolerance
    original_matrix_size = original_matrix.shape[0]
    original_column_names = [f"Zone {i}" for i in range(1, original_matrix_size + 1)]

    original_data = pd.DataFrame(
        original_matrix, columns=original_column_names, index=original_column_names
    )

    original_data["Origin"] = original_data.sum(axis=1)
    original_data.loc["Destination"] = original_data.sum()

    error_list = []  # List to store errors for each iteration

    while normalized_error > tolerance:
        current_row_sums = np.sum(original_matrix, axis=1)
        row_scaling_factors = future_row_sums / current_row_sums
        scaled_matrix = row_scaling_factors[:, np.newaxis] * original_matrix

        scaled_col_sums = np.sum(scaled_matrix, axis=0)
        col_scaling_factors = future_col_sums / scaled_col_sums
        final_scaled_matrix = col_scaling_factors * scaled_matrix

        final_col_sums = np.sum(final_scaled_matrix, axis=0)
        final_row_sums = np.sum(final_scaled_matrix, axis=1)

        error = np.sum(np.abs(final_col_sums - future_col_sums)) + np.sum(
            np.abs(final_row_sums - future_row_sums)
        )
        normalized_error = error / np.sum(future_row_sums)

        error_list.append(normalized_error)  # Append current error to the list

        original_matrix = final_scaled_matrix

    final_scaled_matrix_size = final_scaled_matrix.shape[0]
    final_scaled_column_names = [f"Zone {i}" for i in range(1, final_scaled_matrix_size + 1)]

    final_scaled_data = pd.DataFrame(
        final_scaled_matrix,
        columns=final_scaled_column_names,
        index=final_scaled_column_names,
    )

    final_scaled_data["Origin"] = final_scaled_data.sum(axis=1)
    final_scaled_data.loc["Destination"] = final_scaled_data.sum()
    final_scaled_data = final_scaled_data.round(3)

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 100)

    print("Original OD Matrix:")
    print(original_data)
    print("\nFuture OD Matrix:")
    print(final_scaled_data)
    print("\nNormalized Error: {:.5%}".format(normalized_error))


    def plot_errors(error_list):
        plt.figure(figsize=(10, 6))
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams["font.size"] = 12
        iterations = range(1, len(error_list) + 1)
        plt.plot(iterations, error_list, marker='o')
        plt.title('Error Over Iterations', fontname='Times New Roman', fontsize=16, fontweight='bold')
        plt.xlabel('Iteration', fontname='Times New Roman', fontsize=14, fontweight='bold')
        plt.ylabel('Normalized Error', fontname='Times New Roman', fontsize=14, fontweight='bold', labelpad=10)
        plt.xticks(iterations)
        plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        plt.grid(True)
        plt.show()

    plot_errors(error_list)
