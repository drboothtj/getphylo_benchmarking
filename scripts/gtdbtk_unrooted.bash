start_time=`date`
gtdbtk identify --genome_dir ../benchmarking_data/gtdb_formated/10_1/ --out_dir output/ -x 'fasta' --cpus 8
gtdbtk align --identify_dir output/ --out_dir output/ --skip_gtdb_refs --cpus 8
gtdbtk infer --msa_file output/align/gtdbtk.bac120.user_msa.fasta.gz --out_dir output/ --cpus 8
end_time=`date`
echo start time: $start_time endtime: $end_time
