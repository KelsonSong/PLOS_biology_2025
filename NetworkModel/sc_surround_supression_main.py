# -*- coding: utf-8 -*-
# Copyright 2025 Arvind Kumar @ KTH Stokholm, Sweden
# The MIT License
# Surround Supression in Superior Colliculous
#
# The MIT License

# RUNS WITH NEST 3.4
# Script for NEST simulation of Locally Connected Random Network (LCRN)
# with Excitatory and Inhibitory spiking neurons. 

# There are 12800 neuron. 6400 Exc. and 6400 Inh.
# Neurons are arranged on a uniform grid. 
# Neurons are connected in a distance dependent manner. 
# Connection probability decreases in a Gaussian fashion. 
# The square grid is folded to form a torus to ensure that all neurons have same number of inputs and there are no boundary effects.

# Neurons are driven by Poisson input. 
# Input corresponding to the stimulus is also provided as additional Poisson input to selected neurons

# In this script we change the recurrent connections to study the effect of local connectivity
# in particular we vary Exc to Exc, Exc to Inh and Inh to Exc connections. 
# File names carry the weight information used. 
# Membrane potential and synaptic conductances are recorded in one file and spike in a seprate
# Both types of file have same initial prefix.

from operator import le
import sys
import numpy as np
import nest
import pylab as pl
import matplotlib.pyplot as plt

import lib.lcrn_network as lcrn

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

nrowE, ncolE = 80, 80
nrowI, ncolI = 80, 80

npopE = nrowE * ncolE
npopI = nrowI * ncolI

# Stimulus center and surround
# Stimulation center
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

# Stimulation surround
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

"""
Synaptic strengths
"""
p = 0.05                    # 0.05 - 0.1
stdE = 8
stdI = 12                   # 9 - 11
shift = 0                   # 1 - 3
Jex = 1.
Jin = -1.                   # 4 - 8
g = 4.0

# Connection prob. from data
con_factor = 0.45
cee_base = 0.3*con_factor
cei = 0.25*con_factor
cie = 0.7*con_factor
cii = 0.75*con_factor


std_inh = [8, 10, 12]
std_inh = [10]

ei_input = [[1000.,600.]]

# External input weighs
syn_specE = {'weight': Jex}
syn_specExEx = {'weight': 1.6* Jex}
syn_specExIn = {'weight': 1.7* Jex}
syn_specIxEx = {'weight': 1.6 * Jin}
syn_specIxIn = {'weight': 1.8 * Jin}
syn_specIx = {'weight': 2. * Jin}


jee = [.25]
jie = [0.50, 0.6, 0.7, 0.8, 0.90, 1.0]
jei = [0.2, 0.4, 0.6, 0.8, 1.0]

# jee = [0.5]
# jie = [0.7]
# jei = [0.60]

surr_rate = 100. # surround rate

# strength of stimulus inputs
syn_spec_stim_spk_exc = {'weight': 22. * Jex} # with no background input it gives 90% reponse
syn_spec_stim_spk_inh = {'weight': 18. * Jex} # with no background input it gives 90% reponse


syn_spec_stim_poi = {'weight': 5. * Jex} # with no background it give a rate of ~1Hz 
no_trial = 20

def connect_multiple(pre: np.array, post: np.array, syn_weight, syn_delay):
    size = max(pre.size, post.size)

    if pre.size < post.size:
        pre = np.repeat(pre, size)  # [1,2] => [1,1,2,2]
    if pre.size > post.size:
        post = np.tile(post, size)  # [1,2] => [1,2,1,2]

    nest.Connect(pre, post, "one_to_one", syn_spec={"weight": np.full(size, syn_weight),"delay": np.full(size, syn_delay)})


# jee = [0.25]
# jie = [0.5]
# jei = [0.6]

