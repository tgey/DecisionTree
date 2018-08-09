#!/usr/bin/python3

import pandas as pd

def LoadDatas(Symbole):
	"""Load data from CSV

	Arguments:
		Symbole {str} -- the coin's pair to load

	Returns:
		Dataframe -- Coin's data from csv
	"""


	arr = pd.read_csv(Symbole + ".csv")
	return arr
