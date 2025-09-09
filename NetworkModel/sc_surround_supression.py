# Copyright 2023 Arvind Kumar @ KTH Stokholm, Sweden
# The MIT License
# Surround Supression in Superior Colliculous
#

"""
Script for NEST simulation of Locally Connected Random Network (LCRN)
with Excitatory and Inhibitory spiking neurons. 

There are 12800 neuron. 6400 Exc. and 6400 Inh.
Neurons are arranged on a uniform grid. 
Neurons are connected in a distance dependent manner. 
Connection probability decreases in a Gaussian fashion. 
The square grid is folded to form a torus to ensure that all neurons have same number of inputs and there are no boundary effects.

Neurons are driven by Poisson input. 
Input corresponding to the stimulus is also provided as additional Poisson input to selected neurons
"""


## Usual Python Prelims
import sys
import numpy as np
import nest
import pylab as pl
import matplotlib.pyplot as plt

# Import a functions to connect the neurons in a Gaussian fashion
import lib.lcrn_network as lcrn


# Neuron Parameters
neuron_params = {
    "C_m": 200.0,
    "E_L": -70.0,
    "g_L": 20.,
    "t_ref": 2.0,
    "tau_minus": 20.0,
    "tau_syn_ex": 1.0,
    "tau_syn_in": 3.0,
    "V_reset": -70.0,
    "V_th": -55.0,
}

# Neuron arrangement
nrowE, ncolE = 80, 80
nrowI, ncolI = 80, 80

# Total number of neurons
npopE = nrowE * ncolE
npopI = nrowI * ncolI

# Stimulus center and surround
# Center region is a cricle at the center of the square. Surround a square around the circle

# Stimulation center-- get the neurons ids that are in the center
center_region = 1
cen_x = 30
cen_y = 30
cen_width = 20
cen_radius = int(cen_width/2)

tmp_id_exc = np.repeat(1,cen_width**2)
nn = -1
if center_region ==1: # If it is circular
    for ii in range(cen_width):
        for jj in range(cen_width):
            x1 = (cen_x+ii)
            y1 = (cen_y+jj)
            dd = np.sqrt((x1-40)**2 + (y1-40)**2)
            if dd<=cen_radius:
                nn=nn+1
                tmp_id_exc[nn] = int((cen_x+ii)*nrowE + (cen_y+jj))

cen_id_exc = tmp_id_exc[:nn]

if center_region ==0: # If it is square
    cen_id_exc = np.repeat(1,cen_width**2)
    for ii in range(cen_width):
        for jj in range(cen_width):
            nn=nn+1
            cen_id_exc[nn] = int((cen_x+ii)*nrowE + (cen_y+jj))


cen_id_inh = cen_id_exc + npopE

# Stimulation surround -- get the neurons ids that are in the surround
sur_x = 10
sur_y = 10
sur_width = 60
tmp_id_exc = np.repeat(1,sur_width**2)
nn = -1
for ii in range(sur_width):
    for jj in range(sur_width):
        nn=nn+1
        tmp_id_exc[nn] = int((sur_x+ii)*nrowE + (sur_y+jj))

kk = np.isin(tmp_id_exc,cen_id_exc)
kk = ~np.array(kk)
surround_exc = tmp_id_exc[kk]
surround_inh = surround_exc+npopE

# Connection prob. from data
cee = 0.3
cei = 0.25
cie = 0.7
cii = 0.75

"""
Synaptic strengths
"""
p = 0.05        # Connection probability
stdE = 8        # std of the Gaussian that describes the distance dependent fall of E->E and E->I connections    
stdI = 12       # std of the Gaussian that describes the distance dependent fall of I->I and I->E connections
Jex = 0.75      # Strength of Excitatory synapses from outside -- see the manuscript for the measning of these values
Jin = -1.       # Strength of Excitatory synapses from outside -- see the manuscript for the measning of these values
g = 4.0


