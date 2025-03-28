import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class MicrobiomeDataProcessor:
    def __init__(self):
        self.bacteria_scaler = StandardScaler()
        self.clinical_scaler = StandardScaler()
        
    def split_features(self, df):
        """Split dataframe into bacteria and clinical features"""
        bacteria_cols = ['Bacteroidetes', 'Firmicutes', 
                        'Proteobacteria', 'Actinobacteria']
        clinical_cols = ['Age', 'BMI', 'Insulin_Resistance']
        
        X_bacteria = df[bacteria_cols]
        X_clinical = df[clinical_cols]
        y = df['Prediabetes_Risk']
        
        return X_bacteria, X_clinical, y
    
    def fit_transform(self, df):
        """Fit scalers and transform data"""
        X_bacteria, X_clinical, y = self.split_features(df)
        
        X_bacteria_scaled = self.bacteria_scaler.fit_transform(X_bacteria)
        X_clinical_scaled = self.clinical_scaler.fit_transform(X_clinical)
        
        return X_bacteria_scaled, X_clinical_scaled, y
    
    def transform(self, df):
        """Transform data using fitted scalers"""
        X_bacteria, X_clinical, y = self.split_features(df)
        
        X_bacteria_scaled = self.bacteria_scaler.transform(X_bacteria)
        X_clinical_scaled = self.clinical_scaler.transform(X_clinical)
        
        return X_bacteria_scaled, X_clinical_scaled, y
    
    def prepare_data(self, df, test_size=0.2, val_size=0.2):
        """Prepare train/val/test splits"""
        # First split into train+val and test
        train_val_df, test_df = train_test_split(
            df, test_size=test_size, random_state=42
        )
        
        # Then split train+val into train and val
        train_df, val_df = train_test_split(
            train_val_df, test_size=val_size, random_state=42
        )
        
        # Fit scalers on training data only
        X_train_bacteria, X_train_clinical, y_train = self.fit_transform(train_df)
        
        # Transform validation and test data
        X_val_bacteria, X_val_clinical, y_val = self.transform(val_df)
        X_test_bacteria, X_test_clinical, y_test = self.transform(test_df)
        
        return {
            'train': (X_train_bacteria, X_train_clinical, y_train),
            'val': (X_val_bacteria, X_val_clinical, y_val),
            'test': (X_test_bacteria, X_test_clinical, y_test)
        } 