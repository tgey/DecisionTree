#!/usr/bin/python

import pandas as pd

def LoadDatas(Symbole):
	arr = pd.read_csv(Symbole + ".csv")
	return arr
