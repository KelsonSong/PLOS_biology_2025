# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:16:21 2022

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter
import scipy.stats as st


#==================================================================================================================================

''' FILE PATHS FOR WHOLE COLLICULUS'''

# =============================================================================
# ipsi4935= 'C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/4935/Statistics for 4935 ipsi whole.csv'
# contra4935='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/4935/Statistics for 4935 contra whole.csv'
# 
# ipsi4954='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/4954/Statistics for 4954 ipsi.csv'
# contra4954='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/4954/Statistics for 4954 contra.csv'
# 
# ipsi4956='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/4956/Statistics for 4956 ipsi whole.csv'
# contra4956='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/4956/Statistics for 4956 contra whole.csv'
# 
# ipsi6287='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/6287/Statistics for 6287 ipsi whole.csv'
# contra6287='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/6287/Statistics for 6287 contra whole.csv'
# 
# ipsi6599='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/6599/Statistics for 6599 IPSI WHOLE.csv'
# contra6599='C:/Users/andre/OneDrive/Desktop/whole retina/retina/optimal/6599/Statistics for 6599 CONTRA WHOLE.csv'
# 
# ipsi6601='C:/Users/andre/OneDrive/Desktop/whole retina/retina/suboptimal/6601/Statistics for ipsi corr.csv'
# contra6601='C:/Users/andre/OneDrive/Desktop/whole retina/retina/suboptimal/6601/Statistics for contra.csv'
# 
# =============================================================================

def percentages(filename):
     
    
    ''' filename: the output file of the cell counter plug in of image j that contains smpling data from different regions (on and off) 
    
         returns a list of objects [all the data for vgat cells,all the data for vglut cells, the percentage of vgatcells in the area, the percentage of vglut cells in the area
                               ,the number of vgat cells in the area,the number of vglut cells in the area ]
    '''

    on_ipsi_6599= pd.read_csv(filename)   
       
    try:
        allvgat= on_ipsi_6599.loc[on_ipsi_6599['Type'] == 1]
    except:
        on_ipsi_6599= pd.read_csv(filename,sep=';')
        allvgat= on_ipsi_6599.loc[on_ipsi_6599['Type'] == 1]
    allvglut=on_ipsi_6599.loc[on_ipsi_6599['Type'] == 2]
    numvgat=len(allvgat)
    numvglut=len(allvglut)
    vgat_percentage= len(allvgat)/len (on_ipsi_6599['Type'])
    vglut_percentage=len(allvglut)/len (on_ipsi_6599['Type'])
    #return[allvgat,allvglut,vgat_percentage,vglut_percentage,numvgat,numvglut]
    return[vgat_percentage,vglut_percentage,numvgat,numvglut]



def gat_count(areas_list):
    
    areas_list_gat_counts= []
    for i in areas_list:
        areas_list_gat_counts.append(i[-2])
    return  areas_list_gat_counts




def glut_count(areas_list):
    
    areas_list_gat_counts= []
    for i in areas_list:
        areas_list_gat_counts.append(i[-1])
    return  areas_list_gat_counts
 
    
def pointzerofinderhelper(filepath1,filepath2,i):
    a=distance_finder([0,0,0], filepath1,i)
    b=distance_finder([0,0,0], filepath2,i)
    el_plotador(a,b)

#=========================================================================================================================================
''' fillepaths for gabafos counting results on off areas for experimentaal and controls'''



ipsi5123medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos1 ipsi medial.csv'))
ipsi5123medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 ipsi medial.csv'))
ipsi5123medial=ipsi5123medial1+ipsi5123medial2

contra5123medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos1 contr medial.csv'))
contra5123medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 contr medial.csv'))
contra5123medial=contra5123medial1+contra5123medial2

ipsi5123on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos1 ipsi on.csv'))
ipsi5123on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 ipsi on.csv'))
ipsi5123on=ipsi5123on1+ipsi5123on2

contra5123on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos1contra on.csv'))
contra5123on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 contra on.csv'))
contra5123on=contra5123on1+contra5123on2

ipsi5123lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results5123 gabafos1  latteral ipsi.csv'))
ipsi5123lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 ipsi LATTERAL.csv'))
ipsi5123lateral=ipsi5123lateral1+ipsi5123lateral2

contra5123lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/results 5123  gabafos1 latteral contra.csv'))
contra5123lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 contr LATERAl.csv'))
contra5123lateral=contra5123lateral1+contra5123lateral2
#=============================================================================================================================================
ipsi5124medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 ipsi medial.csv'))
ipsi5124medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2 ipsi medial.csv'))
ipsi5124medial=ipsi5124medial1+ipsi5124medial2


contra5124medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 contra medial.csv'))
contra5124medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2 contra MEDIAL.csv'))
contra5124medial=contra5124medial1+contra5124medial2

ipsi5124on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 ipsi on.csv'))
ispi5124on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2 ipsi on.csv'))
ipsi5124on=ipsi5124on1+ispi5124on2

contra5124on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 contra on.csv'))
contra5124on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2 contra on.csv'))
contra5124on=contra5124on1+contra5124on2

ipsi5124lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 ipsi lateral.csv'))
ipsi5124lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2IPSI lateral.csv'))
ipsi5124lateral=ipsi5124lateral1+ipsi5124lateral2

contra5124lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 contra lateral.csv'))
contra5124lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2 contra lateral.csv'))
contra5124lateral=contra5124lateral1+contra5124lateral2
#===================================================================================================================================================
ipsi5125medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1 ipsi medial.csv'))
ipsi5125medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos2 ipsi medial.csv'))
ipsi5125medial=ipsi5125medial1+ipsi5125medial2

contra5125medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1 contra medial.csv'))
contra5125medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos2 contra medial.csv'))
contra5125medial=contra5125medial1+contra5125medial2

ipsi5125on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1 ipsi on.csv'))
contra5125on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1 contra on.csv'))

ipsi5125lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1 ipsi lateral.csv'))
ipsi5125lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos2 ipsi lateral.csv'))
ipsi5125lateral=ipsi5125lateral1+ipsi5125lateral2

contra5125lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1contra lateral.csv'))
contra5125lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos2 contra lateral.csv'))
contra5125lateral=contra5125lateral1+contra5125lateral2
#=========================================================================================================================================
ipsi4935medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafosipsi medial.csv'))
ipsi4935medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 ipsi medial.csv'))
ipsi4935medial=ipsi4935medial1+ipsi4935medial2

