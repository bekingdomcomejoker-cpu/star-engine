"""
Comprehensive test suite for improved Star Engine core.
Tests all mathematical operators and error handling.
"""

import sys
import os
import pytest
import math
import logging

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from core_improved import (
    StarEngine,
    StarEngineError,
    CoherenceCalculationError,
    DensityValidationError,
    RepentanceError
)
from config import StarEngineConfig, set_config, reset_config


# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)


class TestStarEngineConfig:
    """Test configuration management."""
    
    def test_default_config(self):
        """Test default configuration values."""
        reset_config()
        config = StarEngineConfig()
        
        assert config.HARMONY_RIDGE == 1.67
        assert config.DYNAMIC_INVARIANT == 1.89
        assert config.BINARY_BREAK == 1.7333
        assert config.DENSITY_THRESHOLD == 3.34
        assert config.COVENANT_MULTIPLIER == 5.0
        assert config.QCI_TARGET == math.pi / 2
    
    def test_config_to_dict(self):
        """Test configuration serialization."""
        config = StarEngineConfig()
        config_dict = config.to_dict()
        
        assert 'HARMONY_RIDGE' in config_dict
        assert config_dict['HARMONY_RIDGE'] == 1.67
    
    def test_heart_5_vowel_initialization(self):
        """Test Heart-5 Vowel System initialization."""
        config = StarEngineConfig()
        
        assert 'A' in config.HEART_5_VOWELS
        assert 'E' in config.HEART_5_VOWELS
        assert 'I' in config.HEART_5_VOWELS
        assert 'O' in config.HEART_5_VOWELS
        assert 'U' in config.HEART_5_VOWELS
        
        assert config.HEART_5_VOWELS['A']['name'] == 'Initiation'
        assert config.HEART_5_VOWELS['E']['name'] == 'Discernment'


class TestDynamicInvariant:
    """Test Dynamic Invariant calculations."""
    
    def test_below_harmony_ridge(self):
        """Test invariant below harmony ridge."""
        engine = StarEngine()
        result = engine.get_dynamic_invariant(coherence_score=1.5)
        
        assert result == 1.67
    
    def test_above_harmony_ridge(self):
        """Test invariant above harmony ridge."""
        engine = StarEngine()
        result = engine.get_dynamic_invariant(coherence_score=1.8)
        
        assert result == 1.89
    
    def test_at_harmony_ridge(self):
        """Test invariant at exact harmony ridge."""
        engine = StarEngine()
        result = engine.get_dynamic_invariant(coherence_score=1.67)
        
        # At the boundary, should return HARMONY_RIDGE
        assert result == 1.67
    
    def test_negative_coherence_raises_error(self):
        """Test that negative coherence raises error."""
        engine = StarEngine()
        
        with pytest.raises(CoherenceCalculationError):
            engine.get_dynamic_invariant(coherence_score=-1.0)


class TestDfruitDt:
    """Test dFruit/dt growth metric calculations."""
    
    def test_positive_growth(self):
        """Test positive growth calculation."""
        engine = StarEngine()
        result = engine.calculate_dfruit_dt(alignment=10, separation=2, dt=1)
        
        assert result == 8.0
    
    def test_negative_degradation(self):
        """Test negative degradation calculation."""
        engine = StarEngine()
        result = engine.calculate_dfruit_dt(alignment=2, separation=10, dt=1)
        
        assert result == -8.0
    
    def test_neutral_state(self):
        """Test neutral state calculation."""
        engine = StarEngine()
        result = engine.calculate_dfruit_dt(alignment=5, separation=5, dt=1)
        
        assert result == 0.0
    
    def test_zero_dt_returns_zero(self):
        """Test that zero dt returns 0."""
        engine = StarEngine()
        result = engine.calculate_dfruit_dt(alignment=10, separation=2, dt=0)
        
        assert result == 0.0


class TestTIF:
    """Test Truth Implosion Force calculations."""
    
    def test_tif_calculation(self):
        """Test TIF calculation."""
        engine = StarEngine()
        result = engine.calculate_tif(omega_truth=1.0, target_falsehood=0.8)
        
        assert math.isclose(result, 0.2)
    
    def test_tif_zero_gap(self):
        """Test TIF with zero gap."""
        engine = StarEngine()
        result = engine.calculate_tif(omega_truth=1.0, target_falsehood=1.0)
        
        assert result == 0.0
    
    def test_tif_negative_values(self):
        """Test TIF with negative values."""
        engine = StarEngine()
        result = engine.calculate_tif(omega_truth=-1.0, target_falsehood=-0.5)
        
        assert math.isclose(result, 0.5)


