from ast import literal_eval

from domains import AnalisadorDePresenca


if __name__ == '__main__':
    arr_atas = literal_eval(input())
    analisador_de_presenca = AnalisadorDePresenca(arr_atas)
    print(analisador_de_presenca.ColaboradoresQueViram2WorkshopsSeguidos())
