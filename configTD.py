GetCalcTDMappingConfig = {
    'table': 'CalcTDMapping',
    'fields': 'id, SignalASourceTable, SignalIDA, TimeLagSignalA, SignalBSourceTable, SignalIDB, TimeLagSignalB, SignalCSourceTable, SignalIDC, TimeLagSignalC, UpdateParents, HierarchyID, Multiplier, EQUATION, TimeAggr, TargetCalcSignal, LastSuccess, ActiveQuery'
}

GetTDDataConfig = {
    'table': 'TDData',
    'fields': 'id, QDateTime, SignalID, EntityID, Value'
}

GetCalcTDDataConfig = {
    'table': 'CalcTDData',
    'fields': 'id, QDateTime, SignalID, EntityID, Value'
}

GetHierarchyConfig = {
    'table': 'Hierarchy',
    'fields': 'id, HierarchyID, Name, ChildID, ParentID'
}

GetEntityConfig = {
    'table': 'Entity',
    'fields': 'id, EntityName, FieldName, Location, Type'
}

GetLastSuccess = {
    'table': 'CalcTDMapping',
    'fields': 'LastSuccess'
}
