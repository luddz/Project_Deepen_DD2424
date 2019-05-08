# AlexNet

## 2 fully connected layers - tanh activation - without dropout
Training accuracy  = 0.8950
Training loss = 0.3064

Validation accuracy = 76.05
Validation loss = 0.79.23

Test accuracy = 0.7605
Test loss = 0.7923

Acc graph name = acc_2-fully-tanh-wo_dropout.png
Loss graph name =  loss_2-fully-tanh-wo_dropout.png

## 2 fully connected layers - tanh activation - with dropout
dropout of 40% -> model.add(dropout,0.4)
Training accuracy = 0.8626
Training loss = 0.3968

Validation accuracy = 0.7687
Validation loss = 0.7494

Test accuracy = 0.7494
Test loss = 0.7687

Acc graph name = acc_2-fully-tanh-w_dropout.png
Loss graph name =  loss_2-fully-tanh-w_dropout.png

## 3 fully connected layers - relu activation - without dropout
Training accuracy = 0.8837
Training loss = 0.3367

Validation accuracy = 0.7362
Validation loss = 0.9143

Test accuracy = 0.7362
Test loss = 0.9143

Acc graph name = acc_3-fully-relu_wo_dropout.png
Loss graph name =  loss_3-fully-relu_wo_dropout.png

## 4 fully connected layers - relu activation - with dropout
Training accuracy = 0.8376
Training loss = 0.4804

Validation accuracy = 0.7420
Validation loss = 0.8889

Test accuracy = 0.742
Test loss = 0.8889

Acc graph name = acc_3-fully-relu_w_dropout.png
Loss graph name =  loss_3-fully-relu_w_dropout.png

# Keras example CNN
The training is done on 10 epochs
## 0.25 dropout
Training accuracy = 0.6715
Training loss = 0.9418

Validation accuracy = 0.6684
Validation loss = 0.9454

Test accuracy = 0.6684
Test loss = 0.9454

Acc graph name = acc_keras_w025_dropout.png
Loss graph name = loss_keras_w025_dropout.png