contra4935medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/Results 4935 gaba fos1 contra medial.csv'))
contra4935medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 contra medial.csv'))
contra4935medial=contra4935medial1+contra4935medial2

ipsi4935on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafosipsi on.csv'))
ipsi4935on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 ipsi on.csv'))
ipsi4935on=ipsi4935on1+ipsi4935on2

contra4935on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos contra on.csv'))
contra4935on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 contra on.csv'))
contra4935on=contra4935on1+contra4935on2

ipsi4935lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/Results 4935 gaba fos1 ipsi lateral.csv'))
ipsi4935lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 ipsi lateral.csv'))
ipsi4935lateral=ipsi4935lateral1+ipsi4935lateral2

contra4935lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/Results 4935 gaba fos1 contra lateral.csv'))
contra4935lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 contra lateral.csv'))
contra4935lateral=contra4935lateral1+contra4935lateral2
#=========================================================================================================================================
ipsi4956medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gabafos1 ipsimediall.csv'))
ipsi4956medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gaba fos 2ipsi medial.csv'))
ipsi4956medial=ipsi4956medial1+ipsi4956medial2

contra4956medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/results 4956 gabafos1 contra medial.csv'))
contra4956medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gaba fos2 contra medial.csv'))
contra4956medial=contra4956medial1+contra4956medial2

ipsi4956on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results4956 gaba fos 1ipsi on.csv'))
ipsi4956on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/4956 gabafos2 ipsi on.csv'))
ipsi4956on=ipsi4956on1+ipsi4956on2

contra4956on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gabafos1 contra on.csv'))
contra4956on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gabafos2 contra on.csv'))
contra4956on=contra4956on1+contra4956on2

ipsi4956lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gabafos1 ipsi lateral.csv'))
ipsi4956lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gaba fos 2ipsi lateral.csv'))
ipsi4956lateral=ipsi4956lateral1+ipsi4956lateral2

contra4956lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Results gaba fos contra lateral.csv'))
contra4956lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4956/Resultsgabafos1 contra lateral.csv'))
contra4956lateral=contra4956lateral1+contra4956lateral2
#=========================================================================================================================================
ipsi4954medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 ipsi medial.csv'))
ipsi4954medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 ipsi medial.csv'))
ipsi4954medial=ipsi4954medial1+ipsi4954medial2

contra4954medial1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos1 contra mediall.csv'))
contra4954medial2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 contra mediall.csv'))
contra4954medial=contra4954medial1+contra4954medial2

ipsi4954on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos1 ipsi on.csv'))
ipsi4954on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 ipsi on.csv'))
ipsi4954on=ipsi4954on1+ipsi4954on2

contra4954on1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos1 contra on.csv'))
contra4954on2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 contra on.csv'))
contra4954on=contra4954on1+contra4954on2

ipsi4954lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos1 contra lateral.csv'))
ipsi4954lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 contra lateral.csv'))
ipsi4954lateral=ipsi4954lateral1+ipsi4954lateral2

contra4954lateral1=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos1 contra lateral.csv'))
contra4954lateral2=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 contra lateral.csv'))
contra4954lateral=contra4954lateral1+contra4954lateral2
#==========================================================================================
ipsi6599medial=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/Results ipsi medial pos neg.csv'))
ipsi6599latteral=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/latteral ipsi.csv'))
ipsi6599on=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/6599 Results 1_POS 2_NEG.csv'))
#=================================================================================================
'''lists of areas '''
ipsimedialcontrol=[ipsi5123medial,ipsi5124medial,ipsi5125medial]
ipsimedialexp=[ipsi4935medial,ipsi4956medial,ipsi4954medial,ipsi6599medial]

ipsilatteralcontrol=[ipsi5123lateral,ipsi5124lateral,ipsi5125lateral]
ipsilatteralexp=[ipsi4935lateral,ipsi4956lateral,ipsi4954lateral,ipsi6599latteral]

ipsionexp=[ipsi4935on,ipsi4956on,ipsi4954on,ipsi6599on]
ipsionctrl=[]
ipsioffareadatacontrol=pd.DataFrame()
ipsioffareadataexp=pd.DataFrame()


ipsioffareadatacontrol['med_gaba']=gat_count(ipsimedialcontrol)
ipsioffareadatacontrol['med_glut']=glut_count(ipsimedialcontrol)
ipsioffareadatacontrol['lat_gaba']=gat_count(ipsilatteralcontrol)
ipsioffareadatacontrol['lat_glut']=glut_count(ipsilatteralcontrol)

ipsioffareadatacontrol['med_gaba_percentage']=ipsioffareadatacontrol['med_gaba']/(ipsioffareadatacontrol['med_gaba']+ipsioffareadatacontrol['med_glut'])
ipsioffareadatacontrol['lat_gaba_percentage']=ipsioffareadatacontrol['lat_gaba']/(ipsioffareadatacontrol['lat_gaba']+ipsioffareadatacontrol['lat_glut'])


ipsioffareadataexp['med_gaba']=gat_count(ipsimedialexp)
ipsioffareadataexp['med_glut']=glut_count(ipsimedialexp)
ipsioffareadataexp['lat_gaba']=gat_count(ipsilatteralexp)
ipsioffareadataexp['lat_glut']=glut_count(ipsilatteralexp)
ipsioffareadataexp['on_gaba']=gat_count(ipsionexp)
ipsioffareadataexp['on_glut']=glut_count(ipsionexp)

ipsioffareadataexp['on_gaba_percent']=ipsioffareadataexp['on_gaba']/(ipsioffareadataexp['on_gaba']+ipsioffareadataexp['on_glut'])
ipsioffareadataexp['med_gaba_percent']=ipsioffareadataexp['med_gaba']/(ipsioffareadataexp['med_gaba']+ipsioffareadataexp['med_glut'])
ipsioffareadataexp['lat_gaba_percent']=ipsioffareadataexp['lat_gaba']/(ipsioffareadataexp['lat_gaba']+ipsioffareadataexp['lat_glut'])


