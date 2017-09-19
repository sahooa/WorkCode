import MySQLdb
from xlrd import open_workbook
import time
import datetime
db = MySQLdb.connect(host="v490721-infocenter-rds-dev.cbuqm0ljpfgq.us-east-1.rds.amazonaws.com",
                     port = 1521,# your host, usually localhost
                     user="infocenteradmin",         # your username
                     passwd="infocenter123",  # your password
                     db="eiclegal")
target = db.cursor()
target.execute("TRUNCATE TABLE STG_MEMOTECH_MOI")
target.execute("TRUNCATE TABLE STG_MEMOTECH_FILING")
target.execute("TRUNCATE TABLE STG_MEMOTECH_EXPRY")
target.execute("TRUNCATE TABLE STG_MEMOTECH_GRNT")
target.execute("TRUNCATE TABLE STG_MEMOTECH_PROV_FILING")
start_time = time.time()
timestamp = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
MOI_file_path = "Data\MOI.xlsx"
FILING_file_path = "Data\FILING.xlsx"
EXPRY_file_path = "Data\EXPRY.xlsx"
GRANTS_file_path = "Data\GRANTS.xlsx"
PROV_FILING_file_path = "Data\PROV_FILING.xlsx"
MOI = open_workbook(MOI_file_path)
FILING = open_workbook(FILING_file_path)
EXPRY = open_workbook(EXPRY_file_path)
GRANTS = open_workbook(GRANTS_file_path)
PROV_FILING = open_workbook(PROV_FILING_file_path)
MOI_sheet = MOI.sheet_by_index(0)
FILING_sheet = FILING.sheet_by_index(0)
EXPRY_sheet = EXPRY.sheet_by_index(0)
GRANT_sheet = GRANTS.sheet_by_index(0)
PROV_FILING_sheet = PROV_FILING.sheet_by_index(0)
first_row = 4
last_row_MOI = MOI_sheet.nrows
last_row_FILING = FILING_sheet.nrows
last_row_EXPRY = EXPRY_sheet.nrows
last_row_GRANTS = GRANT_sheet.nrows
last_row_PROV_FILING = PROV_FILING_sheet.nrows
for row in xrange(first_row,last_row_MOI):
    MOI_NUM = MOI_sheet.cell_value(row,0)
    ATTORNEY_NM = MOI_sheet.cell_value(row,1)
    MOI_REC_STA_TXT = MOI_sheet.cell_value(row,2)
    MOI_STA_TXT = MOI_sheet.cell_value(row,3)
    MOI_OPEN_DT = MOI_sheet.cell_value(row,4)
    PGM_NM = MOI_sheet.cell_value(row,5)
    THER_AREA_NM = MOI_sheet.cell_value(row,6)
    ORGL_IP_SITE_NM = MOI_sheet.cell_value(row,7)
    IP_SITE_NM = MOI_sheet.cell_value(row,8)
    RSH_CNTR_NM = MOI_sheet.cell_value(row,9)
    DIV_TXT = MOI_sheet.cell_value(row,10)
    TITL_TXT = MOI_sheet.cell_value(row,11)
    IVNTR_LIST_TXT = MOI_sheet.cell_value(row,12)
    SYS_INRT_TS = timestamp
    SYS_INRT_BY = 'infocenteradmin'
    SYS_SRC_NM = 'Memotech'
    target.execute("Insert into STG_MEMOTECH_MOI \
    (MOI_NUM, ATTORNEY_NM, MOI_REC_STA_TXT, MOI_STA_TXT, MOI_OPEN_DT, PGM_NM, THER_AREA_NM, ORGL_IP_SITE_NM, IP_SITE_NM, RSH_CNTR_NM, DIV_TXT, TITL_TXT, IVNTR_LIST_TXT, SYS_INRT_TS, SYS_INRT_BY, SYS_SRC_NM)\
    VALUES \
    ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
    %(MOI_NUM, ATTORNEY_NM, MOI_REC_STA_TXT, MOI_STA_TXT, MOI_OPEN_DT, PGM_NM, THER_AREA_NM, ORGL_IP_SITE_NM, IP_SITE_NM, RSH_CNTR_NM, DIV_TXT, TITL_TXT, IVNTR_LIST_TXT, SYS_INRT_TS, SYS_INRT_BY, SYS_SRC_NM))
    db.commit()