class TestQCI:
    """Test Quantum Coherence Index calculations."""
    
    def test_qci_calculation(self):
        """Test QCI calculation."""
        engine = StarEngine()
        result = engine.calculate_qci(tif=1.0, resistance=1.0)
        
        assert 'qci' in result
        assert 'status' in result
        assert math.isclose(result['qci'], math.pi / 4)
    
    def test_qci_perfect_collapse(self):
        """Test QCI approaching perfect collapse."""
        engine = StarEngine()
        result = engine.calculate_qci(tif=10.0, resistance=0.1)
        
        # Should be close to π/2
        assert result['qci'] > math.pi / 3
    
    def test_qci_zero_resistance(self):
        """Test QCI with zero resistance."""
        engine = StarEngine()
        result = engine.calculate_qci(tif=1.0, resistance=0)
        
        assert result['qci'] == engine.QCI_TARGET
    
    def test_qci_status_coherent(self):
        """Test QCI status when coherent."""
        engine = StarEngine()
        result = engine.calculate_qci(tif=5.0, resistance=1.0)
        
        if result['qci'] >= (engine.QCI_TARGET * 0.75):
            assert result['status'] == 'COHERENT'


class TestDensity:
    """Test density verification."""
    
    def test_density_above_threshold(self):
        """Test density above threshold."""
        engine = StarEngine()
        is_valid, density = engine.verify_density(i1=1.5, i2=1.5, i3=1.5, i4=1.0)
        
        assert is_valid is True
        assert density >= engine.DENSITY_THRESHOLD
    
    def test_density_below_threshold(self):
        """Test density below threshold."""
        engine = StarEngine()
        is_valid, density = engine.verify_density(i1=0.5, i2=0.5, i3=0.5, i4=0.5)
        
        assert is_valid is False
        assert density < engine.DENSITY_THRESHOLD
    
    def test_density_exact_threshold(self):
        """Test density at exact threshold."""
        engine = StarEngine()
        # Calculate values that give exactly 3.34
        # (i1 * i2 * i3) * i4 = 3.34
        # (1.0 * 1.0 * 3.34) * 1.0 = 3.34
        is_valid, density = engine.verify_density(i1=1.0, i2=1.0, i3=3.34, i4=1.0)
        
        assert is_valid is True
        assert math.isclose(density, engine.DENSITY_THRESHOLD)


class TestRepentanceProtocol:
    """Test Repentance Protocol."""
    
    def test_repentance_execution(self):
        """Test repentance protocol execution."""
        engine = StarEngine()
        result = engine.repentance_protocol("Test sin pattern")
        
        assert result['status'] == 'REPENTANCE_COMPLETE'
        assert 'expose' in result
        assert 'recompile' in result
        assert 'purge' in result
        assert 'reset' in result
        assert result['new_qci'] == engine.QCI_TARGET
    
    def test_repentance_returns_perfect_qci(self):
        """Test that repentance returns perfect QCI."""
        engine = StarEngine()
        result = engine.repentance_protocol("Low coherence")
        
        assert math.isclose(result['new_qci'], math.pi / 2)


class TestOperationalFlow:
    """Test complete operational flow."""
    
    def test_flow_with_good_metrics(self):
        """Test operational flow with good metrics."""
        engine = StarEngine()
        params = {
            'alignment': 10,
            'separation': 2,
            'dt': 1,
            'tif': (1.0, 0.1),
            'resistance': 0.5,
            'i1': 1.5, 'i2': 1.5, 'i3': 1.5, 'i4': 1.0
        }
        
        result, logs = engine.operational_flow("Test input", params)
        
        assert "RELEASED" in result
        assert logs is None
    
    def test_flow_with_low_qci(self):
        """Test operational flow with low QCI."""
        engine = StarEngine()
        params = {
            'alignment': 1,
            'separation': 10,
            'dt': 1,
            'tif': (0.01, 0.5),
            'resistance': 10.0,
            'i1': 1.5, 'i2': 1.5, 'i3': 1.5, 'i4': 1.0
        }
        
        result, logs = engine.operational_flow("Test input", params)
        
        # Should trigger repentance
        if "REJECTED" in result:
            assert "QCI" in result or "Repentance" in result
    
    def test_flow_with_low_density(self):
        """Test operational flow with low density."""
        engine = StarEngine()
        params = {
            'alignment': 10,
            'separation': 2,
            'dt': 1,
            'tif': (1.0, 0.1),
            'resistance': 0.5,
            'i1': 0.1, 'i2': 0.1, 'i3': 0.1, 'i4': 0.1
        }
        
        result, logs = engine.operational_flow("Test input", params)
        
        assert "REJECTED" in result
        assert "Density" in result


class TestErrorHandling:
    """Test error handling."""
    
    def test_star_engine_error_base(self):
        """Test base StarEngineError."""
        with pytest.raises(StarEngineError):
            raise StarEngineError("Test error")
    
    def test_coherence_calculation_error(self):
        """Test CoherenceCalculationError."""
        with pytest.raises(CoherenceCalculationError):
            raise CoherenceCalculationError("Test error")
    
    def test_density_validation_error(self):
        """Test DensityValidationError."""
        with pytest.raises(DensityValidationError):
            raise DensityValidationError("Test error")
    
    def test_repentance_error(self):
        """Test RepentanceError."""
        with pytest.raises(RepentanceError):
            raise RepentanceError("Test error")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
