import tensorflow as tf

from paths.path import dir_path


class NumberModel(object):
    def __init__(self):
        pass
    def hook(self):
        self.create_model()

    def create_model(self):

        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=5)
        test_loss, test_acc = model.evaluate(x_test, y_test)
        print('테스트 정확도:', test_acc)
        file_name = dir_path('number')+'r/save/number_model.h5'
        model.save(file_name)
        print(f'Model Save in {file_name}')

number_menu = ["Exit", #0
                "hook",#1
             ]
number_lambda = {
    "1" : lambda x: x.create_model(),
}

if __name__ == '__main__':
    number= NumberModel()


    while True:
        [print(f"{i}. {j}") for i, j in enumerate(number_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                number_lambda[menu](number)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")