plt.bar(['control med','exp med'],[ipsioffareadatacontrol['med_gaba_percentage'].mean(),ipsioffareadataexp['med_gaba_percent'].mean()],color=['b','r'],yerr=[ipsioffareadatacontrol['med_gaba_percentage'].sem(),ipsioffareadataexp['med_gaba_percent'].sem()])
ipsioffareadatacontrol_mean=round(ipsioffareadatacontrol['med_gaba_percentage'].mean(),3)
ipsioffareadatacontrol_std=round(ipsioffareadatacontrol['med_gaba_percentage'].sem(),3)
ipsioffareadataexp_mean=round(ipsioffareadataexp['med_gaba_percent'].mean(),3)
ipsioffareadataexp_std=round(ipsioffareadataexp['med_gaba_percent'].sem(),3)
p_med=round(st.ttest_ind(ipsioffareadataexp['med_gaba_percent'],ipsioffareadatacontrol['med_gaba_percentage'])[1],5)

plt.text(-0.5, -0.2, f' mean: {ipsioffareadatacontrol_mean} \n std:{ipsioffareadatacontrol_std}')
plt.text(0.6,-0.2,f' mean: {ipsioffareadataexp_mean} \n std:{ipsioffareadataexp_std}')
plt.text(0,-0.4,f'p value med ctrl vs exp:\n {p_med}')
plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/medipsi control exp.eps')

#=======================================================================================
'''tests plots and statistics'''
print('p value ipsimedial control vs exp',st.ttest_ind(ipsioffareadataexp['med_gaba_percent'],ipsioffareadatacontrol['med_gaba_percentage']))

plt.bar(['control med','exp med'],[ipsioffareadatacontrol['med_gaba_percentage'].mean(),ipsioffareadataexp['med_gaba_percent'].mean()],color=['b','r'],yerr=[ipsioffareadatacontrol['med_gaba_percentage'].sem(),ipsioffareadataexp['med_gaba_percent'].sem()])
ipsioffareadatacontrol_mean=ipsioffareadatacontrol['med_gaba_percentage'].mean()
ipsioffareadatacontrol_std=ipsioffareadatacontrol['med_gaba_percentage'].sem()


plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/medipsi control exp.svg')


print('p value ipsilateral control vs exp',st.ttest_ind(ipsioffareadataexp['lat_gaba_percent'],ipsioffareadatacontrol['lat_gaba_percentage']))
plt.bar(['control lat','exp lat'],[ipsioffareadatacontrol['lat_gaba_percentage'].mean(),ipsioffareadataexp['lat_gaba_percent'].mean()],color=['b','r'],yerr=[ipsioffareadatacontrol['med_gaba_percentage'].sem(),ipsioffareadataexp['med_gaba_percent'].sem()])
control_ipsioff_lat_mean=round(ipsioffareadatacontrol['lat_gaba_percentage'].mean(),3)
control_ipsioff_lat_std=round(ipsioffareadatacontrol['lat_gaba_percentage'].sem(),3)
exp_ipsioff_lat_mean=round(ipsioffareadataexp['lat_gaba_percent'].mean(),3)
exp_ipsioff_lat_std=round(ipsioffareadataexp['lat_gaba_percent'].sem(),3)
p_lat=round(st.mannwhitneyu(ipsioffareadataexp['lat_gaba_percent'],ipsioffareadatacontrol['lat_gaba_percentage'])[1],5)
#plt.text(1.7,-0.2,f'mean:{control_ipsioff_lat_mean} \n sem:  {control_ipsioff_lat_std}')
#plt.text(2.7,-0.2,f'mean:{exp_ipsioff_lat_mean} \n sem:{exp_ipsioff_lat_std}')
#plt.text(2.2,-0.4,f'p value lat  ctrl vs exp:\n {p_lat}')
plt.ylabel('ratio of gaba positive cfos positve/ al cfos positive')
plt.title('Off areas comparison ipsi side')

plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/of areas comparison.svg')
plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/of areas comparison.eps')
plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/of areas comparison.pdf')
plt.show()
#===================================================================================================
'''experimental fos statistics'''
ipsi4935whole=('C:/Users/CNB/Desktop/test/for KI/4935/Statistics for 4935 ipsi whole.csv')
contra4935whole=('C:/Users/CNB/Desktop/test/for KI/4935/Statistics for 4935 contra whole.csv')
ipsi4935ons=('C:/Users/CNB/Desktop/test/for KI/4935/Statistics for 4935 ipsi on.csv')
contra4935ons=('C:/Users/CNB/Desktop/test/for KI/4935/Statistics for 4935 contra on.csv')

ipsi4954whole=('C:/Users/CNB/Desktop/test/for KI/4954/Statistics for 4954 ipsi.csv')
contra4954whole=('C:/Users/CNB/Desktop/test/for KI/4954/Statistics for 4954 contra.csv')
ipsi4954ons=('C:/Users/CNB/Desktop/test/for KI/4954/Statistics for 4954 ipsi on.csv')
contra4954ons=('C:/Users/CNB/Desktop/test/for KI/4954/Statistics for 4954 contra on .csv')



ipsi4956whole=('C:/Users/CNB/Desktop/test/for KI/4956/Statistics for 4956 ipsi whole.csv')
contra4956whole=('C:/Users/CNB/Desktop/test/for KI/4956/Statistics for 4956 contra whole.csv')
ipsi4956ons=('C:/Users/CNB/Desktop/test/for KI/4956/Statistics for 4956 on ipsi.csv')
contra4956ons=('C:/Users/CNB/Desktop/test/for KI/4956/Statistics for 4956 on contra.csv')


ipsi6287whole=('C:/Users/CNB/Desktop/test/for KI/6287/Statistics for 6287 ipsi whole.csv')
contra6287whole=('C:/Users/CNB/Desktop/test/for KI/6287/Statistics for 6287 contra whole.csv')
ipsi6287ons=('C:/Users/CNB/Desktop/test/for KI/6287/Statistics for 6287 ipsi on.csv')
contra6287ons=('C:/Users/CNB/Desktop/test/for KI/6287/Statistics for 6287 on contra.csv')



ipsi6599whole=('C:/Users/CNB/Desktop/test/for KI/6599/Statistics for 6599 IPSI WHOLE.csv')
contra6599whole=('C:/Users/CNB/Desktop/test/for KI/6599/Statistics for 6599 CONTRA WHOLE.csv')
ipsi6599ons=('C:/Users/CNB/Desktop/test/for KI/6599/Statistics for 6599 ON IPSI.csv')
contra6599ons=('C:/Users/CNB/Desktop/test/for KI/6599/Statistics for 6599 ON CONTRA.csv')

