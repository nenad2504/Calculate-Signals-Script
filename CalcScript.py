import CalcModel as CM
import configTD
from date import getLastRunInFile, getDates, storeLastRunInFile
from datetime import datetime, date
from formula import calculateFormula

#DB connection
calcModelObject = CM.CalcModel()
myconn = calcModelObject.dbconnect()

# get all rows from CalcTDMapping
CalcTDMappings = calcModelObject.getCalcTDMapping()

# get all rows from TDData
TDDatas = calcModelObject.getTDData()
for TDData in TDDatas:
    TDId = TDData[0]
    TDQDateTime = TDData[1]
    TDSignalID = TDData[2]
    TDEntityID = TDData[3]
    TDValue = TDData[4]

# get all rows from CalcTDData
CalcTDDatas = calcModelObject.getCalcTDData()
for CalcTDData in CalcTDDatas: 
    CalcId = CalcTDData[0] 
    CalcQDateTime = CalcTDData[1]
    CalcSignalID = CalcTDData[2]
    CalcEntityID = CalcTDData[3]
    CalcValue = CalcTDData[4]


dateFormat = '%Y-%m-%d'
lastRun = getLastRunInFile()
dateTimeObj = datetime.now()
currentDay = dateTimeObj.strftime(dateFormat)

dates = getDates(lastRun, currentDay)
# for date in dates:
#     print(date)

# storeLastRunInFile(date)

