import odbcFunctions    

server = '172.20.1.14' 
database = 'msdb' 
username = 'vthiru' 
password = 'precise*3984052'

conn = odbcFunctions.databaseConnect(
    server,
    database,
    username,
    password
    )

odbcFunctions.parkedInEventDisable(conn,'20220107','160000')
odbcFunctions.parkedInEventEnable(conn,'20220107','160000')

odbcFunctions.databaseDisconnect(conn)