from reader import loadData

data = loadData("Database_Scenario1 - Zigbee.csv", "Pathloss_Scenario1 - Zigbee.csv", "Tests_Scenario1 - Zigbee.csv")


print(data.database, data.tests,data.path_loss)
