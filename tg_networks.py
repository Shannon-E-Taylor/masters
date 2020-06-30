# Define control logic functions for each gene

from S1_File import *


cad = Gene("cad")
D = Gene("D")
opa = Gene("opa")
eve = Gene("eve")
odd = Gene("odd")
run = Gene("run")
hairy = Gene("hairy")
ftz = Gene("ftz")
prd = Gene("prd")
slp = Gene("slp")
en = Gene("en")


def cad_cl(s):
    return 0

def D_cl(s): 
    return 1

def opa_cl(s):
    if s["cad"]==1: 
        return 0
    else: 
        return 1

def eve_cl(s):
    if s["D"] == 1:
        if s["odd"] == 1 or s["run"] == 1:
            return 0
        else:
            return 1
    else:
        if s["run"] == 1:
            return 0
        elif s["odd"] == 1:
            return 0
        elif s["slp"] == 1 and s["eve"] == 0:
            return 0
        elif s["en"] == 1:
            return 0
        else:
            return 1

def run_cl(s):
    if s["D"] == 1:
        if s["odd"] == 1:
            return 0
        elif s["hairy"]==1:
            return 0
        else:
            return 1
    else:
        if s["eve"] == 1 and s["run"] == 0:
            return 0
        elif s["odd"] == 1 and s["run"] == 0:
            return 0
        elif s["en"] == 1:
            return 0
        else:
            return 1

def ftz_cl(s):
    if s["slp"] == 1:
        return 0
    elif s["D"] == 1:
        if s["hairy"] == 1:
            return 0
        elif s["eve"] == 1:
            return 0
        else:
            return 1
    else:
        if s["ftz"] == 1:
            return 1
        else:
            return 0

def odd_cl(s):
    if s["slp"] == 1:
        return 0
    elif s["D"] == 1:
        if s["eve"] == 1:
            return 0
        elif s["hairy"] == 1:
            return 0
        else:
            return 1
    else:
        if s["run"] == 1:
            return 0
        elif s["prd"] == 1 and s["odd"] == 0:
            return 0
        elif s["en"] == 1:
            return 0
        else:
            return 1

def hairy_cl(s):
    if s["eve"] == 1: 
        return 0 #add repression by eve: no empirical evidence for this!
    if s["cad"] == 1: 
        if s["hairy"] == 1: 
            return 0 
        else: 
            return 1
    elif s["opa"] == 1: 
        return 0
    else:
        if s["hairy"] == 1: 
            return 1
        else: 
            return 0

def prd_cl(s):
    if s["cad"] == 1 or s["D"] == 1:
        return 0
    elif s["D"] == 1:
            if s["eve"] == 1:
                return 0
            else:
                return 1
    else:
        if s["odd"] == 1:
            return 0
        elif s["prd"] == 1:
            return 1
        else:
            return 0
    

def slp_cl(s):
    if s["cad"] == 1 or s["D"] == 1:
        return 0
    elif s["eve"] == 1:
        return 0
    elif s["D"] == 1:
        if s["prd"] == 0:
            return 0
        elif s["run"] == 1:
            return 0
        else:
            return 1
    else:
        if s["ftz"] == 1 and s["slp"] == 0:
            return 0
        elif s["en"] == 1:
            return 0
        elif s["odd"] == 1 and s["slp"] == 0:
            return 0
        else:
            return 1

def en_cl(s):
    if s["D"] == 1 or s["cad"] == 1:
        return 0
    else:
        if s["odd"] == 1:
            return 0
        elif s["slp"] == 1:
            return 0
        elif s["ftz"] == 1:
            return 1
        elif s["prd"] == 1 and s["run"] == 0:
            return 1
        else:
            return 0