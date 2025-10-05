"""
Unit tests for data preprocessing module.

Run with: pytest tests/test_data_preprocessing.py -v
"""

import pytest
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, 'src')

from data_preprocessing import DataPreprocessor


class TestDataPreprocessor:
    """Test suite for DataPreprocessor class."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample dataset for testing."""
        data = {
            'Learner_ID': [1, 2, 3, 4, 5],
            'Age': [25, 30, None, 35, 28],
            'Gender': ['Male', 'Female', 'Male', None, 'Female'],
            'Learning_Sessions_Completed': [50, 75, 30, 90, 45],
            'Total_Time_Spent_Minutes': [120.5, 200.0, 80.0, None, 150.0],
            'Course_Completion_Percentage': [60.0, 85.0, 40.0, 95.0, 55.0],
            'Pre_Test_Score': [60, 70, 55, 80, 65],
            'Post_Test_Score': [75, 88, 60, 92, 78],
            'Dropout': [False, False, True, False, False],
            'Learning_Pace': ['moderate', 'fast', 'slow', 'fast', 'moderate'],
            'Socioeconomic_Status': ['middle', 'high', 'low', 'high', 'middle']
        }
        return pd.DataFrame(data)
    
    @pytest.fixture
    def preprocessor(self, sample_data, tmp_path):
        """Create preprocessor instance with sample data."""
        # Save sample data to temporary CSV
        csv_path = tmp_path / "test_data.csv"
        sample_data.to_csv(csv_path, index=False)
        return DataPreprocessor(str(csv_path))
    
    def test_initialization(self, preprocessor):
        """Test if DataPreprocessor initializes correctly."""
        assert preprocessor is not None
        assert hasattr(preprocessor, 'df')
        assert isinstance(preprocessor.df, pd.DataFrame)
    
    def test_data_loading(self, preprocessor):
        """Test if data loads correctly."""
        assert len(preprocessor.df) > 0
        assert 'Learner_ID' in preprocessor.df.columns
    
    def test_missing_value_handling(self, preprocessor):
        """Test missing value imputation."""
        # Run preprocessing
        result = preprocessor.preprocess_pipeline()
        df_processed = result['df_original']
        
        # Check no missing values in numeric columns used for clustering
        numeric_cols = df_processed.select_dtypes(include=[np.number]).columns
        assert df_processed[numeric_cols].isnull().sum().sum() == 0
    
    def test_feature_encoding(self, preprocessor):
        """Test categorical feature encoding."""
        result = preprocessor.preprocess_pipeline()
        X_scaled = result['X_scaled']
        
        # Check if data is scaled (should be ndarray)
        assert isinstance(X_scaled, np.ndarray)
        
        # Check if features have reasonable scale (mean ~ 0, std ~ 1)
        assert abs(X_scaled.mean()) < 0.5
        assert abs(X_scaled.std() - 1.0) < 0.5
    
    def test_feature_scaling(self, preprocessor):
        """Test StandardScaler transformation."""
        result = preprocessor.preprocess_pipeline()
        X_scaled = result['X_scaled']
        
        # Scaled data should have similar dimensions to original features
        assert X_scaled.shape[0] == len(preprocessor.df)
        assert X_scaled.shape[1] > 0
    
    def test_pipeline_output_structure(self, preprocessor):
        """Test if pipeline returns expected output structure."""
        result = preprocessor.preprocess_pipeline()
        
        # Check all expected keys are present
        assert 'df_original' in result
        assert 'X_scaled' in result
        assert 'feature_cols' in result
        
        # Check types
        assert isinstance(result['df_original'], pd.DataFrame)
        assert isinstance(result['X_scaled'], np.ndarray)
        assert isinstance(result['feature_cols'], list)
    
    def test_knowledge_gain_calculation(self, preprocessor):
        """Test if knowledge gain is calculated correctly."""
        result = preprocessor.preprocess_pipeline()
        df = result['df_original']
        
        if 'Knowledge_Gain' in df.columns:
            # Knowledge gain should be post_test - pre_test
            expected_gain = df['Post_Test_Score'] - df['Pre_Test_Score']
            assert (df['Knowledge_Gain'] == expected_gain).all()
    
    def test_ordinal_encoding(self, sample_data, tmp_path):
        """Test ordinal encoding for ordered categorical variables."""
        csv_path = tmp_path / "test_ordinal.csv"
        sample_data.to_csv(csv_path, index=False)
        
        preprocessor = DataPreprocessor(str(csv_path))
        result = preprocessor.preprocess_pipeline()
        df = result['df_original']
        
        # Check if Learning_Pace is encoded as ordinal
        if 'Learning_Pace' in df.columns:
            pace_values = df['Learning_Pace'].unique()
            # Should be encoded as 0, 1, 2 or similar
            assert all(isinstance(v, (int, np.integer)) for v in pace_values)


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_dataframe(self, tmp_path):
        """Test handling of empty dataframe."""
        empty_df = pd.DataFrame()
        csv_path = tmp_path / "empty.csv"
        empty_df.to_csv(csv_path, index=False)
        
        with pytest.raises(Exception):
            preprocessor = DataPreprocessor(str(csv_path))
            preprocessor.preprocess_pipeline()
    
    def test_missing_required_columns(self, tmp_path):
        """Test handling of missing required columns."""
        incomplete_df = pd.DataFrame({'A': [1, 2, 3]})
        csv_path = tmp_path / "incomplete.csv"
        incomplete_df.to_csv(csv_path, index=False)
        
        with pytest.raises(Exception):
            preprocessor = DataPreprocessor(str(csv_path))
            preprocessor.preprocess_pipeline()
    
    def test_all_missing_values_column(self, tmp_path):
        """Test handling of column with all missing values."""
        data = pd.DataFrame({
            'Learner_ID': [1, 2, 3],
            'Age': [None, None, None],
            'Learning_Sessions_Completed': [10, 20, 30]
        })
        csv_path = tmp_path / "all_missing.csv"
        data.to_csv(csv_path, index=False)
        
        # Should handle gracefully (impute or drop column)
        preprocessor = DataPreprocessor(str(csv_path))
        result = preprocessor.preprocess_pipeline()
        assert result is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
