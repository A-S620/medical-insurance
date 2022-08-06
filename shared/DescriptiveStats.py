import numpy as np


def create_stats(column_name, column):
    column_range = column.max() - column.min()
    q3, q2 = np.percentile(column, [75, 25])
    column_iqr = q3 - q2
    return {
        column_name: {
            'mean': column.mean(),
            'median': column.median(),
            'mode': column.mode(),
            'range': column_range,
            'IQR': column_iqr,
            'std': np.std(column),
            'var': np.var(column)
        }
    }
