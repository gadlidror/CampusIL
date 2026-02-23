import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def _expect_assert(fn, *args):
  try:
    fn(*args)
  except AssertionError:
    return True
  return False
