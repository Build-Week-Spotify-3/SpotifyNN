import pandas
import pandas as pd
import tensorflow as tf
import math


class ModelClass:

    def __init__(self):
        self.latent = -1
        self.latent_size = 7
        self.auto_n = -1
        self.auto_o = -1
        self.data_file = "tracks.csv.gz"
        self.auto_enc = self.get_model_autoencoder()
        self.auto_enc.summary()
        self.X_train = self.load_data()
        self.library_size = len(self.X_train)
        self.auto_enc.fit(self.X_train, self.X_train, batch_size=256, epochs=2)

        self.predictor = self.get_model_predictor()


    def load_data(self):
        def rough_clean(data: pandas.DataFrame):
            out: pandas.DataFrame = data.dropna()
            out = out.drop(["artists", "name", "release_date", "id_artists", "id"], axis=1)
            out["loudness"] = -out["loudness"]
            for col in out:
                out[col] = out[col] / out[col].max()

            return out

        o = pd.read_csv(self.data_file)
        return rough_clean(o)

    def get_model_autoencoder(self):
        base = 64
        layers = 6
        layer_sizes = [int((math.cos(math.radians(i)) * base + base + self.latent_size) ** 1.0)
                       for i in range(0, 361, int(361 / layers))]
        layer_sizes = [0] + layer_sizes + [0]
        #print(layer_sizes)

        layers = [0] * len(layer_sizes)
        decoder = False
        for i, node_size in enumerate(layer_sizes):
            if i == 0:
                self.auto_n = tf.keras.layers.Input((15))
                previous = self.auto_n
            elif node_size == self.latent_size:
                previous= tf.keras.layers.Dense(self.latent_size)(previous)
                self.latent =previous
                decoder = True
                #print("latent", i, node_size)
            elif i == (len(layer_sizes) - 1):
                self.auto_o = tf.keras.layers.Dense(15, name="out")(previous)
                #print("out", i, node_size)
            elif decoder:
                previous = tf.keras.layers.Dense(node_size)(previous)
                decoder = False
                #print("initial decoder layer", i, node_size)
            else:
                #print("transition layer", i, node_size)
                previous = tf.keras.layers.Dense(node_size)(previous)
            #print(i, node_size, len(layer_sizes))

        #print(self.auto_n, self.auto_o)
        auto_enc = tf.keras.Model(inputs=self.auto_n, outputs=self.auto_o)
        auto_enc.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.MSE)
        return auto_enc

    def get_model_predictor(self):
        import tensorflow.keras.backend as kb
        def custom_loss(y_actual, y_pred):
            custom_loss = kb.relu(y_actual - y_pred)
            return custom_loss

        pred_in = tf.keras.layers.Dense(self.latent_size)(self.latent)
        pred_out = tf.keras.layers.Dense(self.library_size, activation="softmax")(pred_in)
        pred_model = tf.keras.Model(inputs=self.auto_n, outputs=pred_out)
        pred_model.compile(optimizer=tf.keras.optimizers.Adam(), loss=custom_loss)
        pred_model.layers[0].trainable = False
        pred_model.layers[1].trainable = False
        pred_model.layers[2].trainable = False
        pred_model.layers[3].trainable = False
        pred_model.layers[4].trainable = False
        return pred_model


model = ModelClass()