#=============================================================================================================
'''controls fos statistics '''
ipsi5123wholes=('C:/Users/CNB/Desktop/test/for KI/5123/Statistics for 5123 ipsi whole.csv')
contra5123wholes=('C:/Users/CNB/Desktop/test/for KI/5123/Statistics for 5123 contra whole.csv')

ipsi5123ons=('C:/Users/CNB/Desktop/test/for KI/5123/Statistics for 5123 on ipsi.csv')
contra5123ons=('C:/Users/CNB/Desktop/test/for KI/5123/Statistics for 5123 on contra.csv')

ipsi5124wholes=('C:/Users/CNB/Desktop/test/for KI/5124/Statistics for 5124 control ipsi.csv')
contra5124wholes=('C:/Users/CNB/Desktop/test/for KI/5124/Statistics for 5124 control contra.csv')
ipsi5124ons=('C:/Users/CNB/Desktop/test/for KI/5124/Statistics for 5124 on ipsi.csv')
contra5124ons=('C:/Users/CNB/Desktop/test/for KI/5124/Statistics for 5124 on contra.csv')

ipsi5125wholes=('C:/Users/CNB/Desktop/test/for KI/5125/Statistics for 5125 ipsi whole.csv')
contra5125wholes=('C:/Users/CNB/Desktop/test/for KI/5125/Statistics for 5125 contra whole.csv')

ipsi5125ons=('C:/Users/CNB/Desktop/test/for KI/5125/Statistics for 5125 ipsi on .csv')
contra5125on=('C:/Users/CNB/Desktop/test/for KI/5125/Statistics for 5125 contra on.csv')
ipsi6599medial=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/Results ipsi medial pos neg.csv'))
ipsi6599latteral=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/6599/for gabafos 6599/latteral/latteral ipsi.csv'))
ipsi6599on=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/6599/for gabafos 6599/area of diference implant/6599 Results 1_POS 2_NEG.csv'))

contra6599medial=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/medial contra pos neg.csv'))
contra6599on=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/Results 6599 contra 1pos 2neg very active.csv'))
contra6599lateral=np.array(percentages('C:/Users/CNB/Desktop/test/for KI/6599/6599/for gabafos 6599/latteral/lateral contra pos neg.csv'))
#=============================================================================================

#===================================================================================================
'''CENTER OF ON AREA!, THE POINT ZERO FOR DISTACE MEASURING'''
pointzero=[0,0,0]

point6287ipsi=[1300,-300,0]
point6287contra=[1250,-300,0]


point6599ipsi=[1000,-500,32]
point6599contra=[1800,-500,24]

point4935ipsi=[2000,-400,0]
point4935contra=[1750,-400,0]

point4954ipsi=[1750,-1000,0]
point4954contra=[1750,-1000,0]

point4956ipsi=[1250,-400,0]
point4956contra=[1500,-400,0]


point6601ipsi=[1200,-300,0]
point6601contra=[1700,-400,0]


point9323ipsi=[1600,-600,0]
point9323contra=[1200,-600,0]

point5123ipsi=[1200,-250,0]
point5124ipsi=[1200,-250,0]
point5125ipsi=[1200,-250,0]

#===============================================================================================
'''lists'''
lol=[[ipsi6287whole,contra6287whole],[ipsi4954whole,contra4954whole],[ipsi4935whole,contra4935whole],[ipsi4956whole,contra4956whole],[ipsi6599whole,contra6599whole]]
control_ipsi_contra_whole=[[ipsi5123wholes,contra5123wholes],[ipsi5124wholes,contra5124wholes],[ipsi5125wholes,contra5125wholes]]

ipsicontraonlist=[[ipsi4935ons,contra4935ons],[ipsi4954ons,contra4954ons],[ipsi4956ons,contra4956ons],[ipsi6287ons,contra6287ons],[ipsi6599ons,contra6599ons]]

allipsilist=[ipsi6287whole,ipsi4954whole,ipsi4935whole,ipsi4956whole,ipsi6599whole]

ipsilop=[point6287ipsi,point4954ipsi,point4935ipsi,point4956ipsi,point6599ipsi]

ipsilopcontrol=[point5123ipsi,point5124ipsi,point5125ipsi]
ipsion_control=[]

control_ipsi_contra_pointsz=[[0,0,0],[0,0,0],[0,0,0]]
allipsilistctrl=[ipsi5123wholes,ipsi5124wholes,ipsi5125wholes]



ipsiareas6599=[ipsi6599medial,ipsi6599latteral,ipsi6599on]
contraareas6599=[contra6599medial,contra6599lateral]
ipsiareas4954=[ipsi4954medial,ipsi4954lateral,ipsi4954on]
contraareas4954=[contra4954medial,contra4954lateral,contra4954on]

ipsimedialcontrol=[ipsi5123medial,ipsi5124medial,ipsi5125medial]
ipsimedialexp=[ipsi4935medial,ipsi4956medial,ipsi4954medial,ipsi6599medial]
contramedialexp=[contra4935medial,contra4956medial,contra4954medial,contra6599medial]
contramedialcontrol=[contra5123medial,contra5124medial,contra5125medial]
ipsiareas4954=[ipsi4954medial,ipsi4954lateral,ipsi4954on]
contraareas4954=[contra4954medial,contra4954lateral,contra4954on]

ipsilatteralcontrol=[ipsi5123lateral,ipsi5124lateral,ipsi5125lateral]
ipsilatteralexp=[ipsi4935lateral,ipsi4956lateral,ipsi4954lateral,ipsi6599latteral]
contralatteralexp=[contra4935lateral,contra4956lateral,contra4954lateral,contra6599lateral]
contralatteralcontrol=[contra5123lateral,contra5124lateral,contra5125lateral]
ipsiareas4956=[ipsi4956medial,ipsi4956lateral,ipsi4956on]
contraareas4956=[contra4956medial,contra4956lateral,contra4956on]
ipsi5124areas=[ipsi5124medial,ipsi5124lateral]
contra5124areas=[contra5124medial,contra5124lateral]
ipsiareas5123=[ipsi5123medial,ipsi5123lateral]
contraareas5123=[contra5123medial,contra5123lateral]


ipsionexp=[ipsi4935on,ipsi4956on,ipsi4954on,ipsi6599on]
contraonexp=[contra4935on,contra4956on,contra4954on,contra6599on]
ipsi5125areas=[ipsi5125medial,ipsi5125lateral]
contra5125_areas=[ipsi5125medial,contra5125lateral]

