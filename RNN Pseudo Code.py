# let us define a RNN class 
import tensorflow as tf 
class MyRNNCell(tf.keras.layers.layer):
  def __init__(self, input_dim,rnn_units):
    # Initialize weights and biases for input-to-hidden connection
    # Initialize the Weights and biases for hidden-to-hidden connection
    # Initialize the Weights and Biases for hidden-to-output connection
    self.W_xh = self.add_weights()
    self.W_hh = self.add_weights()
    self.W_hy= self.add_weights()

    

    
