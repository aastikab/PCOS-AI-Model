import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input, Dense, Dropout, concatenate, BatchNormalization
)

class HybridPredictor:
    def __init__(self):
        self.model = self._build_model()
        
    def _build_model(self):
        # Microbiome input branch
        microbiome_input = Input(shape=(4,), name='microbiome_input')
        x1 = Dense(32, activation='relu')(microbiome_input)
        x1 = BatchNormalization()(x1)
        x1 = Dropout(0.3)(x1)
        
        # Clinical features branch
        clinical_input = Input(shape=(3,), name='clinical_input')
        x2 = Dense(16, activation='relu')(clinical_input)
        x2 = BatchNormalization()(x2)
        x2 = Dropout(0.2)(x2)
        
        # Combine branches
        combined = concatenate([x1, x2])
        x = Dense(64, activation='relu')(combined)
        x = BatchNormalization()(x)
        x = Dropout(0.4)(x)
        x = Dense(32, activation='relu')(x)
        x = BatchNormalization()(x)
        
        # Output layer
        output = Dense(1, activation='sigmoid')(x)
        
        model = Model(
            inputs=[microbiome_input, clinical_input],
            outputs=output
        )
        
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy', tf.keras.metrics.AUC()]
        )
        
        return model
    
    def train(self, train_data, val_data, epochs=50, batch_size=32):
        """Train the model"""
        X_train_bacteria, X_train_clinical, y_train = train_data
        X_val_bacteria, X_val_clinical, y_val = val_data
        
        history = self.model.fit(
            [X_train_bacteria, X_train_clinical],
            y_train,
            validation_data=([X_val_bacteria, X_val_clinical], y_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[
                tf.keras.callbacks.EarlyStopping(
                    patience=10,
                    restore_best_weights=True
                )
            ]
        )
        
        return history
    
    def predict(self, X_bacteria, X_clinical):
        """Make predictions"""
        return self.model.predict([X_bacteria, X_clinical]) 