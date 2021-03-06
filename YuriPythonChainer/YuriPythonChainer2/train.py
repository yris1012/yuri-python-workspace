import os
import numpy as np
import chainer
from chainer import optimizers,serializers
import chainer.functions as F
from model import myLinear

def train_myLinear(n_epoch):
  # create save model dir
  save_dir = './myModel_Linear'
  if not os.path.exists(save_dir):
    os.mkdir(save_dir)

  # setup model
  my_model = myLinear(k_num = 10) # k_numは0~9の10個
  optimizer = optimizers.Adam()
  optimizer.setup(my_model)
  # STEP 1---------------------------------------------------
  # load MNIST
  train, test = chainer.datasets.get_mnist() #it takes time...
  train_num = len(train)
  test_num = len(test)
  # ---------------------------------------------------------
  for epoch in range(0, n_epoch):
    for i in range(0, train_num):
      # STEP 2 ----------------------------------------------
      input,target = train[i] # img data(np.float32) for input, label(int) for target
      # reshape each datum
      input = input.reshape(1, input.shape[0])
      target = np.array([target], np.int32)
      # input to model
      output = my_model(input)
      # -----------------------------------------------------
      # STEP 3 ----------------------------------------------
      loss = F.softmax_cross_entropy(output, target)
      accuracy = F.accuracy(output, target)
      # backward model
      my_model.cleargrads()
      loss.backward()
      optimizer.update()
      # -----------------------------------------------------
      print("epoch:{} {}/{}".format(epoch+1,i+1,train_num))
      print("\t loss:{} accuracy:{}".format(loss.data, accuracy.data))
  
  # save trained model
  serializers.save_npz('{}/epoch{}_myLinearmodel.npz'.format(save_dir, n_epoch), my_model)


if __name__ == '__main__':
  train_myLinear(n_epoch = 100)