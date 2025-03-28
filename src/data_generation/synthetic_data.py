import numpy as np
import pandas as pd
from scipy.stats import norm, multivariate_normal

class MicrobiomeDataGenerator:
    def __init__(self, seed=42):
        self.seed = seed
        np.random.seed(seed)
        
        # Define baseline parameters
        self.bacteria_baseline = {
            'Bacteroidetes': {'mean': 30, 'std': 5},
            'Firmicutes': {'mean': 40, 'std': 7},
            'Proteobacteria': {'mean': 15, 'std': 3},
            'Actinobacteria': {'mean': 10, 'std': 2}
        }
        
        # PCOS effects on bacteria
        self.pcos_effects = {
            'Bacteroidetes': -5,
            'Firmicutes': 8,
            'Proteobacteria': 3,
            'Actinobacteria': -2
        }
        
        # Clinical parameters
        self.clinical_params = {
            'Age': {'mean': 28, 'std': 5},
            'BMI': {'mean': 27, 'std': 4},
            'Insulin_Resistance': {'mean': 2.5, 'std': 0.5}
        }

    def generate_bacteria_profile(self, is_pcos):
        """Generate bacterial composition for one sample"""
        profile = {}
        total = 0
        
        for bacteria, params in self.bacteria_baseline.items():
            mean = params['mean']
            if is_pcos:
                mean += self.pcos_effects[bacteria]
            
            value = max(0, np.random.normal(mean, params['std']))
            profile[bacteria] = value
            total += value
        
        # Normalize to 100%
        for bacteria in profile:
            profile[bacteria] = (profile[bacteria] / total) * 100
            
        return profile

    def generate_clinical_data(self, is_pcos):
        """Generate clinical parameters for one sample"""
        data = {}
        
        for param, base in self.clinical_params.items():
            mean = base['mean']
            if is_pcos and param == 'Insulin_Resistance':
                mean += 0.8
            
            data[param] = np.random.normal(mean, base['std'])
            
        return data

    def generate_dataset(self, n_samples=1000):
        """Generate complete dataset with both PCOS and control samples"""
        data = []
        
        for _ in range(n_samples):
            is_pcos = np.random.choice([0, 1], p=[0.5, 0.5])
            
            sample = {
                'PCOS': is_pcos,
                **self.generate_bacteria_profile(is_pcos),
                **self.generate_clinical_data(is_pcos)
            }
            
            # Calculate prediabetes risk (simplified model)
            risk_score = (
                0.3 * sample['Insulin_Resistance'] +
                0.2 * (sample['BMI'] - 25) / 10 +
                0.1 * (sample['Firmicutes'] - sample['Bacteroidetes']) / 10
            )
            
            sample['Prediabetes_Risk'] = 1 / (1 + np.exp(-risk_score))
            
            data.append(sample)
        
        return pd.DataFrame(data)

    def save_dataset(self, filepath, n_samples=1000):
        """Generate and save dataset to CSV"""
        df = self.generate_dataset(n_samples)
        df.to_csv(filepath, index=False)
        return df 