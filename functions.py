import numpy as np

""" 
    Returns an asset's price after the asset return is applied to it.

    Args:
        assetPrice (double): Price of the asset.
        returnValue (double): Return of the asset.

    Returns:
        double: The asset's price after the asset return is applied to it.
"""

def assetValue(assetPrice, returnValue):
    return assetPrice * (1 + returnValue)


# Function that generates a random number between -1 and 1
# to mimick the return on assets based on a probability distribution

""" 
    Generates a random number between -1 and 1 to mimick the return on assets based 
    on a probability distribution.

    Args:
        standardDeviation (double): The standard deviation of our probability distribution.
        mean (double): The mean of your probability distribtuion.

    Returns:
        double: A number between -1 and 1 based on a probability distribution
"""
def assetReturn(standardDeviation, mean):
    

    return 0
