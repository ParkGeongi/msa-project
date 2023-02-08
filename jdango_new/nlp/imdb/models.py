import tensorflow as tf
from keras.callbacks import ModelCheckpoint, EarlyStopping

from keras_preprocessing.sequence import pad_sequences
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow.keras.layers
from keras.layers import Dense
from keras import Sequential
from tensorflow.keras.optimizers import RMSprop

class ImdbModel(object):

    def __init__(self):
        global train_input,train_target,test_input,test_target, val_input,val_target, train_oh, val_oh
        (train_input, train_target), (test_input, test_target) = tf.keras.datasets.imdb.load_data(num_words=500)
        train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2,
                                                                            random_state=42)

        train_seq = pad_sequences(train_input, maxlen=100)
        val_seq = pad_sequences(val_input, maxlen=100)
        train_oh = tf.keras.utils.to_categorical(train_seq)
        val_oh = tf.keras.utils.to_categorical(val_seq)


    def hook(self):
        self.create_model()


    def create_model(self):


        sample_length = 100
        freq_word = 500
        model = Sequential()
        model.add(tensorflow.keras.layers.SimpleRNN(8, input_shape=(sample_length, freq_word)))
        model.add(Dense(1, activation= 'sigmoid'))
        model.summary()
        model.compile( loss='binary_crossentropy', optimizer=RMSprop(learning_rate=1e-4), metrics=['accuracy'])

        checkpoint_cb = ModelCheckpoint('best-simplernn-model.h5', save_best_only=True)
        early_stopping_cb = EarlyStopping(patience=3, restore_best_weights=True)
        history = model.fit(train_oh, train_target, epochs=100, batch_size=64,
                                 validation_data=(val_oh, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train', 'val'])
        plt.show()

    def fit(self):


        self.model.complie(optimizer = RMSprop(learning_rate=1e-04), loss = 'binary_crossentropy', metrics = ['accuracy'])
        checkpoint_cb = ModelCheckpoint('best-simplernn-model.h5', save_best_only = True)
        early_stopping_cb = EarlyStopping(patience = 3,restore_best_weights = True)
        history = self.model.fit(train_oh,train_target,epochs = 100,batch_size = 64, validation_data =(val_oh,val_target),callbacks = [checkpoint_cb,early_stopping_cb])

        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train','val'])
        plt.show()


imdb_menu = ["Exit",  # 0
             "hook",  # 1
             ]
imdb_lambda = {
    "1": lambda x: x.hook(),
}

if __name__ == '__main__':
    imdb =ImdbModel()

    while True:
        [print(f"{i}. {j}") for i, j in enumerate(imdb_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                imdb_lambda[menu](imdb)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")

