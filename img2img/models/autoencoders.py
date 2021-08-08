import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model


class AutoEncoder(Model):
    def __init__(self, filters_count_list=[32, 16],
                 input_shape=(1054, 1054, 3)):
        super(AutoEncoder, self).__init__()
        encoder_layers = [layers.Conv2D(size, (3, 3),
                                        activation='relu',
                                        padding='same',
                                        strides=2)
                          for size in filters_count_list]
        self.encoder = tf.keras.Sequential([layers.Input(shape=input_shape)] +
                                           encoder_layers)

        decoder_layers = [layers.Conv2DTranspose(
                size, kernel_size=3, strides=2,
                activation='relu', padding='same')
                for size in filters_count_list]
        decoder_layers.reverse()
        self.decoder = tf.keras.Sequential(decoder_layers + [
            layers.Conv2D(3, kernel_size=(3, 3),
                          activation='sigmoid', padding='valid')])
        self.build((None,) + input_shape)

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


if __name__ == '__main__':
    model = AutoEncoder()
    print(model.summary())
