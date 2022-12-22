class PresenceAnalyzer:

    def __init__(self, attendancelist: list):
        self.attendancelist = attendancelist
        self.__match_workshop = []

    def Watched2WorkshopsFollowed(self):

        for i in range(1, len(self.attendancelist)):
            arr_id = self.attendancelist[i].split()

            for id in arr_id:
                match_id = self.attendancelist[i-1].find(id)

                if match_id != -1 and not id in self.__match_workshop:
                    self.__match_workshop.append(id)

                else:
                    pass

        return sorted(self.__match_workshop)
