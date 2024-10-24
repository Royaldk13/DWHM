import pandas as pd
import numpy as np

# Given time (x) and mass (y) data
df = pd.DataFrame({
    'X': [5, 7, 12, 16, 20],
    'Y': [40, 120, 180, 210, 240]
})

# Mean of X and Y
mean_X = df['X'].mean()
mean_Y = df['Y'].mean()

# Initialize new columns for intermediate calculations
df['a'] = df['X'] - mean_X  # a = X - mean_X
df['b'] = df['Y'] - mean_Y  # b = Y - mean_Y
df['a*b'] = df['a'] * df['b']  # a*b
df['a^2'] = df['a'] * df['a']  # a^2

# Calculate the sum of a*b and a^2
sum_ab = df['a*b'].sum()
sum_aa = df['a^2'].sum()

# Compute slope (w1) and intercept (w0) for the linear regression line
w1 = sum_ab / sum_aa
w0 = mean_Y - (w1 * mean_X)

# Prediction for x = 27
x = 27
y_pred = w0 + w1 * x

# Output the estimated value of y
print(f"Estimated value of y for x={x} seconds is {y_pred} grams.")
