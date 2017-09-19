import MySQLdb

db = MySQLdb.connect(host="comm-infocntr-amer-dev-01.ciean0huuvrb.us-east-1.rds.amazonaws.com",
                     user="infocntrdevmstr",         # your username
                     passwd="infocntrdevmstr_201708A",  # your password
                     db="devinfocntr")

target = db.cursor()

target.execute("INSERT INTO DETCG ( select  REC_TYPE_CODE,CAST(TRIM(REPT_ID) as unsigned),CAST(TRIM(SEQ_NO) as unsigned),CAST(TRIM(DET_REF_NO) as DECIMAl(25,0)),CAST(TRIM(PREV_REP_ID) as unsigned),CAST(TRIM(PROD_SERV_ID) as DECIMAL(25,0)),\
CAST(TRIM(PRESC_SERV_REF_NO) as unsigned),CAST(TRIM(FILL_NO) as unsigned),CAST(TRIM(DAYS_SUPP) as unsigned),CAST(TRIM(QTY) as unsigned)/1000,str_to_date(TRIM(DOS),'%Y%m%d'),CAST(TRIM(SPID_QUALIFIER) as unsigned),\
CAST(TRIM(SPID) as unsigned),CAST(TRIM(GAP_PREV) as DECIMAL(14,2)),CAST(TRIM(GAP_CURR) as DECIMAL(14,2)),CAST(TRIM(GAP_PER) as DECIMAL(14,2)),CAST(TRIM(PREV_REP_PERIOD) as unsigned),CAST(TRIM(CURR_REP_PERIOD) as unsigned),INSERT_TIMESTAMP from STG_DETCG);")
print "Loadind DETCG"
db.commit()

target.execute("INSERT INTO TPALH ( select REC_TYPE_CODE,CAST(TRIM(CURR_REP_PERIOD) as unsigned),CAST(TRIM(SEQ_NO) as unsigned),CAST(TRIM(REP_ID) as unsigned),str_to_date(TRIM(DDPS_SYSTEM_DATE),'%Y%m%d'),\
CAST(TRIM(DDPS_SYSTEM_TIME) as unsigned),FILE_ID,CAST(TRIM(LAB_CD) as unsigned),INSERT_TIMESTAMP from STG_TPALH);")
print "Loadind TPALH"
db.commit()

target.execute("INSERT INTO TPAMH ( select REC_TYPE_CODE,CAST(TRIM(CURR_REP_PERIOD) as unsigned),CAST(TRIM(SEQ_NO) as unsigned),str_to_date(TRIM(DDPS_SYSTEM_DATE),'%Y%m%d'),\
CAST(TRIM(DDPS_SYSTEM_TIME) as unsigned),FILE_ID,MANF_P_NO,INSERT_TIMESTAMP from STG_TPAMH);")
print "Loadind TPAMH"
db.commit()

target.execute("INSERT INTO TPAMT  (select REC_TYPE_CODE,CAST(TRIM(CURR_REP_PERIOD) as unsigned),CAST(TRIM(SEQ_NO) as unsigned),str_to_date(TRIM(DDPS_SYSTEM_DATE),'%Y%m%d'),CAST(TRIM(DDPS_SYSTEM_TIME) as unsigned),\
FILE_ID,MANF_P_NO,CAST(TRIM(DET_REC_COUNT) as unsigned),CAST(TRIM(TOT_REP_GAP_AMT_PREV) as DECIMAl(14,2)),CAST(TRIM(TOT_REP_GAP_AMT_CURR) as DECIMAl(14,2)),CAST(TRIM(TOT_REP_GAP_AMT_PRD) as DECIMAl(14,2)),INSERT_TIMESTAMP from devinfocntr.STG_TPAMT);")
print "Loadind TPAMT"
db.commit()

target.execute("INSERT INTO TPALT  (select REC_TYPE_CODE,CAST(TRIM(CURR_REP_PERIOD) as unsigned),CAST(TRIM(SEQ_NO) as unsigned),CAST(TRIM(REPT_ID) as unsigned),str_to_date(TRIM(DDPS_SYSTEM_DATE),'%Y%m%d'),CAST(TRIM(DDPS_SYSTEM_TIME) as unsigned),\
FILE_ID,CAST(TRIM(LAB_CD) as unsigned),CAST(TRIM(DET_REC_COUNT) as unsigned),CAST(TRIM(TOT_REP_GAP_AMT_PREV) as DECIMAl(14,2)),CAST(TRIM(TOT_REP_GAP_AMT_CURR) as DECIMAl(14,2)),CAST(TRIM(TOT_REP_GAP_AMT_PRD) as DECIMAl(14,2)),INSERT_TIMESTAMP from devinfocntr.STG_TPALT);")
print "Loadind TPAMT"
db.commit()

target.close()
