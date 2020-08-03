from warp_image.thinplate.numpy import *

try:
    import torch
    import warp_image.thinplate.pytorch as torch
except ImportError:
    pass

__version__ = '1.0.0'
