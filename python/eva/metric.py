# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import numpy as _np

def valuation_mse(a,b):
    """ Calculate the total mean squared error between two valuations

        Parameters
        ----------
        a,b : dict from names to list of numbers
            Must have the same structure
        """
    if set(a.keys()) != set(b.keys()):
        raise ValueError("Valuations must have the same keys")
    mse = sum(_np.mean((_np.array(a[k]) - _np.array(b[k]))**2) for k in a.keys())
    return mse / len(a)
