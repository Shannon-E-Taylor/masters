
# Import helper functions
from S1_File import *
from networks import *

import pandas as pd 

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


#def make_simulation(shift): 
genelist = ["cad_cl", "opa_theornet_cl", 
"hairy_theornet_cl", "eve_theornet_cl", 
"run_cl", "ftz_cl", "odd_cl", "prd_cl", "slp_cl", "en_cl"]



################
# SIMULATION 2 #
################

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

nsegments = 2
opashift = 6
uniform_delay = 6


def make_simulation(shift):
	# Initialise tissue (label, num cells, network)
	embryo = Tissue("embryo", 16*nsegments, pr_system)

	embryo.set_colors(color_dict)

	# Set synthesis and decay time delays (gene name, s, d)
	embryo.set_uniform_delays(uniform_delay,uniform_delay)
	embryo.set_delays("cad", uniform_delay, 144) # decays after t=144 ie simultaneous like 
	embryo.set_delays("hairy", 30, 18)
	embryo.set_delays("opa", 18, uniform_delay)
	#embryo.set_delays("eve", 6, 140)


	# Set initial conditions (gene name, list of initial states)
	embryo.set_rna_state("hairy", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]*nsegments)
	embryo.set_rna_ages("hairy", ([(i*3) for i in range(10)] + [0] * 6)*nsegments)

	embryo.set_protein_state("hairy", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]*nsegments)
	embryo.set_protein_ages("hairy", ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + [(i*3) for i in range(6)])*nsegments)



	embryo.set_protein_state("cad", [1 for i in range(nsegments*16)])
	embryo.set_protein_ages("cad", [114-(i*shift) for i in range(nsegments*16)]) 
	#18 = uniform_delay * n_extra_cell

	title = "BIG_stripes/synth6_h3_opa"+str(shift)
	embryo.simulate(title, 250)
	embryo.animate(title, framedelay=100)

for i in range(12): 
	make_simulation(i)

make_simulation(15)
make_simulation(18)

make_simulation(24)
make_simulation(0)

shift = 3 
nsegments = 2

inputs = {
	"hairy RNA state": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]*nsegments,
	"hairy RNA ages": ([(i*3) for i in range(10)] + [0] * 6)*nsegments,
	"hairy protein state": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]*nsegments,
	"hairy protein ages":  ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + [(i*3) for i in range(6)])*nsegments, 
	"cad protein stage": [1 for i in range(nsegments*16)], 
	"cad protein ages": [114-(i*shift) for i in range(nsegments*16)]

}



inputtable = pd.DataFrame(inputs, columns = inputs.keys())
inputtable = inputtable.transpose() 
print(inputtable.to_latex(bold_rows = True))
