from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import plot_model
import matplotlib.pyplot as plt
import os

batch_size = 32
num_classes = 10
epochs = 3
save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'keras_cifar10_trained_model.h5'

(x_train,y_train), (x_test,y_test) = cifar10.load_data()
print('x_train shape:',x_train.shape)
print(x_train.shape[0], ' train samples')
print(x_test.shape[0], ' test samples')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
#Layer 1
model.add(Conv2D(32,(3,3), padding = 'same',input_shape=x_train.shape[1:]))
model.add(Activation('relu'))

#Layer 2
model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))

#Layer 3
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

#Layer 4
model.add(Conv2D(64, (3, 3), padding = 'same'))
model.add(Activation('relu'))

#Layer 5
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))

#Layer 6
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Layer 7
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))

#Layer 8
model.add(Dense(num_classes))
model.add(Activation('softmax'))

opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

history = model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs,
validation_data = (x_test,y_test) , shuffle = True)


if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s ' % model_path)

# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plot_model(model, to_file='model.png')
