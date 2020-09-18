import mysql.connector
import configTD
from env import HOST, NAME, USER, PASSWORD

class CalcModel:

    def __init__(self):
        pass
    
    # connection with Database
    def dbconnect(self):
            self.conn = mysql.connector.connect(host=HOST,
                                                database=NAME,
                                                user=USER,
                                                password=PASSWORD)
            return self.conn
    
    #get all data from CalcTDMapping table
    def getCalcTDMapping(self):
        mycursor = self.conn.cursor()
        mytable = configTD.GetCalcTDMappingConfig["table"]
        myfields = configTD.GetCalcTDMappingConfig["fields"]
        mywhere = ""
        mysql = "SELECT " + myfields + " FROM " + mytable + mywhere
        mycursor.execute(mysql)
        myresult = mycursor.fetchall()
        return myresult

    #get all data from CalcTDData table
    def getCalcTDData(self):
        mycursor = self.conn.cursor()
        mytable = configTD.GetCalcTDDataConfig["table"]
        myfields = configTD.GetCalcTDDataConfig["fields"]
        mywhere = ""
        mysql = "SELECT " + myfields + " FROM " + mytable + mywhere
        mycursor.execute(mysql)
        myresult = mycursor.fetchall()
        return myresult
    
    #get all data from TDData table
    def getTDData(self):
        mycursor = self.conn.cursor()
        mytable = configTD.GetTDDataConfig["table"]
        myfields = configTD.GetTDDataConfig["fields"]
        mywhere = ""
        mysql = "SELECT " + myfields + " FROM " + mytable + mywhere
        mycursor.execute(mysql)
        myresult = mycursor.fetchall()
        return myresult

    #get all data from Entity table
    def getEntity(self):
        mycursor = self.conn.cursor()
        mytable = configTD.GetEntityConfig["table"]
        myfields = configTD.GetEntityConfig["fields"]
        mywhere = ""
        mysql = "SELECT " + myfields + " FROM " + mytable + mywhere
        mycursor.execute(mysql)
        myresult = mycursor.fetchall()
        return myresult

    #get all data from Hierarchy table 
    def getHierarchy(self):
        mycursor = self.conn.cursor()
        mytable = configTD.GetHierarchyConfig["table"]
        myfields = configTD.GetHierarchyConfig["fields"]
        mysql = "SELECT " + myfields + " FROM " + mytable
        mycursor.execute(mysql)
        myresult = mycursor.fetchall()
        return myresult



    """ Get signals from both tables"""

    def getSignalFromTDData(self, SignalID, EntityID, QDateTime):
        mycursor = self.conn.cursor()
        mytable = configTD.GetTDDataConfig["table"]
        myfields = configTD.GetTDDataConfig["fields"]
        mywhere = "SignalID = %s AND EntityID = %s AND QDateTime > %s"
        mysql = "SELECT " + myfields + " FROM " + mytable + " WHERE " + mywhere
        mycursor.execute(mysql, (SignalID, EntityID, QDateTime, ))
        myresult = mycursor.fetchall()
        return myresult

    def getSignalFromCalcTDData(self, SignalID, EntityID, QDateTime):
        mycursor = self.conn.cursor()
        mytable = configTD.GetCalcTDDataConfig["table"]
        myfields = configTD.GetCalcTDDataConfig["fields"]
        mywhere = "SignalID = %s AND EntityID = %s AND QDateTime > %s"
        mysql = "SELECT " + myfields + " FROM " + mytable + " WHERE " + mywhere
        mycursor.execute(mysql, (SignalID, EntityID, QDateTime, ))
        myresult = mycursor.fetchall()
        return myresult

    def getLastSuccess(self):
        mycursor = self.conn.cursor()
        mytable = configTD.GetLastSuccess["table"]
        myfields = configTD.GetLastSuccess["fields"]
        mysql = "SELECT " + myfields + " FROM " + mytable
        mycursor.execute(mysql)
        myresult = mycursor.fetchall()
        return myresult