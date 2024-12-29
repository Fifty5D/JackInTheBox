import discord
from secret import USE_TEST_BOT

#====================
# Guild ID's. // Jack
#====================
GUILD_ID = 864441968776052747 if USE_TEST_BOT else 288446755219963914
GUILD = discord.Object(id=GUILD_ID)

#======================
# Channel ID's. // Jack
#======================
COMMENDATIONS_CHANNEL_ID = 1274979300386275328 if USE_TEST_BOT else 1109263109526396938
REPORT_LOG_CHANNEL_ID = 866938361628852224 if USE_TEST_BOT else 889752071815974952
UNIT_STAFF_CHANNEL_ID = 864442610613485590 if USE_TEST_BOT else 740368938239524995
ZEUS_FEEDBACK_CHANNEL_ID = 1295556674525855797 if USE_TEST_BOT else 1294336572342145207
STAFF_ADVISOR_CHANNEL_ID = 1322744163200139265 if USE_TEST_BOT else 962058109931638825

#===========================
# Special Role ID's. // Jack
#===========================
UNIT_STAFF_ROLE_ID = 864443672032706560 if USE_TEST_BOT else 655465074982518805
CURATOR_ROLE_ID = 977543359432380456 if USE_TEST_BOT else 392773303770677248
ZEUS_ROLE_ID = 977543532904583199 if USE_TEST_BOT else 796178478142849048
ZEUSINTRAINING_ROLE_ID = 1133852373836640306 if USE_TEST_BOT else 988950379330941050

#==============================
# Sigma Rank Role ID's. // Jack
#==============================
CANDIDATE_ROLE_ID = 1248923418372341770 if USE_TEST_BOT else 1237921006128205905
ASSOCIATE_ROLE_ID = 864443914668474399 if USE_TEST_BOT else 1237959079876493343
CONTRACTOR_ROLE_ID = 864443893852667932 if USE_TEST_BOT else 1237920226113491014
MERCENARY_ROLE_ID = 1248923647003983905 if USE_TEST_BOT else 1237921257467416628
TACTICIAN_ROLE_ID = 864443849342189577 if USE_TEST_BOT else 1237920649687863336
OPERATOR_ROLE_ID = 864443872003620874 if USE_TEST_BOT else 1237920430845722645
STRATEGIST_ROLE_ID = 864443819571019776 if USE_TEST_BOT else 1237920780927631420

#=======================================================
# Information for commend_candidate_tracking.py. // Jack
#=======================================================
OPERATION_KEYWORD = "has attended an operation"
TOTAL_OPERATIONS = 3