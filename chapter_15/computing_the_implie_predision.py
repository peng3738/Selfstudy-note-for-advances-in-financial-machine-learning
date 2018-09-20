def binHR(sl,pt,freq,tSR):
    '''
Given a trading rule characterized by the parameters{sl,pt,freq},
what's the min precision p required to achieve a sharpe ratio tSR?
1)Inputs
sl: stop loss threshold
pt:profit taking threshold
freq:number of bets per year
tSR: target annual sharpe ratio
2)output
p: the min precision rate p required to achieve tSR
'''
    a=(freq+tSR**2)*(pt-sl)**2
    b=(2*freq*sl-tSR**2*(pt-sl))*(pt-sl)
    c=freq*sl**2
    p=(-b+(b**2-4*a*c)**.5)/(2.*a)
    return p