surr_rate = 220.    # Rate of Poisson process to mimic surround stimulation

std_inh = [8, 10, 12] # STD of I->I and I->E was varied

# External inputs -- to excitatory and inhibitory neurons. Both pops may receive different amount input
ei_input = [[5200.,2500.]]

# External input weighs
syn_specE = {'weight': Jex}
syn_specEx = {'weight': 2. * Jex}
syn_specIx = {'weight': 2. * Jin}

syn_specEE = {'weight': .20 * Jex}
syn_specEI = {'weight': .20 * Jex}
syn_specII = {'weight': .20 * Jin}
syn_specIE = {'weight': .35 * Jin}


# Recurrent weights that were varied
jee = [0.1, 0.8]
jei = [0.75, 1.0, 1.25, 1.5, 1.75]
jie = [0.7, 0.8, 0.9, 1.0, 1.1]

# strength of stimulus inputs
syn_spec_stim_spk = {'weight': 120. * Jex} # with no background input it gives 90% reponse
syn_spec_stim_poi = {'weight': 25. * Jex} # with no background it give a rate of ~1Hz 

no_stim = 20        # Number of times the stimulus was repeated
pp_std = 1.         # Cenyter input was a Pulse Packet with std 1.ms

for a1 in range(len(jee)):
    for a2 in range(len(jie)):
        for a3 in range(len(jei)):

            # External Input
            nu_exc = ei_input[0][0]
            nu_inh = ei_input[0][1]

            # Synapses in the format NEST needs
            syn_specEE = {'weight': jee[a1] * Jex,'delay':0.2}
            syn_specEI = {'weight': jei[a3] * Jex,'delay':0.1}
            syn_specII = {'weight': 0.50 * Jin,'delay':0.1}
            syn_specIE = {'weight': jie[a2] * Jin,'delay':0.1}
            
            # File Name
            output_file = 'XCent_Surr_Jee_'+str(jee[a1]) + '_Jie_' + str(jie[a2]) + '_Jei_' + str(jei[a3])
            
            # NEST Reset
            np.random.seed(0)
            nest.ResetKernel()
            nest.SetKernelStatus({
                'local_num_threads': 4,
                'resolution': 0.1,
                'data_path': './data_slow_input_strong',
                'overwrite_files': True,
            })

            # Multimeter -- to record synaptic conduactances
            multimeter = nest.Create('multimeter', params = {'withtime': True,
                'interval': 0.1,
                'to_file':   True,
                'to_memory': False,
                'label':     output_file,
                'record_from': ['V_m','g_ex','g_in']})

            # Spike detector -- to record spikes
            sd = nest.Create('spike_detector', params={
                            'to_file':      True,
                            'to_memory':    False,
                            'label':        output_file,
            })

            #Create neurons -- both neuron types have same parameters
            popE = nest.Create("iaf_cond_exp", npopE, params=neuron_params)
            popI = nest.Create("iaf_cond_exp", npopI, params=neuron_params)
            pop = popE + popI

            # Distribute V_m -- neurons ahve a different initial mem. pot.
            V_m = np.random.normal(-65., 5., len(pop))
            V_m_all = [{'V_m': V_mi} for V_mi in V_m]
            nest.SetStatus(pop, V_m_all)
            
            # External Poisson Generator
            poi_e = nest.Create('poisson_generator',1,{'rate':nu_exc})
            poi_i = nest.Create('poisson_generator',1,{'rate':nu_inh})

            # Connect external inputs
            nest.Connect(poi_e,popE, syn_spec=syn_specEx)
            nest.Connect(poi_e,popI, syn_spec=syn_specEx)
            nest.Connect(poi_i,popE, syn_spec=syn_specIx)
            nest.Connect(poi_i,popI, syn_spec=syn_specIx)

            # Connect the neurons

            offsetE = popE[0]
            offsetI = popI[0]

            for idx in range(npopE):
                # E-> E
                source = idx, nrowE, ncolE, nrowE, ncolE, int(cee * npopE), stdE
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                nest.Connect([popE[idx]], (targets + offsetE).tolist(), syn_spec=syn_specEE)

                # E-> I
                source = idx, nrowE, ncolE, nrowI, ncolI, int(cei * npopI), stdI
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                nest.Connect([popE[idx]], (targets + offsetI).tolist(), syn_spec=syn_specEI)

            for idx in range(npopI):
                # I-> E
                source = idx, nrowI, ncolI, nrowE, ncolE, int(cie * npopE), stdE
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                nest.Connect([popI[idx]], (targets + offsetE).tolist(), syn_spec=syn_specIE)

                # E-> I
                source = idx, nrowI, ncolI, nrowI, ncolI, int(cii * npopI), stdI
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                nest.Connect([popI[idx]], (targets + offsetI).tolist(), syn_spec=syn_specII)

            # Stimulation -- Surround
            stim_poi_surround = nest.Create('poisson_generator',1,{'rate':surr_rate,'start':500000.,'stop':600000.})
            
            
            # add Center input as a pulse packet -- 
            # First collect the input spikes in a spike generator
            spk_gen = nest.Create('spike_generator',len(cen_id_exc)+len(cen_id_inh))
            pp_mean = np.zeros((1,no_stim*3))
            center_end = no_stim*100. + 100.
            pp_mean[0,0:no_stim] = np.arange(100.,center_end,100.)
            for hh in range(no_stim):
                ini = no_stim + hh*2            
                pp_mean[0,ini] = center_end + (250.*hh) + 100 # 1
                pp_mean[0,ini+1] = center_end + (250.*hh) + 205# 1

            for sg in range(len(spk_gen)):
                pp_sg = pp_mean + np.random.uniform(0,pp_std,(1,no_stim*3))
                pp_sg = np.round(pp_sg*10)/10
                nest.SetStatus([spk_gen[sg]],{'spike_times':pp_sg[0]})

            # NEST Device parrot_neuron was used to inject inputs at  specific times
            parrot_ex = nest.Create('parrot_neuron',len(cen_id_exc))
            parrot_in = nest.Create('parrot_neuron',len(cen_id_inh))

            # connect the pulse packet (spkgen --> parrot--> neuron) i.e. the center stimulus
            nest.Connect(spk_gen[0:len(cen_id_exc)],parrot_ex,{'rule': 'one_to_one'})
            nest.Connect(spk_gen[len(cen_id_exc):],parrot_in,{'rule': 'one_to_one'})
            nest.Connect(parrot_ex,cen_id_exc.tolist(),{'rule': 'one_to_one'},syn_spec=syn_spec_stim_spk)
            nest.Connect(parrot_in,cen_id_inh.tolist(),{'rule': 'one_to_one'},syn_spec=syn_spec_stim_spk)

            # Connect the surround inputs
            nest.Connect(stim_poi_surround,surround_exc.tolist(),syn_spec=syn_spec_stim_poi)
            nest.Connect(stim_poi_surround,surround_inh.tolist(),syn_spec=syn_spec_stim_poi)

            # Connect spike detector to population of all neurons
            nest.Connect(pop, sd)
            nest.SetStatus([popE[cen_id_exc[200]]], {'V_th':1e3})
            nest.Connect(multimeter,[popE[cen_id_exc[200]]])

            #Start simulation

            # warm up the network
            wuptime = center_end # for the center stimulation only
            nest.Simulate(wuptime)

            # Now do multiple trials of surround
            
            for ii in range(no_stim):
                print(ii)
                ini = center_end + ii*250.
                fin = ini + 200.
                nest.SetStatus(stim_poi_surround,{'start':ini,'stop':fin})
                print('ini', str(ini), 'fin', str(fin), 'spk1', str(ini+100), 'spk2', str(fin))
                nest.Simulate(250.) # inter stimulation internal 
            nest.Simulate(100.)
