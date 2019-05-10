# AlexNet

## 2 fully connected layers - tanh activation - without dropout
Training accuracy  = 0.8950
Training loss = 0.3064

Validation accuracy = 0.7605
Validation loss = 0.7923

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

## 3 fully connected layers - tanh activation - with dropout
Training accuracy = 0.8799
Training loss = 0.3419

Validation accuracy = 0.7599
Validation loss = 0.8001

Test accuracy = 0.8001
Test loss = 0.7599

Acc graph name = acc_3-fully-tanh_w_dropout.png
Loss graph name =  loss_3-fully-tanh_w_dropout.png

## 3 fully connected layers - relu activation - with dropout
Training accuracy = 0.8376
Training loss = 0.4804

Validation accuracy = 0.7420
Validation loss = 0.8889

Test accuracy = 0.742
Test loss = 0.8889

Acc graph name = acc_3-fully-relu_w_dropout.png
Loss graph name =  loss_3-fully-relu_w_dropout.png


## 3 fully connected layers - relu activation - with dropout - with normalization
Training accuracy = 0.8231
Training loss = 0.5256

Validation accuracy = 0.7416
Validation loss = 0.8409

Test accuracy = 0.7416
Test loss = 0.8409

Acc graph name = acc_3-fully-relu-norm_w_dropout.png
Loss graph name =  loss_3-fully-relu-norm_w_dropout.png


## 3 fully connected layers - relu activation - without dropout - with normalization
Training accuracy = 0.9240
Training loss = 0.2218

Validation accuracy = 0.7444
Validation loss = 0.9206

Test accuracy = 0.7444
Test loss = 0.9206

Acc graph name = acc_3-fully-relu-norm_w_dropout.png
Loss graph name =  loss_3-fully-relu-norm_w_dropout.png

## 3 fully connected layer - relu - with drop - with normalization - with agumentation (Final model)
training acc =  0.8193
training loss = 0.5420

best validation acc = 0.7961
final acc = 0.7878
final loss = 0.6532

## Final model 25 - 50 epochs
Training accuracy = 0.8724
Training loss = 0.3938

best validation = 0.8396
final acc = 0.8297
final loss = 0.5669

## final model
test acc = 0.7538
test loss = 1.4581

training loss = 0.0681
training acc = 0.9800



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
