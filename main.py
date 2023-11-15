from reader import loadData
from visualize import *

data = loadData("Database_Scenario1 - Zigbee.csv", "Pathloss_Scenario1 - Zigbee.csv", "Tests_Scenario1 - Zigbee.csv")

visualize_data(data)

print(data.database, data.tests,data.path_loss)
