class AnalisadorDePresenca:

    def __init__(self, atas: list):
        self.atas = atas
        self.__match_workshop = []

    def ColaboradoresQueViram2WorkshopsSeguidos(self):

        for i in range(1, len(self.atas)):
            arr_id = self.atas[i].split()

            for id in arr_id:
                match_id = self.atas[i-1].find(id)

                if match_id != -1 and not id in self.__match_workshop:
                    self.__match_workshop.append(id)

                else:
                    pass

        return sorted(self.__match_workshop)
