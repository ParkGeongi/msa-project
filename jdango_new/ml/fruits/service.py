
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.keras import layers
import tensorflow as tf
import seaborn as sns
from tensorflow import keras
from keras.callbacks import ModelCheckpoint

from paths.path import dir_path


class FruitsService:
    def __init__(self):
        global imagepath, model,batch_size, img_height, img_width, train_ds_pre, val_ds_pre,test_ds_pre,test_ds1_pre, train_ds, val_ds,test_ds, class_names, num_classes

        imagepath = dir_path('fruits')+r'\data\Training\Apple Golden 3\0_100.jpg'
        train_dir = dir_path('fruits')+ 'r\data\Training'
        test_dir = dir_path('fruits') + 'r\data\Test'
        batch_size = 32
        img_height = 100
        img_width = 100

        train_ds_pre = tf.keras.preprocessing.image_dataset_from_directory(
            train_dir,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        val_ds_pre = tf.keras.preprocessing.image_dataset_from_directory(
            train_dir,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        class_names = train_ds_pre.class_names

        print(class_names)

        test_ds_pre = tf.keras.preprocessing.image_dataset_from_directory(
            test_dir,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        test_ds1_pre = tf.keras.preprocessing.image_dataset_from_directory(
            test_dir,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size,
            shuffle=False)
        BUFFER_SIZE = 10000
        AUTOTUNE = tf.data.experimental.AUTOTUNE
        num_classes = 5
        train_ds = train_ds_pre.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds_pre.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = test_ds_pre.cache().prefetch(buffer_size=AUTOTUNE)

    def hook(self):
        self.img_plot()
        self.img_plot2()
        self.graph_test()
        self.confusion_matrix()

    def img_plot(self):
        img = tf.keras.preprocessing.image.load_img(imagepath)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    def img_plot2(self):

        y = np.concatenate([y for x, y in test_ds_pre], axis=0)
        print(y)
        y1 = np.concatenate([y for x, y in test_ds1_pre], axis=0)
        print(y1)
        x = np.concatenate([x for x, y in test_ds1_pre], axis=0)
        print(x[0])
        plt.figure(figsize=(3, 3))
        plt.imshow(x[0].astype("uint8"))
        plt.title(class_names[y1[0]])
        plt.axis("off")
        plt.show()
        plt.figure(figsize=(3, 3))
        plt.imshow(x[-1].astype("uint8"))
        plt.title(class_names[y1[-1]])
        plt.axis("off")
        plt.show()


    def create_model(self):

        model = tf.keras.Sequential([
            layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Flatten(),
            layers.Dense(500, activation='relu'),
            layers.Dropout(.50),
            layers.Dense(num_classes, activation='softmax')
        ])
        print(model.summary())
        model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy'])
        checkpointer = ModelCheckpoint(dir_path('fruits')+r'\save\CNNClassifier.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, monitor='val_accuracy',
                                                          restore_best_weights=True)
        epochs = 20

        history = model.fit(
            train_ds,
            batch_size=batch_size,
            validation_data=val_ds,
            epochs=epochs,
            callbacks=[checkpointer, early_stopping_cb]
        )
        return model ,history
    def graph_test(self):
        model, history = self.create_model()
        len(history.history['val_accuracy'])

        acc = history.history['accuracy']  # 모델의 학습 정확도를 변수 acc에 저장
        val_acc = history.history['val_accuracy']  # 모델의 검증 정확도를 변수 val_acc에 저장

        loss = history.history['loss']  # 모델의 학습 손실을 변수 loss에 저장
        val_loss = history.history['val_loss']  # 모델의 검증 손실을 변수 val_loss에 저장

        # epochs가 14회가 아닌 다른 결과(예:10회)로 나오면 아래 줄 14를 해당 숫자인 10로 바꿔주야 함에 유의
        epochs_range = range(1, len(loss) + 1)  # epochs가 14회까지만 수행된 것을 반영

        # 학습 정확도와 검증 정확도를 그리기
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        # 학습 손실와 검증 손실을 그리기
        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

        model.load_weights(r'C:\Users\AIA\project\jdango_new\ml\fruits\save\CNNClassifier.h5')

        test_loss, test_acc = model.evaluate(test_ds)

        print("test loss: ", test_loss)
        print()
        print("test accuracy: ", test_acc)
        predictions = model.predict(test_ds1_pre)
        score = tf.nn.softmax(predictions[0])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )
        score = tf.nn.softmax(predictions[-1])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )


    def confusion_matrix(self):
        model = tf.keras.Sequential([
            layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Flatten(),
            layers.Dense(500, activation='relu'),
            layers.Dropout(.50),
            layers.Dense(num_classes, activation='softmax')
        ])
        model.load_weights(dir_path('fruits')+r'\save\CNNClassifier.h5')
        predictions = model.predict(test_ds)

        y1 = np.concatenate([y for x, y in test_ds], axis=0)
        #predictions = np.array(predictions)
        predictions = [np.argmax(tf.nn.softmax(predictions[i])) for i in range(len(predictions))]
        print(np.array(predictions))
        print(y1)

        matrix = confusion_matrix(predictions, y1)
        sns.heatmap(matrix, annot=True, cmap='Blues')
        plt.show()

if __name__ == '__main__':


    s = FruitsService()
    s.confusion_matrix()