for row in xrange(first_row,last_row_FILING):
    DOCKET_NUM = FILING_sheet.cell_value(row,0)
    FILING_TYPE_TXT = FILING_sheet.cell_value(row,1)
    CTRY_NM = FILING_sheet.cell_value(row,2)
    FILING_EVNT_TXT = FILING_sheet.cell_value(row,3)
    LCL_FILING_PERFORMED_DT = FILING_sheet.cell_value(row,4)
    CUR_STA_TXT = FILING_sheet.cell_value(row,5)
    FILING_NUM = FILING_sheet.cell_value(row,6)
    FILING_DT = FILING_sheet.cell_value(row,7)
    GRNT_DT = FILING_sheet.cell_value(row,8)
    PRCR_AGNT_NM = FILING_sheet.cell_value(row,9)
    OWNR_TXT = FILING_sheet.cell_value(row,10)
    LICENSEE_TXT = FILING_sheet.cell_value(row,10)
    EXPRY_DT = FILING_sheet.cell_value(row,10)
    RANK_TXT = FILING_sheet.cell_value(row,11)
    ATTORNEY_NM = FILING_sheet.cell_value(row,12)
    PGM_NM = FILING_sheet.cell_value(row,13)
    THER_AREA_NM = FILING_sheet.cell_value(row,14)
    DIV_TXT = FILING_sheet.cell_value(row,15)
    target.execute("INSERT INTO STG_MEMOTECH_FILING\
    (DOCKET_NUM, FILING_TYPE_TXT, CTRY_NM, FILING_EVNT_TXT, LCL_FILING_PERFORMED_DT, CUR_STA_TXT, FILING_NUM, FILING_DT, GRNT_DT, PRCR_AGNT_NM, OWNR_TXT, LICENSEE_TXT, EXPRY_DT, RANK_TXT, ATTORNEY_NM, PGM_NM, THER_AREA_NM, DIV_TXT, SYS_INRT_TS,SYS_INRT_BY,SYS_SRC_NM)\
    VALUES \
    ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
    %(DOCKET_NUM, FILING_TYPE_TXT, CTRY_NM, FILING_EVNT_TXT, LCL_FILING_PERFORMED_DT, CUR_STA_TXT, FILING_NUM, FILING_DT, GRNT_DT, PRCR_AGNT_NM, OWNR_TXT, LICENSEE_TXT, EXPRY_DT, RANK_TXT, ATTORNEY_NM, PGM_NM, THER_AREA_NM, DIV_TXT, timestamp,'infocenteradmin','Memotech'))
    db.commit()

for row in xrange(first_row,last_row_EXPRY):
    DOCKET_NUM = EXPRY_sheet.cell_value(row,0)
    FILING_TYPE_TXT = EXPRY_sheet.cell_value(row,1)
    CTRY_NM = EXPRY_sheet.cell_value(row,2)
    EXPR_EVNT_TYPE_TXT = EXPRY_sheet.cell_value(row,3)
    EXPR_PERFORMED_DT = EXPRY_sheet.cell_value(row,4)
    CUR_STA_TXT = EXPRY_sheet.cell_value(row,5)
    FILING_NUM = EXPRY_sheet.cell_value(row,6)
    FILING_DT = EXPRY_sheet.cell_value(row,7)
    GRNT_DT = EXPRY_sheet.cell_value(row,8)
    PRCR_AGNT_NM = EXPRY_sheet.cell_value(row,9)
    OWNR_TXT = EXPRY_sheet.cell_value(row,10)
    LICENSEE_TXT = EXPRY_sheet.cell_value(row,11)
    EXPRY_DT = EXPRY_sheet.cell_value(row,12)
    RANK_TXT = EXPRY_sheet.cell_value(row,13)
    ATTORNEY_NM = EXPRY_sheet.cell_value(row,14)
    PGM_NM = EXPRY_sheet.cell_value(row,15)
    THER_AREA_NM = EXPRY_sheet.cell_value(row,16)
    DIV_TXT = EXPRY_sheet.cell_value(row,17)
    target.execute("INSERT INTO STG_MEMOTECH_EXPRY \
    (DOCKET_NUM, FILING_TYPE_TXT, CTRY_NM, EXPR_EVNT_TYPE_TXT, EXPR_PERFORMED_DT, CUR_STA_TXT, FILING_NUM, FILING_DT, GRNT_DT, PRCR_AGNT_NM, OWNR_TXT, LICENSEE_TXT, EXPRY_DT, RANK_TXT, ATTORNEY_NM, PGM_NM, THER_AREA_NM, DIV_TXT, SYS_INRT_TS, SYS_INRT_BY, SYS_SRC_NM)\
    VALUES \
    ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
    %(DOCKET_NUM, FILING_TYPE_TXT, CTRY_NM, EXPR_EVNT_TYPE_TXT, EXPR_PERFORMED_DT, CUR_STA_TXT, FILING_NUM, FILING_DT, GRNT_DT, PRCR_AGNT_NM, OWNR_TXT, LICENSEE_TXT, EXPRY_DT, RANK_TXT, ATTORNEY_NM, PGM_NM, THER_AREA_NM, DIV_TXT, timestamp,'infocenteradmin','Memotech'))
    db.commit()