for a1 in range(len(jee)):
    for a2 in range(len(jie)):
        for a3 in range(len(jei)):

            nu_exc = ei_input[0][0]
            nu_inh = ei_input[0][1]
            # syn_specEE = {'weight': jee[a1] * Jex, 'delay':1.} # exc to exc
            # syn_specEI = {'weight': jei[a3] * Jex, 'delay':1.} # exc to inh
            # syn_specII = {'weight': .20 * Jin, 'delay':1.} # inh to exc
            # syn_specIE = {'weight': jie[a2] * Jin, 'delay':1.} # inh to exc

            syn_specEE = jee[a1] * Jex * jee_factor[a4]# exc to exc
            syn_specEI = jei[a3] * Jex * jee_factor[a4]# exc to inh
            syn_specII = .20 * Jin # inh to inh
            syn_specIE = jie[a2] * Jin # inh to exc

            output_file = 'XCent_Surr_Jee_'+str(jee[a1]) + '_Jei_' + str(jei[a3]) + '_Jie_' + str(jie[a2])
            # output_file = 'test'
            np.random.seed(0)
            nest.ResetKernel()
            nest.SetKernelStatus({
                'local_num_threads': 4,
                'resolution': 0.1,
                'data_path': './data',
                'overwrite_files': True,
            })

            # Multimeter
            multimeter = nest.Create('multimeter', {'record_to':'ascii',
                'label':     output_file,'interval':0.1,
                'record_from': ['V_m','g_ex','g_in']})

            # Spike detector
            sd = nest.Create("spike_recorder",{'record_to':'ascii','label':output_file})

            #Create neurons
            popE = nest.Create("iaf_cond_alpha", npopE, params=neuron_params)
            popI = nest.Create("iaf_cond_alpha", npopI, params=neuron_params)
            pop = popE + popI
            popE_ids = np.array(popE)
            popI_ids = np.array(popI)

            # Distribute V_m
            V_m = np.random.normal(-65., 5., len(pop))
            V_m_all = [{'V_m': V_mi} for V_mi in V_m]
            nest.SetStatus(pop, V_m_all)
            V_m = np.random.normal(-55., 2., len(pop))
            V_m_all = [{'V_th': V_mi} for V_mi in V_m]
            nest.SetStatus(pop, V_m_all)
            
            # External Poisson Generator
            poi_e = nest.Create('poisson_generator',1,{'rate':nu_exc})
            poi_i = nest.Create('poisson_generator',1,{'rate':nu_inh})

            # Connect external inputs
            nest.Connect(poi_e,popE, syn_spec=syn_specExEx)
            nest.Connect(poi_e,popI, syn_spec=syn_specExIn)
            nest.Connect(poi_i,popE, syn_spec=syn_specIxEx)
            nest.Connect(poi_i,popI, syn_spec=syn_specIxIn)

            # Connect the neurons
            offsetE = popE[0]
            offsetI = popI[0]

            for idx in range(npopE):
                # E-> E
                source = idx, nrowE, ncolE, nrowE, ncolE, int(cee * npopE), stdE
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                # syn_specE = {'weight': Jx}
                connect_multiple(popE_ids[idx], popE_ids[targets],syn_specEE,1.)
                # nest.Connect([popE[idx]], (targets + offsetE).tolist(), syn_spec=syn_specEE)

                # E-> I
                source = idx, nrowE, ncolE, nrowI, ncolI, int(cei * npopI), stdI
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                connect_multiple(popE_ids[idx], popI_ids[targets],syn_specEI,1.)
                # nest.Connect([popE[idx]], (targets + offsetI).tolist(), syn_spec=syn_specEI)

            for idx in range(npopI):
                # I-> E
                source = idx, nrowI, ncolI, nrowE, ncolE, int(cie * npopE), stdE
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                connect_multiple(popI_ids[idx], popE_ids[targets],syn_specIE,1.)
                # nest.Connect([popI[idx]], (targets + offsetE).tolist(), syn_spec=syn_specIE)

                # E-> I
                source = idx, nrowI, ncolI, nrowI, ncolI, int(cii * npopI), stdI
                targets, delay = lcrn.lcrn_gauss_targets(*source)
                targets = targets[targets != idx]
                connect_multiple(popI_ids[idx], popI_ids[targets],syn_specII,1.)
                # nest.Connect([popI[idx]], (targets + offsetI).tolist(), syn_spec=syn_specII)


            [int(cee * npopE), int(cei * npopI), int(cie * npopE), int(cii * npopI)]
            # Stimulation
            # stim_poi_surround = nest.Create('poisson_generator',1,{'rate':surr_rate,'start':500000.,'stop':600000.})
            # spk_gen = nest.Create('spike_generator')
            # spk_time = np.zeros(no_trial)
            # spk_time[0:] = np.arange(100.,(no_trial+1)*100.,100.)
            # nest.SetStatus(spk_gen,{'spike_times':spk_time})

            stim_poi_surround = nest.Create('poisson_generator',no_trial,{'rate':surr_rate,'start':500000.,'stop':600000.})
            
            poi_surr_start_times = np.arange(2100,6900.,250.)
            poi_surr_stop_times = np.arange(2300,7100.,250.)
            stim_poi_surround = nest.Create('poisson_generator',no_trial,{'rate':surr_rate,'start':poi_surr_start_times,'stop':poi_surr_stop_times})
            
            spk_gen_time = np.zeros(len(poi_surr_start_times)*2+20)
            spk_gen_time[0:20] = np.arange(100.,(no_trial+1)*100.,100.)
            spk_gen_time[20:len(poi_surr_start_times)+20] = poi_surr_start_times+100.
            spk_gen_time[len(poi_surr_start_times)+20:] = poi_surr_stop_times+5.
            spk_gen_time.sort()
            spk_gen = nest.Create('spike_generator')
            nest.SetStatus(spk_gen,{'spike_times':spk_gen_time})
            

            parrot_ex = nest.Create('parrot_neuron',1)

            nest.Connect(spk_gen,parrot_ex)
            nest.Connect(parrot_ex,cen_id_exc.tolist(),syn_spec=syn_spec_stim_spk_exc)
            nest.Connect(parrot_ex,cen_id_inh.tolist(),syn_spec=syn_spec_stim_spk_inh)
            nest.Connect(stim_poi_surround,surround_exc.tolist(),syn_spec=syn_spec_stim_poi)
            nest.Connect(stim_poi_surround,surround_inh.tolist(),syn_spec=syn_spec_stim_poi)

            # Connect spike detector to population of all neurons
            nest.Connect(pop, sd)
            # nest.SetStatus([popE_ids[cen_id_exc[200]]], {'V_th':1e3})
            nest.Connect(multimeter,[popE_ids[cen_id_exc[200]]])

            # #Start simulation
            # wuptime = no_trial*100.+100. # for the center stimulation only
            # nest.Simulate(wuptime)


            # Now do multiple trials of surround
            # for ii in range(no_trial):
            #     print(ii)
            #     ini = wuptime + ii*250.
            #     fin = ini + 200.
            #     nest.SetStatus(stim_poi_surround,{'start':ini,'stop':fin})
            #     nest.SetStatus(spk_gen,{'spike_times':[ini+100., fin+5.]})
            #     print('ini', str(ini), 'fin', str(fin), 'spk1', str(ini+100), 'spk2', str(fin))
            #     nest.Simulate(250.)
            nest.Simulate(7200.)

