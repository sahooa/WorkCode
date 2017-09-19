import MySQLdb
import smtplib
from decimal import *

db = MySQLdb.connect(host="comm-infocntr-amer-dev-01.ciean0huuvrb.us-east-1.rds.amazonaws.com",
                     user="infocntrdevmstr",         # your username
                     passwd="infocntrdevmstr_201708A",  # your password
                     db="devinfocntr")

target = db.cursor()
target.execute(" select round(sum(gap_prev),2),round(sum(gap_curr),2),round(sum(gap_per),2) from devinfocntr.STG_DETCG")


for row in target:
    tot_gap_prev,tot_gap_curr,tot_gap_per = row
    print tot_gap_prev,tot_gap_curr,tot_gap_per

target.execute("SELECT cast(TOT_REP_GAP_AMT_PREV as decimal(14,2)),cast(TOT_REP_GAP_AMT_CURR as decimal(14,2)) ,cast(TOT_REP_GAP_AMT_PRD as decimal(14,2)) FROM devinfocntr.STG_TPAMT")

for row in target:
    det_tot_gap_prev,det_tot_gap_curr,det_tot_gap_per = row
    print det_tot_gap_prev,det_tot_gap_curr,det_tot_gap_per

if (float(det_tot_gap_prev)!=float(tot_gap_prev ) or float(det_tot_gap_curr)!=float(tot_gap_curr) or float(det_tot_gap_per)!=float(tot_gap_per)):
    print "Values dont add up"

else:
    print "All matched up"




target.close()
