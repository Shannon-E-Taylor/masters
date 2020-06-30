## This simulation corresponds to Simulation 10 in S2 Text (see also S10 Movie and Fig 2B)

# Import helper functions
from S1_File import *
from networks import *

#### NB! Duplicate of the one in networks.py
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
    print "yeet"
    return globals()[network_name]

def make_simulation(shift): 
  genelist = ["cad_cl", "opa_theornet_cl", 
  "hairy_theornet_cl", "eve_theornet_cl", 
  "run_cl", "ftz_cl", "odd_cl", "prd_cl", "slp_cl", "en_cl"]

  color_dict = {
        "cad":'orange',
        "D": "black",
        "opa":'darkslategray',
        "eve":'red',
        "run":'green',
        "ftz": 'darkorange',
        "odd":'blue',
        "hairy":'gold',
        "prd": 'purple',
        "slp": 'deepskyblue',
        "en": 'brown'} 

  initialize_network("pr_system", genelist)

  # Initialise tissue (label, num cells, network)
  embryo = Tissue("embryo", 20, pr_system)
        
  embryo.set_colors(color_dict)

  # Set synthesis and decay time delays (gene name, s, d)
  embryo.set_uniform_delays(6,6)
  embryo.set_delays("cad", 6, 156) # decays after t=144 ie simultaneous like 
  embryo.set_delays("hairy", 30, 18)
  embryo.set_delays("opa", 18, 6)
  #embryo.set_delays("eve", 6, 140)


  # Set initial conditions (gene name, list of initial states)
  embryo.set_rna_state("hairy", [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1])
  embryo.set_rna_ages("hairy", [0, 6, 12, 18, 24, 0, 0, 0, 0, 6, 12, 18, 24, 0, 0, 0, 0, 6, 12, 18])
  embryo.set_protein_state("hairy", [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0])
  embryo.set_protein_ages("hairy", [0, 0, 0, 0, 0, 0, 6, 12, 0, 0, 0, 0, 0, 0, 6, 12, 0, 0, 0, 0])
  embryo.set_protein_state("cad", [1 for i in range(20)])

  title = "opa_decays/gap=" + str(shift)
  embryo.set_protein_ages("cad", [114-(i*shift) for i in range(20)])
  embryo.simulate(title, 500)
  embryo.animate(title, framedelay=100)

# make_simulation(1)
# make_simulation(2)
# make_simulation(3)
# make_simulation(4)
# make_simulation(5)
# make_simulation(6)
# make_simulation(8)
# make_simulation(24)
# make_simulation(0)
# make_simulation(48)
make_simulation(72)
make_simulation(96)