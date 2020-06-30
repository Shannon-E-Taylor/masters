from S1_File import *

#########
#NETWORK#
#########


# Initialise each gene in network
g1 = Gene("g1")
g2 = Gene("g2")
cad = Gene("cad")
opa = Gene("opa")
eve = Gene("eve")
odd = Gene("odd")
run = Gene("run")
hairy = Gene("hairy")
ftz = Gene("ftz")
prd = Gene("prd")
slp = Gene("slp")
en = Gene("en")
color_dict = {"g1":'black',
          "g2":'black',
          "cad":'orange',
          "opa":'darkslategray',
          "eve":'red',
          "run":'green',
          "ftz": 'darkorange',
          "odd":'blue',
          "hairy":'gold',
          "prd": 'purple',
          "slp": 'deepskyblue',
          "en": 'brown'} 



# Define control logic functions for each gene
def g1_cl(s):
    if s["g1"] == 1 or s["opa"] == 1:
        return 0
    else:
        return 1

def g2_cl(s):
    if s["g2"] == 1 or s["opa"] == 1:
        return 0
    else:
        return 1

def g1_theornet_cl(s): 
    return 0

def g2_theornet_cl(s): 
    return 0

def cad_cl(s):
    return 0


def opa_cl(s):
    return 1

def opa_theornet_cl(s):
    if s["cad"]==1: 
        return 0
    else: 
        return 1

#regulation of eve in Drosophila
def eve_drosnet_cl(s):
    if s["opa"] == 0:
        if s["g2"] == 1:
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



#regulation of eve in theoretical network 
#CHANGES: repression by runt and odd
def eve_theornet_cl(s):
    if s["opa"] == 0:
        if s["run"] == 1 or s["odd"] == 1:
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
    if s["opa"] == 0:
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
    elif s["opa"] == 0:
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
    elif s["opa"] == 0:
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

#regulation of hairy in Drosophila 
def hairy_drosnet_cl(s):
    if s["opa"] == 0 and s["g1"] == 0:
        return 1
    else:
        return 0

#regulation of hairy in Drosophila
#CHANGE: hairy autorepression
def hairy_theornet_cl(s): 
    if s["opa"] == 0 and s["hairy"]==0:
        return 1
    else:
        return 0

def prd_cl(s):
    if s["cad"] == 1:
        return 0
    elif s["opa"] == 0:
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
    if s["cad"] == 1:
        return 0
    elif s["eve"] == 1:
        return 0
    elif s["opa"] == 0:
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
    if s["opa"] == 0:
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


# no gap control logic for eve: should over write other stuff 
def eve_drosnet2_cl(s):
    if s["opa"] == 0:
        if s["odd"] or s["run"] ==1: 
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



###########
#FUNCTIONS#
###########

def initialize_network(network_name, genelist): 
    # Initialise gene network
    globals()[network_name] = Network()
    for i in genelist: 
        # Assign control logic functions to each gene
        gene_name = i.split("_")[0]
        globals()[gene_name].control_logic=globals()[i]
        # Add genes to network
        globals()[network_name].add_gene(globals()[gene_name])
    # Update network (calculates state spaces etc)
    globals()[network_name].update()
    return globals()[network_name]


##################
# RUN DROS MODEL #
##################


# def run_wt_dros(title): 
#     global embryo 
#     #gene_init()
    # dros_network_genelist = ["g1_cl", "g2_cl", "cad_cl", "opa_cl", 
    # "hairy_drosnet_cl", "eve_drosnet_cl", 
    # "run_cl", "ftz_cl", "odd_cl", "prd_cl", "slp_cl", "en_cl"]
    # color_dict = {"g1":'black',
    #       "g2":'black',
    #       "cad":'orange',
    #       "opa":'darkslategray',
    #       "eve":'red',
    #       "run":'green',
    #       "ftz": 'darkorange',
    #       "odd":'blue',
    #       "hairy":'gold',
    #       "prd": 'purple',
    #       "slp": 'deepskyblue',
    #       "en": 'brown'} 
    # initialize_network("pr_system_dros", dros_network_genelist)

    # embryo = Tissue("embryo", 20, pr_system_dros)

    # # Choose gene colors          
    # embryo.set_colors(color_dict)

    # # Set synthesis and decay time delays (gene name, s, d)
    # embryo.set_uniform_delays(6,6)
    # embryo.set_delays("g1", 18, 30)
    # embryo.set_delays("g2", 18, 30)
    # embryo.set_delays("cad", 6, 24)
    # embryo.set_delays("opa", 36, 6)

    # # Set initial conditions (gene name, list of initial states)
    # embryo.set_protein_state("cad", [1 for i in range(20)])
    # embryo.set_protein_state("g1", [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1])
    # embryo.set_rna_state("g1", [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0])
    # embryo.set_rna_ages("g1", [0, 6, 12, 0, 0, 0, 0, 0, 0, 6, 12, 0, 0, 0, 0, 0, 0, 6, 12, 0])
    # embryo.set_protein_ages("g1", [0, 0, 0, 0, 6, 12, 18, 24, 0, 0, 0, 0, 6, 12, 18, 24, 0, 0, 0, 0])
    # embryo.set_protein_state("g2", [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0])
    # embryo.set_rna_state("g2", [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1])
    # embryo.set_rna_ages("g2", [0, 0, 0, 6, 12, 0, 0, 0, 0, 0, 0, 6, 12, 0, 0, 0, 0, 0, 0, 6])
    # embryo.set_protein_ages("g2", [18, 24, 0, 0, 0, 0, 6, 12, 18, 24, 0, 0, 0, 0, 6, 12, 18, 24, 0, 0])

    # # Run and visualise simulation
    # embryo.simulate(title, 80)
    # embryo.animate(title, framedelay=100)
    
