def function_with_uncommon_error(x):
    if x == 0:
        return float('inf') # Return positive infinity instead of causing an error
    else:
        return x + 1