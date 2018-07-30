#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt
from matplotlib import interactive
import matplotlib.gridspec as gridspec

def display_indica(coin):
    fig1 = plt.figure(1)
    spec1 = gridspec.GridSpec(ncols=2, nrows=2)

    f1_ax1 = fig1.add_subplot(spec1[0, :])
    f1_ax2 = fig1.add_subplot(spec1[1, :])

    f1_ax1.plot([float(i) for i in coin.indicators.data['Close']] , label='Close')
    f1_ax1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
    f1_ax1.plot([float(i) for i in coin.indicators.predicted] , label='Predited', color='tab:red')
    f1_ax1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    f1_ax2.plot([float(i) for i in coin.indicators.rsi],
                label='RSI', color='k')
    f1_ax2.axhline(y = 30)
    f1_ax2.axhline(y = 70)
    f1_ax2.fill_between(range(0, len(coin.indicators.rsi)), 0, 30, facecolor='lightsalmon')
    f1_ax2.fill_between(range(0, len(coin.indicators.rsi)), 70, 100, facecolor='lightgreen')
    f1_ax2.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)


    fig3 = plt.figure(2)
    spec3 = gridspec.GridSpec(ncols=2, nrows=2)
    f3_ax1 = fig3.add_subplot(spec3[0, :])
    f3_ax4 = fig3.add_subplot(spec3[1, :])
    fig3.tight_layout()

    bollup = [float(i) for i in coin.indicators.bollup]
    bolllow = [float(i) for i in coin.indicators.bolllow]

    f3_ax1.fill_between(range(0, len(bolllow)), bolllow, bollup, color='b', alpha=0.2)
    f3_ax1.plot([float(i) for i in coin.indicators.bollmid],
                label='BBand Middle', color='tab:red')
    f3_ax1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    f3_ax1.plot([float(i) for i in coin.indicators.data['Close']],
                label='Price', color='k')
    f3_ax1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    f3_ax4.plot([float(i) for i in coin.indicators.mfi],
                label='MFI', color='tab:red')
    f3_ax4.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)



    fig4 = plt.figure(3)
    spec4 = gridspec.GridSpec(ncols=2, nrows=2)
    f4_ax1 = fig4.add_subplot(spec4[0, :])
    f4_ax4 = fig4.add_subplot(spec4[1, :])
    fig4.tight_layout()

    f4_ax1.plot([float(i) for i in coin.indicators.cci],
                label='CCI', color='k')
    f4_ax1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    f4_ax4.plot([float(i) for i in coin.indicators.slowd],
                label='slowd', color='tab:red')
    f4_ax4.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    f4_ax4.plot([float(i) for i in coin.indicators.slowk],
                label='slowk', color='tab:green')
    f4_ax4.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    plt.figure(4)
    plt.plot([float(i) for i in coin.indicators.macd], label='MACD')
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    plt.plot([float(i) for i in coin.indicators.macdsignal],
                label='MACD Signal', color='tab:red')
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    plt.plot([float(i) for i in coin.indicators.macdhist],
                label='MACD Hist', color='tab:green')
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
    plt.show()
