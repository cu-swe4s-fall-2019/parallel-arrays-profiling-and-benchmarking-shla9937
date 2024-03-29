import sys
import argparse
import gzip
import time
import matplotlib
import matplotlib.pyplot as plt
import cProfile
import data_viz
import plot_gtex


parser = argparse.ArgumentParser(
           description='Parsing operator.')

parser.add_argument('--gene_reads_file',
                    type=str,
                    help='Name of file',
                    required=True)

parser.add_argument('--sample_attributes',
                    type=str,
                    help='Attributes file',
                    required=True)

parser.add_argument('--gene',
                    type=str,
                    help='Gene of interest',
                    required=True)

parser.add_argument('--group_type',
                    type=str,
                    help='SMTS or SMTSD',
                    required=True)

parser.add_argument('--output_file',
                    type=str,
                    help='Output file name',
                    required=True)

args = parser.parse_args()


def main():
    search = plot_gtex.linear_search
    data_file_name = args.gene_reads_file
    sample_info_file_name = args.sample_attributes
    group_col_name = args.group_type
    sample_id_col_name = 'SAMPID'
    gene_name = args.gene
    output_file = args.output_file
    samples = []
    sample_info_header = None

    for l in open(sample_info_file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = search(group_col_name, sample_info_header)
    sample_id_col_idx = search(sample_id_col_name, sample_info_header)
    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
        curr_group_idx = search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    version = None
    dim = None
    data_header = None
    gene_name_col = 1
    group_counts = [[] for i in range(len(groups))]

    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = l.rstrip().split('\t')
            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    data_viz.boxplot(group_counts, output_file,
                     gene_name, group_col_name, "Gene read counts", groups)


if __name__ == '__main__':
    main()
