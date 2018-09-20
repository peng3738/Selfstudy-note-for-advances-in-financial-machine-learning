def binFreq(sl,pt,p,tSR):
    '''
Given  a trading rule characterized by the parameters{sl,pt,freq},
what's the number of bets/year needed to achieve a Sharpe ratio
tSR with precision rate p?
Note: Equation with radicals,check for extraneous solution.
1)Inputs
sl:stop loss threshold
pt:profit taking threshold
p:precision rate p
tSR:target annual Sharpe ratio
2)Output
freq:number of bets per year needed
'''
    freq=(tSR*(pt-sl))**2*p*(1-p)/((pt-sl)*p+sl)**2 # possible extraneous
    if not np.isclose(binSR(s1,pt,freq,p),tSR):return
    return freq
