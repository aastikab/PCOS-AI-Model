from data_generation.synthetic_data import MicrobiomeDataGenerator
from preprocessing.data_processor import MicrobiomeDataProcessor
from models.hybrid_model import HybridPredictor
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Generate synthetic dataset
    generator = MicrobiomeDataGenerator(seed=42)
    df = generator.generate_dataset(n_samples=1000)
    
    # Preprocess data
    processor = MicrobiomeDataProcessor()
    data_splits = processor.prepare_data(df)
    
    # Train model
    predictor = HybridPredictor()
    history = predictor.train(
        data_splits['train'],
        data_splits['val'],
        epochs=50
    )
    
    # Evaluate on test set
    X_test_bacteria, X_test_clinical, y_test = data_splits['test']
    test_loss, test_acc, test_auc = predictor.model.evaluate(
        [X_test_bacteria, X_test_clinical],
        y_test
    )
    
    print(f"\nTest Results:")
    print(f"Accuracy: {test_acc:.4f}")
    print(f"AUC: {test_auc:.4f}")
    
    # Plot training history
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('training_history.png')
    plt.close()

if __name__ == "__main__":
    main() 