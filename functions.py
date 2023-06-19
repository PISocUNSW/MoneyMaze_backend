# Imported Libraries
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


#######################################################################################################################

""" 
    Generates a random number between -1 and 1 to mimick the return on assets based 
    on a probability distribution.

    Args:
        mean (double): The mean of the asset's return in the probability distribution.
        standardDeviation (double): The standard deviation of the asset's return in the probability distribution.

    Returns:
        double: A number between -1 and 1 based on a probability distribution
"""
def assetReturn(mean, standardDeviation):
    assetReturns = np.random.normal(mean, standardDeviation)
    return assetReturns

