# Stock Tracker Project
# Author: Edward Zhang
# I don't know what this does yet

# Import Packages

import numpy as np
import pandas as pd
import pyfolio as pf

stock_rets = pf.utils.get_symbol_rets('FB')
pf.create_returns_tear_sheet(stock_rets, live_start_date='2015-12-1')
