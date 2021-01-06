#!/bin/sh

#$ -N BONNIE_MVP_k
#$ -cwd
#$ -q sopa.1.day
#$ -l h_vmem=2G
#$ -l h_rt=8:00:00

# Send mail at submission and completion of script
#$ -m be
#$ -M s1534750@sms.ed.ac.uk

export MYHOME=`pwd`
export MYSCRATCH=/scratch/`pwd`

mkdir -p $MYSCRATCH

cp  $MYHOME/*  $MYSCRATCH/

cd $MYSCRATCH

echo -e "\n#############################################################"
date
hostname
echo -e "#############################################################\n"

# TYPE COMMAND LINE HERE -----------------------------------------------------------
python3 cp1_plot.py k 50 1 10100

echo "Job ran on $( hostname ) " > $MYHOME/mylog

cp  $MYSCRATCH/*  $MYHOME/
rm -r $MYSCRATCH