for row in xrange(first_row,last_row_GRANTS):
    DOCKET_NUM = GRANT_sheet.cell_value(row,0)
    CTRY_NM = GRANT_sheet.cell_value(row,1)
    FILING_TYPE_TXT = GRANT_sheet.cell_value(row,2)
    CUR_STA_TXT = GRANT_sheet.cell_value(row,3)
    FILING_DT = GRANT_sheet.cell_value(row,4)
    FILING_NUM = GRANT_sheet.cell_value(row,5)
    GRNT_DT = GRANT_sheet.cell_value(row,6)
    GRNT_NUM = GRANT_sheet.cell_value(row,7)
    EXPRY_DT = GRANT_sheet.cell_value(row,8)
    PGM_NM = GRANT_sheet.cell_value(row,9)
    THER_AREA_NM = GRANT_sheet.cell_value(row,10)
    OWNR_TXT = GRANT_sheet.cell_value(row,11)
    DIV_TXT = GRANT_sheet.cell_value(row,12)
    ATTORNEY_AGNT_NM = GRANT_sheet.cell_value(row,13)
    TITL_TXT = GRANT_sheet.cell_value(row,14)
    target.execute("INSERT INTO STG_MEMOTECH_GRNT\
    (DOCKET_NUM, CTRY_NM, FILING_TYPE_TXT, CUR_STA_TXT, FILING_DT, FILING_NUM, GRNT_DT, GRNT_NUM, EXPRY_DT, PGM_NM, THER_AREA_NM, OWNR_TXT, DIV_TXT, ATTORNEY_AGNT_NM, TITL_TXT, SYS_INRT_TS, SYS_INRT_BY,SYS_SRC_NM)\
    VALUES\
    ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
    %(DOCKET_NUM, CTRY_NM, FILING_TYPE_TXT, CUR_STA_TXT, FILING_DT, FILING_NUM, GRNT_DT, GRNT_NUM, EXPRY_DT, PGM_NM, THER_AREA_NM, OWNR_TXT, DIV_TXT, ATTORNEY_AGNT_NM, TITL_TXT, timestamp,'infocenteradmin','Memotech'))
    db.commit()

for row in xrange(first_row,last_row_PROV_FILING):
    DOCKET_NUM = PROV_FILING_sheet.cell_value(row,0)
    FILING_TYPE_TXT = PROV_FILING_sheet.cell_value(row,1)
    CTRY_NM = PROV_FILING_sheet.cell_value(row,2)
    FILING_EVNT_TXT = PROV_FILING_sheet.cell_value(row,3)
    FILING_PERFORMED_DT = PROV_FILING_sheet.cell_value(row,4)
    CUR_STA_TXT = PROV_FILING_sheet.cell_value(row,5)
    FILING_NUM = PROV_FILING_sheet.cell_value(row,6)
    FILING_DT = PROV_FILING_sheet.cell_value(row,7)
    PRCR_AGNT_NM = PROV_FILING_sheet.cell_value(row,8)
    OWNR_TXT = PROV_FILING_sheet.cell_value(row,9)
    LICENSEE_TXT = PROV_FILING_sheet.cell_value(row,10)
    RANK_TXT = PROV_FILING_sheet.cell_value(row,11)
    ATTORNEY_NM = PROV_FILING_sheet.cell_value(row,12)
    PGM_NM = PROV_FILING_sheet.cell_value(row,13)
    THER_AREA_NM = PROV_FILING_sheet.cell_value(row,14)
    DIV_TXT = PROV_FILING_sheet.cell_value(row,15)
    target.execute("INSERT INTO STG_MEMOTECH_PROV_FILING\
    (DOCKET_NUM, FILING_TYPE_TXT, CTRY_NM, FILING_EVNT_TXT, FILING_PERFORMED_DT, CUR_STA_TXT, FILING_NUM, FILING_DT, PRCR_AGNT_NM, OWNR_TXT, LICENSEE_TXT, RANK_TXT, ATTORNEY_NM, PGM_NM, THER_AREA_NM, DIV_TXT,SYS_INRT_TS, SYS_INRT_BY,SYS_SRC_NM)\
    VALUES \
    ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
    %(DOCKET_NUM, FILING_TYPE_TXT, CTRY_NM, FILING_EVNT_TXT, FILING_PERFORMED_DT, CUR_STA_TXT, FILING_NUM, FILING_DT, PRCR_AGNT_NM, OWNR_TXT, LICENSEE_TXT, RANK_TXT, ATTORNEY_NM, PGM_NM, THER_AREA_NM, DIV_TXT,timestamp,'infocenteradmin','Memotech'))
    db.commit()
