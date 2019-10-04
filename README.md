# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Data_viz.py is now able to take a series of arguement to create a boxplot with lablled axes, title, and tick marks from a list. Will also check to make sure list isn't list of lists.

Plot_gtex.py contains the search methods linear_search, binary_search, and nested_binary_search. The nested_binary_search function will search a list of lists and return the second item in the list.

Plot_gtex_script.py is used to parse the files below using search functions from plot_gtex.py and plot them into a nice boxplot using data_viz.py.

Run_plot_gtex_script.sh is bash script to run plot_gtex_script.py.

Benchmarking:

Plot_gtex.linear_search.txt contains the results of a cProfile run of the plot_gtex_script.py using linear_search methods. When switched to binary searching, the program was actually much slower. This was because of how I made the list of lists containing the indexes of each item in the original list. I ran a cProfile on that and it showed that the 'append' function was the largest time sink because I used it in many for loops to get the searchable lists I wanted. A better way to do this would simply be to make a list the length of the list you want to search with a range of numbers that long (i.e. 0-(len(list)-1)) and then join the lists.

I then used the internal time function to see how long it takes using each search method to do the same task. For a for loop containing a search it too the linear search method 0.04559588432312012 seconds, it took the slow binary search 0.26045656204223633 seconds. This could be speed up a lot, by getting around the append problem.

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

