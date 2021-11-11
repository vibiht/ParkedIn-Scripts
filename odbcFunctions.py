import pandas
import numpy
import pyodbc

def databaseConnect(server,database,username,password):
    conn = pyodbc.connect('DRIVER={SQL Server};'
        'SERVER='+server+
        ';DATABASE='+database+
        ';UID='+username+
        ';PWD='+password
        )
    return conn

def databaseDisconnect(conn):
    conn.close()

def databaseSelect(conn, query):
    cursor = conn.cursor()
    cursor.execute(query) 
    return cursor.fetchall()

def parkedInEventEnable(conn, date, time):
    query ="USE [msdb];"
    print (query)
    cursor = conn.cursor()
    cursor.execute(query)
    query ="DECLARE @schedule_id int;"
    print (query)
    cursor = conn.cursor()
    cursor.execute(query) 
    query ="EXEC msdb.dbo.sp_add_jobschedule @job_id=N'a9910a3f-8cd7-4031-8ba5-510b087fea64', @name=N'"+date+"Disable', "\
    "@enabled=1, "\
    "@freq_type=1, "\
    "@freq_interval=1, "\
    "@freq_subday_type=0, "\
    "@freq_subday_interval=0, "\
    "@freq_relative_interval=0, "\
    "@freq_recurrence_factor=1, "\
    "@active_start_date="+date+", "\
    "@active_end_date=99991231, "\
    "@active_start_time="+time+", "\
    "@active_end_time=235959, "\
    "@schedule_id = @schedule_id;"
    print (query)
    cursor = conn.cursor()
    cursor.execute(query) 

def parkedInEventDisable(conn, date, time):
    query ="USE [msdb];"
    print (query)
    cursor = conn.cursor()
    cursor.execute(query) 
    query ="DECLARE @schedule_id int;"
    print (query)
    cursor = conn.cursor()
    cursor.execute(query) 
    query ="EXEC msdb.dbo.sp_add_jobschedule @job_id=N'992ecb67-64db-44b9-b3a9-b68189e8e5a5', @name=N'"+date+"Disable', "\
    "@enabled=1, "\
    "@freq_type=1, "\
    "@freq_interval=1, "\
    "@freq_subday_type=0, "\
    "@freq_subday_interval=0, "\
    "@freq_relative_interval=0, "\
    "@freq_recurrence_factor=1, "\
    "@active_start_date="+date+", "\
    "@active_end_date=99991231, "\
    "@active_start_time="+time+", "\
    "@active_end_time=235959, "\
    "@schedule_id = @schedule_id;"
    print (query)
    cursor = conn.cursor()
    cursor.execute(query) 