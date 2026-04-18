class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])
        print(self.map)        

    def get(self, key: str, timestamp: int) -> str:
        timestamps=[element[0] for element in self.map[key]]
        values=[element[1] for element in self.map[key] if element[0] <= timestamp]
        if values:
            if timestamp in timestamps:
                return values[timestamps.index(timestamp)]
            else:
                return values[-1]
        return ""