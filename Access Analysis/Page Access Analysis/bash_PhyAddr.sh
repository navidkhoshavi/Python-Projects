#!/bin/bash
FILES=/media/nvidia/MyFile2/backup/TACO/swaptions/*
#TACO_PhyAddr=/home/nvidia/simulation/gem5/m5out/TACO/dedup/PhyAddr
TACO_PhyAddr=/media/nvidia/MyFile2/backup/TACO/swaptions/PhyAddr
for file in $FILES
do
	fname=`basename $file`
	echo "Processing $fname file"
	grep 'system.l2: ReadReq.*\|system.l2: ReadExReq.*' $file > $TACO_PhyAddr/$fname
	echo "Done processing $fname file"
	#$rm $FILES/$fname
done

#FILES2=/home/nvidia/simulation/gem5/m5out/TACO/dedup/PhyAddr/*
#TACO_PhyAddr_addr=/home/nvidia/simulation/gem5/m5out/TACO/dedup/PhyAddr/addr
FILES2=/media/nvidia/MyFile2/backup/TACO/swaptions/PhyAddr/*
TACO_PhyAddr_addr=/media/nvidia/MyFile2/backup/TACO/swaptions/PhyAddr/addr
for file in $FILES2
do
	fname=`basename $file`
	grep -o '0x.*' $file | cut -d " " -f1 | cut -d " " -f2 > $TACO_PhyAddr_addr/$fname
	#rm $FILES2/$fname
	#mv $TACO_PhyAddr_addr/* $TACO_PhyAddr
	#rmdir addr
done

	#grep -o 'paddr.*' $file | cut -d "," -f1 | cut -d " " -f2 > $TACO_parse_PhyAddr/$fname
	#grep -o 'paddr.*' $file | cut -d "," -f1 | cut -d " " -f2 > $TACO_parse_PhyAddr/$fname
	#$grep 'system.l2: ReadReq\|system.l2: ReadExReq' $file > $TACO_parse_PhyAddr/$fname
	#if grep $a $file; then
		#grep 'system.l2: ReadReq\|system.l2: ReadExReq' $file > $TACO_parse_PhyAddr/$fname
	#else
		#echo not found
	#fi
	#rm $TACO/$fname

