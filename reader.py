import csv
import dataclasses
from dataclasses import dataclass
from typing import List


# TODO: WILL BE REMOVED JANEK TAKE CARE

@dataclass
class Entry:
    def __post_init__(self):
        for field in dataclasses.fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                setattr(self, field.name, field.type(value))


@dataclass
class TestEntry(Entry):
    point: int
    x: float
    y: float
    RSSI_A: int
    RSSI_B: int
    RSSI_C: int


@dataclass
class DatabaseEntry(Entry):
    x: float
    y: float
    RSSI_A: int
    RSSI_B: int
    RSSI_C: int


@dataclass
class PathlossEntry(Entry):
    distance: float
    RSSI: int
    point: int


class ScenarioData:
    def __init__(self, path_loss, tests, database):
        self.path_loss: List[PathlossEntry] = path_loss
        self.tests: List[TestEntry] = tests
        self.database: List[DatabaseEntry] = database


def loadData(db_filename: str, path_filename: str, tests_filename: str) -> ScenarioData:
    database = []
    with open(db_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            database.append(DatabaseEntry(*row))

    pathloss = []
    with open(path_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            pathloss.append(PathlossEntry(*row))

    tests = []
    with open(tests_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            tests.append(TestEntry(*row))

    return ScenarioData(pathloss, tests, database)