on=[[ipsi4935on],[ipsi4956on],[ipsi4954on],[ipsi6599on]]
med=[[ipsi4935medial],[ipsi4956medial],[ipsi4954medial],[ipsi6599medial]]
lat=[[ipsi4935lateral],[ipsi4956lateral],[ipsi4954lateral],[ipsi6599latteral]]
off=[[ipsi4935medial,ipsi4935lateral],[ipsi4956medial,ipsi4956lateral],[ipsi4954medial,ipsi4954lateral],[ipsi6599medial,ipsi6599latteral]]




on=[[ipsi4935on],[ipsi4956on],[ipsi4954on],[ipsi6599on]]
med=[[ipsi4935medial],[ipsi4956medial],[ipsi4954medial],[ipsi6599medial]]
lat=[[ipsi4935lateral],[ipsi4956lateral],[ipsi4954lateral],[ipsi6599latteral]]
off=[[ipsi4935medial,ipsi4935lateral],[ipsi4956medial,ipsi4956lateral],[ipsi4954medial,ipsi4954lateral],[ipsi6599medial,ipsi6599latteral]]

oncontraexp=[[contra4935on],[contra4956on],[contra4954on],[contra6599on]]
ofmedcontraexp=[[contra4935medial],[contra4956medial],[contra4954medial],[contra6599medial]]
offlatcontraexp=[[contra4935lateral],[contra4956lateral],[contra4954lateral],[contra6599lateral]]

offcontraexp=[[contra4935medial,contra4935lateral],[contra4956medial,contra4956lateral],[contra4954medial,contra4954lateral],[contra6599medial,contra6599lateral]]

ipsiareas4935=[ipsi4935medial,ipsi4935lateral,ipsi4935on]
contraareas4935=[contra4935medial,contra4935lateral,contra4935on]

allipsiareasctrl=[ipsiareas5123,ipsi5124areas,ipsi5125areas]
allipsiareasexp=[ipsiareas4935,ipsiareas4956,ipsiareas4954,ipsiareas6599]

allcontraareasctrl=[contraareas5123,contra5124areas,contra5125_areas]
allcontraareasexp=[contraareas4935,contraareas4956,contraareas4954,contraareas6599]




def vgat_percentageploter(on,off_medial,off_lateral):
    
    plt.style.use('fivethirtyeight')
    
    
    fig, ax = plt.subplots(3)
    
    ax[0].pie([on[-1],on[-2]],labels=['vgatneg','vgatpos'],autopct='%1.2f%%')
    ax[0].set_title('on region')
    #plt.show()
    #ax[2]=plt.subplot()
    ax[1].pie([off_medial[-1],on[-2]],labels=['vgatneg','vgatpos'],autopct='%1.2f%%')
    ax[1].set_title('off medial region')
   #plt.show()
    #off_latteral=plt.subplot()
    ax[2].pie([off_lateral[-1],on[-2]],labels=['vgatneg','vgatpos'],autopct='%1.2f%%')
    ax[2].set_title('off region latteral')
    fig.suptitle(str(), fontsize=16)
   # plt.show()
   
   
   
def percentageploter2(on,off_med,off_lat,title):
    plt.style.use('seaborn')
    
    on=area_mean_finder(on)
    print(type(on))
    
    off_med=area_mean_finder(off_med)
    print(type(off_med))
   
    off_lat=area_mean_finder(off_lat)
    print(type(off_lat))
  
    fig, ax = plt.subplots(3)
    
    ax[0].pie(on,labels=['vgatpos','vgatneg'],autopct='%1.2f%%')
    ax[0].set_title('on region')
    #plt.show()
    #ax[2]=plt.subplot()
    ax[1].pie(off_med,labels=['vgatpos','vgatneg'],autopct='%1.2f%%')
    ax[1].set_title('off medial region')
   #plt.show()
    #off_latteral=plt.subplot()
    ax[2].pie(off_lat,labels=['vgatpos','vgatneg'],autopct='%1.2f%%')
    ax[2].set_title('off region latteral')
    fig.suptitle(title, fontsize=16)
   # plt.show()





def area_mean_finder(area_list):
    '''
    finds the mean of the gat and glut cells from areas of the same kind(on med or lat) of many different animals

    Parameters
    ----------
    fos_list : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    '''
    #print(area_list)
    gat_meanlist=[]
    glut_meanlist=[]
    #print('we')
    for file in area_list:
        gat_num=file[-2]
        glut_num=file[-1]
        #print(gat_num,glut_num)
        gat_meanlist.append(gat_num)
        glut_meanlist.append(glut_num)
    gat_mean=np.mean(gat_meanlist)
    glut_mean=np.mean(glut_meanlist)
    return [gat_mean,glut_mean]
        
