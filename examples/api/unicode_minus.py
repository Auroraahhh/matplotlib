"""
=============
Unicode minus
=============

You can use the proper typesetting `Unicode minus`__ or the ASCII hyphen for
minus, which some people prefer.  :rc:`axes.unicode_minus` controls the default
behavior.

__ https://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes

The default is to use the Unicode minus.
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
