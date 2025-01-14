'''
Get all cptac data
downloads data into docker image
'''

import cptac
import os
os.mkdir('data/') if not os.path.exists('data/') else print('Folder exists data/')

def getCancerObj(cancertype):
   # cptac.download(dataset=cancertype,source='harmonized',)
    if cancertype == 'brca':
        dat = cptac.Brca()
    elif cancertype == 'ccrcc':
        dat = cptac.Ccrcc()
    elif cancertype == 'coad':
        dat = cptac.Coad()
    elif cancertype == 'gbm':
        dat = cptac.Gbm()
    elif cancertype == 'hnscc':
        dat = cptac.Hnscc()
    elif cancertype == 'lscc':
        dat = cptac.Lscc()
    elif cancertype == 'luad':
        dat = cptac.Luad()
    elif cancertype == 'ovarian':
        dat = cptac.Ov()
    elif cancertype =='pdac':
        dat = cptac.Pdac()
    elif cancertype =='ucec':
        dat = cptac.Ucec()
    else:
        print('Wrong cancer type: '+cancertype)
        exit()
    return dat


for ds in ['brca', 'ccrcc', 'ucec', 'coad','pdac', 'ovarian', 'luad', 'hnscc', 'gbm','lscc']:
    try:
        dat=getCancerObj(ds)

        #this call changed in recent version
        dat_list = dat.list_data_sources().set_index('Data type').to_dict()['Available sources']
        clinsource = dat_list['clinical']
        if 'harmonized' in clinsource:
            cs = 'harmonized'
        else:
            cs = clinsource[0]
        dat.get_clinical(cs)
        tsource = dat_list['proteomics']
        res = dat.get_proteomics(tsource[0])
        if res.columns.nlevels == 2:
            res.columns = res.columns.droplevel(1)
        
        print(ds+':',res.shape)
        res.to_csv('data/'+ds+'.csv')
    except Exception as e:
        print(e)