def on_med_lat_difference_finder(on,med,lat):
    '''
    finds the means of 

    Parameters
    ----------
    on : TYPE
        DESCRIPTION.
    med : TYPE
        DESCRIPTION.
    lat : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    on_gat_mean=area_mean_finder(on)[0]
    on_glut_mean=area_mean_finder(on)[1]
    on_means=[on_gat_mean,on_glut_mean]
    
    med_gat_mean=area_mean_finder(med)[0]
    med_glut_mean=area_mean_finder(med)[1]
    med_means=[med_gat_mean,med_glut_mean]
    
    lat_gat_mean=area_mean_finder(lat)[0]
    lat_glut_mean=area_mean_finder(lat)[1]
    lat_means=[lat_gat_mean,lat_glut_mean]
    
    
    return [on_means,med_means,lat_means]



bins=np.linspace(-2000,2000,50)






 
#ipsion6599=distance_finder([0,0,0], 'C:\Users\andre\OneDrive\Desktop\whole retina\9323')






''' IPSI ON AREAS FOS COUNT NO THRESHOLD'''



#

def distance_finder(point,filename,i=0):
    '''
    

    Parameters
    ----------
    point : TYPE list or tuple with three numbers  [x,y,z]
        DESCRIPTION. the xyz coordinates of the point from which we want to find the spatial distribution of cells
    filename : TYPE csv file output of the 3d object counter plug in of image j. contains all the cells identified by the algorythm in rows and several attributes of them
    among which the x y z coordinates 
        DESCRIPTION.

    Returns
    -------
    data : TYPE dataframe
        data has all the initial information plus the distances in all axis and in space .

    '''
    #point =[1170.48,311.96,0]
    data=pd.read_csv(filename)
    data['Y']=-data['Y']
    data['X']=data['X']
    distance_x=data['X']-point[0]
    distance_y=data['Y']-point[1]
    distance_z=data['Z']-point[2]
    distance_2d=np.sqrt((distance_x**2)+(distance_y**2))
   
    distance_3d=np.sqrt((distance_x**2)+(distance_y**2)+(distance_z**2))
    data['distance_x']= distance_x
    data['distance_y']=distance_y
    data['distance_z']=distance_z
    data['distance_3d']=distance_3d
    data['distance_2d']=distance_2d
    data.loc[data.distance_x<0,'distance_2d']=-distance_2d
    mini=data['distance_2d'].min()
    maxi=data['distance_2d'].max()
    xmaxi= data['distance_x'].max()
    xmini=data['distance_x'].min()
    data['distance_x_norm']=data['distance_x']/(xmaxi-xmini)
    data['distance_2d_norm']=data['distance_2d']/(maxi-mini)
    data['Mean_norm']=(data['Mean']-data['Mean'].min())/((data['Mean'].max()-data['Mean'].min()))
    data_filt=data.loc[data['Mean_norm']>=i]
    return data_filt
 
#we need to find the mean cell count for all the animals  for every bin






















def el_plotador(ipsi,contra):##### p
    bins=np.linspace(-0.7,0.7,30)
   # sns.distplot(ipsi['distance_x'],bins=bins,norm_hist=True)
    #sns.distplot(contra['distance_x'],bins=bins,norm_hist=True)
    #sns.kdeplot(ipsi['distance_x'])
    #sns.kdeplot(ipsi['distance_x'],)
    #sns.kdeplot(ipsi,contra)
# =============================================================================
#     sigmai = ipsi['distance_2d_norm'].sem()
#     sigmac=contra['distance_2d_norm'].sem()
#     mui=ipsi['distance_2d_norm'].mean()
#     muc=-contra['distance_2d_norm'].mean()
#     plt.hist(ipsi['distance_2d_norm'],color='b',label='ipsi',bins=bins,density=True)
#    
#     plt.hist(-contra['distance_2d_norm'],color='r',label='contra',alpha=0.5,stacked=True,bins=bins,density=True)
#     
# =============================================================================
    
# =============================================================================
#     co = ((1 / (np.sqrt(2 * np.pi) * sigmac)) *      # finds and plots the lines fitting the histogram
#      np.exp(-0.5 * (1 / sigmac * (bins - muc))**2))  #
#     ip = ((1 / (np.sqrt(2 * np.pi) * sigmai)) *      #
#      np.exp(-0.5 * (1 / sigmai * (bins - mui))**2))  #
#     plt.plot(bins,co,'--')
#     plt.plot(bins,ip)
#     plt.legend(loc='upper left')
#     plt.show()
# =============================================================================
    ipsi=distance_finder([0,0,0], ipsi)
    contra= distance_finder([0,0,0],contra)
    plt.scatter((-ipsi['X']+3000),ipsi['Y'],color='b',label='ipsi')
    plt.scatter(contra['X'],contra['Y'],color='r',label='contra')
    plt.grid()
    plt.legend(loc='upper left')
    plt.title('ChR2')
    plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/cfos location ipsicontra control.svg')
    plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/cfos cfos location ipsicontra control.eps')
    plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/cfos cfos location ipsicontra control.pdf')
    plt.show()

# =============================================================================
# 
# def mean_finder(ipsi_list, contra_list):
#     bins=np.linspace(-0.7,0.7,15)
#     contralist=[]
#     ipsilist=[]
#     for i,c in zip(ipsi_list, contra_list):
#         ipsi=i['distance_2d_norm']
#         contra=c['distance_2d_norm']
#         ipsibined=pd.cut(ipsi,bins=bins)
#         contrabined=pd.cut(contra,bins=bins)
#         ipsibined=ipsibined.value_counts(sort=False)
#         contrabined=contrabined.value_counts(sort=False)
#         ipsilist.append(ipsibined)
#         contralist.append(contrabined)
#     print(ipsilist,contralist)
#     
# # =============================================================================
# #     df=pd.DataFrame()
# #     df['ipsi']=ipsilist
# #     df['contra']=contralist
# #     df['mean']=df.mean(axis=0)
# # =============================================================================
#     return 
#     
#     
# ============================================================================
# =============================================================================
# def meanfinder(ls):
#      bins=np.linspace(-1.7,.5,15)
#      sumi=np.zeros(14)
#      for i in ls:
#          #print('ITERATION START')
#          
#          ipsibined1=pd.cut(i['distance_2d_norm'],bins=bins).value_counts(sort=False)
#         
#          #rint (ipsibined1)
#          sumi=sumi+ipsibined1
#          #print('sum',sumi)
#      return sumi
#          
# bins=np.linspace(-1.5,1.5,15)
def allploter(ipsi_list,contra_list):
    for i,c in zip(ipsi_list, contra_list):
        el_plotador(i,c)
# 
#     
# def mean_ploter(ipsi_list,contra_list):
#     ipsi=meanfinder(ipsi_list) 
#     contra=meanfinder(contra_list)
#     plt.hist(ipsi,color='b')
#     #plt.show()
#     plt.hist(contra,color='r')
#     plt.show()
# =============================================================================
    
def activation_ploter(filepathipsi,filepathcontra,title):
   
    plt.style.use('fivethirtyeight')
    bins=np.linspace(0,50,25)
    ipsi=pd.read_csv(filepathipsi)['Mean']
    contra=pd.read_csv(filepathcontra)['Mean']
    plt.hist(ipsi,bins=bins,alpha=0.5,label='ipsi')
    plt.hist(contra,bins=bins,color='r',alpha=0.5,label='contra')
    plt.xlabel('C-fos fluorescence intensity')
    plt.ylabel('Cell Number')
    plt.legend()
    plt.title(title)
    plt.show()
# =============================================================================
    plt.bar('ipsi',len(ipsi),alpha=0.5,label='ipsi')
    plt.bar('contra',len(contra),alpha=0.5,label='contra')
    plt.xlabel(['ipsi','contra'])
    plt.ylabel('Cell Number')
    plt.title(title)
    plt.legend()
    plt.show()
# =============================================================================
# =============================================================================
# plt.hist(a['Mean'],bins=np.linspace(0,50,50),color='y',alpha=0.3)
# plt.hist(b,bins=np.linspace(0,50,50),color='g',alpha=0.5)
# plt.style.use('seaborn')
# plt.show()
#     
#     
#     
# =============================================================================


bins=np.linspace(0,1,20)
def normalizer(ipsi_contra_list,bins,i=0):
    
    a=distance_finder([0,0,0],ipsi_contra_list[0],i)['Mean']
    b=distance_finder([0,0,0],ipsi_contra_list[1],i)['Mean']
    c=pd.DataFrame()
    c['ipsi']=a
    c['contra']=b
    tmax=c.max().max()
    tmin=c.min().min()
    c=(c-tmin)/(tmax-tmin)
    a=np.histogram(c['ipsi'],bins=bins)
    b=np.histogram(c['contra'],bins=bins)
    ispibinned=a[0]
    contrabinned=b[0]
    binedges=a[1]
    
    return[ispibinned,contrabinned,binedges]

def merger(filelist,bins,i=0):
    
    
    ''' for cfos intensity ploting normalization and binning'''
   # print ('filelist',filelist)
    ipsidf=pd.DataFrame()
    contradf=pd.DataFrame()
    binedges=normalizer(filelist[0],bins,i)[2]
    bin_centers = 0.5*(binedges[1:] + binedges[:-1])
   # print ('bincenters',bin_centers)
    #print(bin_centers)
    #binwidth=(binedges[:-1]-binedges[1:])
    for file in filelist:
       #print (file)
       ipsi=pd.DataFrame(normalizer(file,bins,i)[0])              #make a new dataframe from
      # print( ipsi)
       contra=pd.DataFrame(normalizer(file,bins,i)[1])
      # print(contra)
       ipsidf=pd.concat([ipsidf,ipsi],axis=1)
       contradf=pd.concat([contradf,contra],axis=1)
       #print (ipsidf,contradf)
    ipsidf['mean']=ipsidf.mean(axis=1)
    ipsidf['std']=ipsidf.sem(axis=1)
    ipsidf['bincenters']=bin_centers
    contradf['mean']=contradf.mean(axis=1)
    contradf['std']=contradf.sem(axis=1)
    contradf['bincenters']=bin_centers
    #plt.bar(df['bincenters'],df['mean'],align='edge',edgecolor='black',width=0.05,yerr=df['std'],capsize=0.3)#xlabel='normalised intensity',ylabel='cell count')
    #plt.xlabel='normalised intensity'
    #plt.ylabel='cell count'
    #plt.show()
    return [ipsidf, contradf]



# =============================================================================
def ipsicontra_mean_intensity_ploter(list_of_lists,bins,i=0):
     
     plt.style.use('fivethirtyeight')
     a=merger(list_of_lists,bins,i)
     for i in a:
         plt.bar(i['bincenters'],i['mean'],align='edge',edgecolor='black',alpha=0.5,width=0.052632)#,yerr=a[0]['std'])
     plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/ipsi vs contra mean intensity')
     a=merger(list_of_lists,bins,i)
     plt.bar(a['bincenters'],a['mean'],align='edge',edgecolor='black',width=0.05,yerr=a['std'],capsize=0.3)
     plt.xlabel='normalised intensity'
     plt.ylabel='cell count'
     plt.show()
     # =============================================================================
     # width=0.052632
     # plt.plot(a[0]['bincenters'],a[0]['mean'],color='b')        
     # plt.plot(a[1]['bincenters'],a[1]['mean'],color='r')
     # plt.plot(a[0]['bincenters'],(a[0]['mean']+a[0]['std']),linestyle='dotted',color='b',alpha=0.3)
     # plt.plot(a[0]['bincenters'],(a[0]['mean']-a[0]['std']),linestyle='dotted',color='b',alpha=0.3)
     # plt.plot(a[1]['bincenters'],(a[1]['mean']+a[1]['std']),linestyle='dotted',color='r',alpha=0.3)
     # plt.plot(a[1]['bincenters'],(a[1]['mean']-a[1]['std']),linestyle='dotted',color='r',alpha=0.3)
     # 
     # plt.show()
     # =============================================================================
     #plt.bar((a[0]['bincenters']-width/2),a[0]['mean'],color='b',align='center',edgecolor='black',alpha=0.5,width=width/2)
     #plt.errorbar((a[0]['bincenters']-width/2),a[0]['mean'],a[0]['std'],color='black',capsize=5,elinewidth=2)
     #plt.errorbar((a[0]['bincenters']),a[0]['mean'],a[0]['std'],color='black',elinewidth=2)
    # plt.bar((a[1]['bincenters']),a[1]['mean'],color='r',align='center',edgecolor='black',alpha=0.5,width=width/2)#,yerr=a[1]['std'])
     #plt.show()
# =============================================================================
all_ipsi_on_Chr2=['C:/Users/CNB/Desktop/test/for KI/6287/Statistics for 6287 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/6599/6599 Results 1_POS 2_NEG.csv','C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos2 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/4954/Results 4954 gabafos1 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/4956/4956 gabafos2 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/4956/Results4956 gaba fos 1ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafosipsi on.csv','C:/Users/CNB/Desktop/test/for KI/4935/results 4935 gabafos2 ipsi on.csv']
all_ipsi_on_ctrl=['C:/Users/CNB/Desktop/test/for KI/5125/Results gabafos1 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos2 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/5124/Results 5124 gabafos1 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos1 ipsi on.csv','C:/Users/CNB/Desktop/test/for KI/5123/Results 5123 gabafos2 ipsi on.csv']
ipsions=[ipsi4935ons,ipsi4954ons,ipsi4956ons,ipsi6287ons,ipsi6599ons]
ipsionctrl=[ipsi5123ons,ipsi5124ons,ipsi5125ons]

def fos_mean_num_ploter(list1,list2,label1,label2,title):
    ''' takes as input two lists and two stings like [ipsion1,ipsion2],[contraon1,contraon2]  
    plots the mean number of c fos positive cells (preferably used for on areas) between two groups'''
    
    
    
    plt.style.use('fivethirtyeight')
    ipsil=[]
    contral=[]
    try:
        for ipsi in list1:
            a=len(pd.read_csv(ipsi))
            ipsil.append(a)
        for contra in list2:
            b=len(pd.read_csv(contra))
            contral.append(b)
    except:
        print( 'test')
        
        
    ipsimean=round(np.mean(ipsil),3)
    contramean=round(np.mean(contral),3)
    ipsistd=round(np.sem(ipsil),3)
    contrastd=round(np.sem(contral),3)
    p=round(st.ttest_ind(ipsil,contral)[1],3)
    plt.bar([label1, label2],[ipsimean,contramean],yerr=[ipsistd,contrastd],color=['b','r'])
    plt.text(-0.5,-100, f'mean{label1}={ipsimean} \n std{label1}={ipsistd}')
    plt.text(1,-100, f'mean{label2}={contramean} \n std{label2}={contrastd}')
    plt.text(0.2,-150,f'ttest pvalue: {p}')
    plt.ylabel('cell number')   
    plt.title(title)
    plt.savefig(f'C:/Users/CNB/Desktop/test/for KI/figures/fosnumberipsi {label1} {label2},{title} .pdf')
    plt.savefig(f'C:/Users/CNB/Desktop/test/for KI/figures/fosnumberipsi {label1} {label2}, {title} .eps')
    plt.savefig(f'C:/Users/CNB/Desktop/test/for KI/figures/fosnumberipsi {label1} {label2},{title} .svg')    
    plt.show()
    return(ipsil,contral)   


whole_sc_chr2vsctr=fos_mean_num_ploter(allipsilist,allipsilistctrl,'chr2','ctrl','whole sc')
only_on_chr2vsctr=fos_mean_num_ploter(ipsions,ipsionctrl,'chr2','ctrl','only on')
        
        
bins=np.linspace(-1,1,60)
def ipsiallploter(pointlist,allipsilist,bins,distance_of_interest,i):
    ''' takes as input a list of points (the centeres of the on areas),a list of filepaths 
    corresponding to the whole colliculus coordinates measurments,and the bins)
    it return a dataframe with with binned distance counts for every ainmal in each column
    and maybe mean and std for every bin'''
    ipsidf=pd.DataFrame()
    for point,file in zip(pointlist,allipsilist):
        ipsi=pd.DataFrame(data=distance_finder(point,file,i)[distance_of_interest])
        print(ipsi)
        ipsi=pd.Series(np.histogram(ipsi,bins)[0])####   ipsi[0] is the counts ipsi [1] the binedges
        ipsi=ipsi/(ipsi.max()-ipsi.min())
        binedges=pd.Series(np.histogram(ipsi,bins)[1])
        ipsidf=pd.concat([ipsidf,ipsi],axis=1)
    bincenters=bincenters=0.5*(binedges[1:] + binedges[:-1])
    ipsidf=pd.concat([ipsidf,bincenters],axis=1)
    return ipsidf
    
        
        
# =============================================================================
''' ploting all the columns of the '''
# for i in range(5):
#     plt.plot(a.iloc[:,-1],a.iloc[:,i])
#     plt.show()        
# =============================================================================
        
     
        
        
def function2(listipsicontra,bins,i):
    ipsi=pd.DataFrame(data=distance_finder([0,0,0],listipsicontra[0],i)['distance_2d_norm'])
    contra=pd.DataFrame(data=distance_finder([0,0,0],listipsicontra[1],i)['distance_2d_norm'])
    ipsi=np.histogram(ipsi,bins=bins)[0]
    contra=np.histogram(contra,bins=bins)[0]
    binedges=np.histogram(contra,bins=bins)[1]
    return [ipsi,contra,binedges]




def function3(list_of_lists,bins):
    binedges=function2(list_of_lists[0],bins)[2]
    bincenters=0.5*(binedges[1:] + binedges[:-1])
    print (bincenters,len(bincenters))
    first=pd.DataFrame(function2(list_of_lists[0],bins)[0])
    firstc=pd.DataFrame(function2(list_of_lists[0],bins)[1])
    print('before llop')
    for listipsicontra in list_of_lists[1:]:
        
        ipsi=pd.DataFrame(function2(listipsicontra,bins)[0])
        contra=pd.DataFrame(function2(listipsicontra,bins)[1])
        first=pd.concat([first,ipsi],axis=1)
        firstc=pd.concat([firstc,contra],axis=1)
    firstc['mean']=firstc.mean(axis=1)
    first['mean']=first.mean(axis=1)
    first['std']=first.iloc[:,:-1].sem(axis=1)
    
    firstc['std']=firstc.iloc[:,:-1].sem(axis=1)
    first['BINcenters']=bincenters
    firstc['BINcenters']=bincenters

    return(first,firstc)

def ipsicontra_intensity_ploter(lol,bins,title):
    a=merger(lol,bins)
    a[0]['mean']==a[1]['mean']
    plt.style.use('fivethirtyeight')
    plt.plot(a[0]['bincenters'],a[0]['mean'],label='ipsi',color='b')
    plt.plot(a[0]['bincenters'],a[1]['mean'],label='contra',color='r')
    plt.legend()
    plt.xlabel('Normalised fluorescent intensity')
    plt.ylabel('Number of cells')
    plt.title(title)
    plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/cfos normalised intensity whole colliculus.svg')
    plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/cfos normalised intensity whole colliculus.eps')
    plt.savefig('C:/Users/CNB/Desktop/test/for KI/figures/cfos normalised intensity whole colliculus.pdf')
    
    plt.show()



outputfilepath='C:/Users/CNB/Desktop/test/for KI/figures/for ploting/mldistance controls.eps'
def alldistanceploter(ipsilop,allipsilist,bins,distancetype,outputfilepath):
    a=ipsiallploter(ipsilop,allipsilist,bins,distancetype,)
    
    for i in range(len(ipsilop)):
         plt.style.use('fivethirtyeight')
         plt.plot(a.iloc[:,-1],a.iloc[:,i])
    plt.xlabel('ML')
    plt.ylabel('cfos positive cells')
    plt.title('mCherry')
    plt.savefig(outputfilepath)
    #plt.savefig('C:/Users/chara/Downloads/for ploting-20210704T175929Z-001/for ploting/mldistance controls.eps')
    #plt.savefig('C:/Users/chara/Downloads/for ploting-20210704T175929Z-001/for ploting/mldistancecontrols.pdf')
    
    plt.show()