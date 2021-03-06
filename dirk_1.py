from dirk_2 import *

#****************
sim_dir = ''
data_dir = 'static/data/'

anonymous = True

#sorted_dirs = [ 'cat_sort/', 'nicksw_sort_pp1/', 'dan_sort/','james_sort/', 'nickst_sort/', 'pierre_sort/', 'martin_sort/']
sorted_dirs = [ 'test_sort/']
sorted_file = 'ViSAPy_0'

#********************* READ TSF FILES *******************
tsf_name = data_dir + '/'+ sorted_file + '_truth_filtered'
if True:  #Set to false, do not load .tsf file data
    f = open(sim_dir + tsf_name + '.tsf', "rb")
    print "Loading ", sim_dir + tsf_name + '.tsf'
    tsf = Tsf_file(f, sim_dir)  #Auto load tsf file attributes: n_electrodes, ec_traces, SampleFreqeuncy and others
    tsf.sim_dir = sim_dir
    tsf.tsf_name = tsf_name
    f.close()

##*************** READ GROUND TRUTH FILE : SORT1 ************************

ptcs_flag = 1

if 'silico' in sorted_file:
    Sort1 = Loadptcs(sorted_file+'_truth_filtered', sim_dir+data_dir, ptcs_flag, save_timestamps=False)
    Sort1.name=sorted_file+'_truth_filtered'
    Sort1.filename=sorted_file+'_truth_filtered'
    Sort1.rawfile= tsf_name
    Sort1.directory=sim_dir+data_dir
    Sort1.sim_dir = sim_dir
    Sort1.data_dir = data_dir

if 'ViSAPy' in sorted_file:
    Sort1 = Loadcsv_vispy(sorted_file, data_dir, tsf)


##************** READ 2ND SORT DATA **********

for sorted_dir in sorted_dirs:

    print "******* LOADING: ", sorted_dir, " ************* "

    fname = sim_dir + sorted_dir + sorted_file + '.csv'
    Sort2 = Loadcsv(fname, tsf, sim_dir + sorted_file + '/')
    Sort2.directory=sim_dir + sorted_dir
    Sort2.name = sorted_file
    Sort2.filename=sorted_file
    Sort2.sim_dir = sim_dir
    Sort2.chanpos=[999]
    f.close()

    Sort2.n_spikes=0
    for i in range(len(Sort2.units)):
        Sort2.n_spikes+= len(Sort2.units[i])

    #Run the compare_sorts algorithm on the data if not already done
    Compare_sorts(Sort1, Sort2, tsf)

Plot_Composite_metrics(sim_dir, sorted_dirs, sorted_file, anonymous)
