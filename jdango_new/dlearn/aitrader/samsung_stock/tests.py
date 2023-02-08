from dlearn.aitrader.samsung_stock.models import Dnn_Model, Dnn_Ensemble_Model, Lstm_Model, Lstm_Ensemble_Model

menu = ["Exit",
        "Dnn Model",
        "Dnn Ensemble",
        "Lstm Model",
        "Lstm Ensemble"]
if __name__ == '__main__':

    while True:
        [print(f"{i}. {j}") for i, j in enumerate(menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                if menu == "1": Dnn_Model().create()
                elif menu == "2": Dnn_Ensemble_Model().create()
                elif menu == "3": Lstm_Model().create()
                elif menu == "4": Lstm_Ensemble_Model().create()
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")