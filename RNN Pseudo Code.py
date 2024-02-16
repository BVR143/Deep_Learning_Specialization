# let us define a RNN class 
import tensorflow as tf 
class MyRNNCell(tf.keras.layers.layer):
  def __init__(self, input_dim,rnn_units, output_dim):
    # Initialize weights and biases for input-to-hidden connection
    # Initialize the Weights and biases for hidden-to-hidden connection
    # Initialize the Weights and Biases for hidden-to-output connection
    self.W_xh = self.add_weight([input_dim, rnn_units])
    self.W_hh = self.add_weight([rnn_units, rnn_uits])
    self.W_hy= self.add_weight([rnn_units, output_dim])

    # Initialize hidden state to zeros 
    self.h = tf.zeros([rnn_units,1])

  def Call(self, x):
    # update the hidden state by using the Non-linearity 
    self.h = tf.math,tanh( (self.W_xh * x) + ( self.W_hh * self.h ))

    # compute the output
    output = self.W_hy * self.h

    # return the current output and the current hidden state 
    return output, self.h

    