# loop over id and assign column name to variables
for CalcTDMapping in CalcTDMappings:
    Id = CalcTDMapping[0]
    SignalASourceTable = CalcTDMapping[1]
    SignalA = CalcTDMapping[2]
    TimeLagSignalA = CalcTDMapping[3]
    SignalBSourceTable = CalcTDMapping[4]
    SignalB = CalcTDMapping[5]
    TimeLagSignalB = CalcTDMapping[6]
    SignalCSourceTable = CalcTDMapping[7]
    SignalC = CalcTDMapping[8]
    TimeLagSignalC = CalcTDMapping[9]
    UpdateParents = CalcTDMapping[10]
    HierachyID = CalcTDMapping[11] 
    Multiplier = CalcTDMapping[12]
    EQUATION = CalcTDMapping[13]
    TimeAggr = CalcTDMapping[14]
    TargetCalcSignal = CalcTDMapping[15]
    LastSuccess = CalcTDMapping[16]
    ActiveQuery = CalcTDMapping[17]

    # 3. skip if ActiveQuery is False
    if not ActiveQuery:
        continue
    formulaParams = { }

    Hierarchies = calcModelObject.getHierarchy()
    for hierarchy in Hierarchies: 
        hId = hierarchy[0]
        hHierachyID = hierarchy[1]
        name = hierarchy[2]
        childID = hierarchy[3]
        parentID = hierarchy[4]

        # These signals are only for children entity
        """ SIGNAL A """
        if(SignalASourceTable == 'TDData'):
            # SignalA Only for children entities
            signalAtddata = calcModelObject.getSignalFromTDData(SignalA, childID, LastSuccess)
            signalAChildEnt = sum(float(sigAtd[4]) for sigAtd in signalAtddata)
            formulaParams['A'] = signalAChildEnt
            
            # SignalA Only for parents entities
            #Need if UpdateParent == True
            signalAtddata = calcModelObject.getSignalFromTDData(SignalA, parentID, LastSuccess)
            signalAParentEnt = sum(float(sigAtd[4]) for sigAtd in signalAtddata) 
                
                
        elif (SignalASourceTable == 'CalcTDData'): 

            # SignalA Only for children entities
            signalACalcTDData = calcModelObject.getSignalFromCalcTDData(SignalA, childID, LastSuccess)
            signalAChildEnt = resultSignalACalcTDData = sum(float(sigActd[4]) for sigActd in signalACalcTDData)
            formulaParams['A'] = signalAChildEnt
                
            # SignalA Only for parents entities
            #Need if UpdateParent == True
            signalACalcTDData = calcModelObject.getSignalFromCalcTDData(SignalA, parentID, LastSuccess)
            signalAParentEnt = resultSignalACalcTDData = sum(float(sigActd[4]) for sigActd in signalACalcTDData)
                
                
        """ SIGNAL B """
        if(SignalBSourceTable == 'TDData'):

            # SignalB Only for children entities
            signalBtddata = calcModelObject.getSignalFromTDData(SignalB, childID, LastSuccess)
            signalBChildEnt = sum(float(sigBtd[4]) for sigBtd in signalBtddata)
            formulaParams['B'] = signalBChildEnt

            # SignalB Only for parents entities
            #Need if UpdateParent == True
            signalBtddata = calcModelObject.getSignalFromTDData(SignalB, parentID, LastSuccess)
            signalBParentEnt = sum(float(sigBtd[4]) for sigBtd in signalBtddata)  
                
        elif (SignalBSourceTable == 'CalcTDData'): 

            # SignalB Only for children entities
            signalBCalcTDData = calcModelObject.getSignalFromCalcTDData(SignalB, childID, LastSuccess)
            signalBChildEnt = resultSignalBCalcTDData = sum(float(sigBctd[4]) for sigBctd in signalBCalcTDData)
            formulaParams['B'] = signalBChildEnt
            # print("SigB: " + str(SignalB) + " chID: " + str(childID) + " LSucc: " + str(LastSuccess)+ " Res: " + str(signalBChildEnt) + " ForRes: " + str(formulaParams['B']))
            # SignalB Only for parents entities
            #Need if UpdateParent == True
            signalBCalcTDData = calcModelObject.getSignalFromCalcTDData(SignalB, parentID, LastSuccess)
            signalBParentEnt = resultSignalBCalcTDData = sum(float(sigBctd[4]) for sigBctd in signalBCalcTDData)  


        """ SIGNAL C """
        if(SignalCSourceTable == 'TDData'):

            # SignalC Only for children entities
            signalCtddata = calcModelObject.getSignalFromTDData(SignalC, childID, LastSuccess)
            signalCChildEnt = sum(float(sigCtd[4]) for sigCtd in signalCtddata) 
            formulaParams['C'] = signalCChildEnt

            # SignalC Only for parents entities
            #Need if UpdateParent == True
            signalCtddata = calcModelObject.getSignalFromTDData(SignalC, parentID, LastSuccess)
            signalCParentEnt = sum(float(sigCtd[4]) for sigCtd in signalCtddata)
                
        elif (SignalCSourceTable == 'CalcTDData'): 
            # SignalC Only for children entities
            signalCCalcTDData = calcModelObject.getSignalFromCalcTDData(SignalC, childID, LastSuccess)
            signalCChildEnt = resultSignalCCalcTDData = sum(float(sigCctd[4]) for sigCctd in signalCCalcTDData)
            formulaParams['C'] = signalCChildEnt

            # SignalC Only for parents entities
            #Need if UpdateParent == True
            signalCCalcTDData = calcModelObject.getSignalFromCalcTDData(SignalC, parentID, LastSuccess)
            signalCParentEnt = resultSignalCCalcTDData = sum(float(sigCctd[4]) for sigCctd in signalCCalcTDData)

        if EQUATION is not None:
            equationResult = calculateFormula(EQUATION, formulaParams)
            if TimeAggr is None:
                CalcChildren = equationResult * Multiplier
                if UpdateParents == 1:
                    resultParent = []
                    formulaParams['A'] = signalAParentEnt
                    formulaParams['B'] = signalBParentEnt
                    formulaParams['C'] = signalCParentEnt
                    equationResult = calculateFormula(EQUATION, formulaParams)
                    CalcParent = equationResult * Multiplier
                    resultParent.append(CalcParent)
                    CalcParentResult = sum(resultParent)
                    if CalcParent == 0: # skip if the result is 0 
                        continue
                    # print(CalcParentResult)
                    
            else:
                resChildren = []
                CalcChildren = equationResult * Multiplier
                resChildren.append(CalcChildren)
                result =sum(resChildren)
                # print(result)
                if UpdateParents == 1:
                    resParent = []
                    formulaParams['A'] = signalAParentEnt
                    formulaParams['B'] = signalBParentEnt
                    formulaParams['C'] = signalCParentEnt
                    equationResult = calculateFormula(EQUATION, formulaParams)
                    CalcParents = equationResult * Multiplier
                    resParent.append(CalcParents)
                    CalcParentResult = sum(resParent)
                    if CalcParentResult == 0:  # skip if the result is 0 
                        continue
                    # print(CalcParentResult)

        # else:
        #     print('hello')