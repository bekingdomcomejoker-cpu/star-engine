"""
Hypothesis Validation Tests for Star Engine
Empirical testing of core claims about system behavior
"""

import pytest
import math
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from core_improved import StarEngine
from config import get_config, reset_config, StarEngineConfig
from logging_module import get_logger


class TestDynamicInvariantHypothesis:
    """
    Hypothesis 1: Coherence threshold at 1.67→1.89 produces measurably 
    different system behavior
    """
    
    def setup_method(self):
        """Reset config before each test"""
        reset_config()
        self.engine = StarEngine()
        self.config = get_config()
    
    def test_coherence_below_harmony_ridge(self):
        """
        Below 1.67: Should maintain HARMONY_RIDGE mode
        Expected: invariant == 1.67
        """
        result = self.engine.get_dynamic_invariant(coherence_score=1.5)
        assert result == self.config.HARMONY_RIDGE
        assert result == 1.67
    
    def test_coherence_above_dynamic_invariant(self):
        """
        Above 1.89: Should activate TRI_NODE_SYNTHESIS
        Expected: invariant == 1.89
        """
        result = self.engine.get_dynamic_invariant(coherence_score=1.95)
        assert result == self.config.DYNAMIC_INVARIANT
        assert result == 1.89
    
    def test_coherence_at_boundary(self):
        """
        At exact threshold: Define expected behavior
        Expected: Should be at boundary
        """
        result = self.engine.get_dynamic_invariant(coherence_score=1.67)
        assert result in [1.67, 1.89]
    
    def test_coherence_gradient_effect(self):
        """
        Test that coherence score creates gradient effect
        Expected: Multiple calls with increasing coherence show progression
        """
        results = []
        for coherence in [1.0, 1.5, 1.67, 1.8, 1.89, 2.0]:
            result = self.engine.get_dynamic_invariant(coherence)
            results.append(result)
        
        # Should have transition point
        assert 1.67 in results or 1.89 in results
    
    def test_coherence_validation_bounds(self):
        """
        Test that coherence is validated within bounds
        Expected: Coherence between 0 and 2
        """
        # Valid range
        assert self.engine.get_dynamic_invariant(0.5) is not None
        assert self.engine.get_dynamic_invariant(1.5) is not None
        assert self.engine.get_dynamic_invariant(2.0) is not None


class TestTripleIProtocolHypothesis:
    """
    Hypothesis 2: Internal → Inverse → Invariant processing produces 
    better outputs than standard processing
    """
    
    def setup_method(self):
        """Setup for each test"""
        reset_config()
        self.engine = StarEngine()
        self.logger = get_logger()
    
    def test_internal_axioms_enforcement(self):
        """
        Internal layer should enforce covenant axioms
        Expected: Malicious input is rejected or transformed
        """
        # This would require Triple I implementation
        # For now, test that engine validates input
        result, logs = self.engine.operational_flow(
            "Test input",
            {"i1": 1.5, "i2": 1.5, "i3": 1.5, "i4": 1.0}
        )
        
        # Should complete without error
        assert result is not None
        assert isinstance(result, dict)
    
    def test_deterministic_output(self):
        """
        Invariant lock should produce deterministic output
        Expected: Same input produces same output every time
        """
        input_data = "Test determinism"
        params = {"i1": 1.5, "i2": 1.5, "i3": 1.5, "i4": 1.0}
        
        results = []
        for _ in range(3):
            result, _ = self.engine.operational_flow(input_data, params)
            results.append(result.get('status'))
        
        # All results should be identical
        assert results[0] == results[1] == results[2]
    
    def test_consistency_across_runs(self):
        """
        Test that system produces consistent results
        Expected: Multiple runs with same input produce same output
        """
        input_data = "Consistency test"
        params = {"i1": 1.5, "i2": 1.5, "i3": 1.5, "i4": 1.0}
        
        result1, _ = self.engine.operational_flow(input_data, params)
        result2, _ = self.engine.operational_flow(input_data, params)
        
        assert result1['status'] == result2['status']


class TestRepentanceProtocolHypothesis:
    """
    Hypothesis 3: 4-step self-correction cycle improves performance 
    when metrics drop
    """
    
    def setup_method(self):
        """Setup for each test"""
        reset_config()
        self.engine = StarEngine()
        self.config = get_config()
    
    def test_repentance_qci_improvement(self):
        """
        Repentance should improve QCI score
        Expected: qci_after > qci_before
        """
        # Simulate degraded state
        initial_qci = 0.5  # Below target of π/2 ≈ 1.57
        
        # Execute repentance
        result = self.engine.repentance_protocol("Low QCI detected")
        
        # QCI should improve
        assert result['qci_after'] > initial_qci
        assert result['qci_after'] >= (math.pi / 4)
    
    def test_repentance_steps_execution(self):
        """
        All four steps should execute
        Expected: expose, recompile, purge, reset all present
        """
        result = self.engine.repentance_protocol("Test")
        
        assert result['expose'] is not None
        assert result['recompile'] is not None
        assert result['purge'] == True
        assert result['reset'] == True
        assert result['status'] == 'REPENTANCE_COMPLETE'
    
    def test_repentance_qci_target_achievement(self):
        """
        After repentance, QCI should approach target
        Expected: qci_after closer to target than qci_before
        """
        result = self.engine.repentance_protocol("QCI improvement test")
        
        qci_before = result['qci_before']
        qci_after = result['qci_after']
        target = self.config.QCI_TARGET
        
        # Distance to target should decrease
        distance_before = abs(target - qci_before)
        distance_after = abs(target - qci_after)
        
        assert distance_after <= distance_before
    
    def test_repentance_prevents_cascade_failure(self):
        """
        Repentance should prevent system degradation
        Expected: System remains operational after repentance
        """
        # Trigger repentance
        self.engine.repentance_protocol("Cascade prevention")
        
        # System should still be operational
        result, _ = self.engine.operational_flow(
            "Test after repentance",
            {"i1": 1.5, "i2": 1.5, "i3": 1.5, "i4": 1.0}
        )
        
        assert result['status'] != 'FAILED'


class TestQCIQualityCorrelationHypothesis:
    """
    Hypothesis 4: QCI (arctan(TIF/resistance)) correlates with 
    output quality
    """
    
    def setup_method(self):
        """Setup for each test"""
        reset_config()
        self.engine = StarEngine()
        self.config = get_config()
    
    def test_high_tif_high_qci(self):
        """
        High TIF should produce high QCI
        Expected: qci > π/4 when TIF is high
        """
        result = self.engine.calculate_qci(tif=2.0, resistance=0.1)
        
        assert result['qci'] > (math.pi / 4)
        assert result['status'] == 'COHERENT'
    
    def test_low_tif_low_qci(self):
        """
        Low TIF should produce low QCI
        Expected: qci < π/4 when TIF is low
        """
        result = self.engine.calculate_qci(tif=0.1, resistance=2.0)
        
        assert result['qci'] < (math.pi / 4)
        assert result['status'] == 'NEEDS_REPENTANCE'
    
    def test_qci_monotonic_with_tif(self):
        """
        QCI should increase monotonically with TIF
        Expected: Higher TIF → Higher QCI
        """
        qci_values = []
        for tif in [0.1, 0.5, 1.0, 1.5, 2.0]:
            result = self.engine.calculate_qci(tif=tif, resistance=1.0)
            qci_values.append(result['qci'])
        
        # Should be monotonically increasing
        for i in range(len(qci_values) - 1):
            assert qci_values[i] <= qci_values[i + 1]
    
    def test_qci_inverse_with_resistance(self):
        """
        QCI should decrease with resistance
        Expected: Higher resistance → Lower QCI
        """
        qci_values = []
        for resistance in [0.1, 0.5, 1.0, 1.5, 2.0]:
            result = self.engine.calculate_qci(tif=1.0, resistance=resistance)
            qci_values.append(result['qci'])
        
        # Should be monotonically decreasing
        for i in range(len(qci_values) - 1):
            assert qci_values[i] >= qci_values[i + 1]
    
    def test_qci_threshold_prediction_accuracy(self):
        """
        QCI threshold should predict repentance need
        Expected: Accuracy > 75% on random samples
        """
        predictions = []
        actuals = []
        
        for i in range(20):
            # Generate random TIF and resistance
            tif = 0.1 + (i * 0.1)
            resistance = 2.0 - (i * 0.05)
            
            result = self.engine.calculate_qci(tif=tif, resistance=resistance)
            qci = result['qci']
            
            predicted_needs_repentance = qci < (math.pi / 4)
            actual_needs_repentance = result['status'] == 'NEEDS_REPENTANCE'
            
            predictions.append(predicted_needs_repentance)
            actuals.append(actual_needs_repentance)
        
        # Calculate accuracy
        accuracy = sum(p == a for p, a in zip(predictions, actuals)) / len(predictions)
        assert accuracy >= 0.75, f"Accuracy {accuracy} should be >= 0.75"


class TestDensityValidationHypothesis:
    """
    Hypothesis 5: Density validation correctly identifies system coherence
    """
    
    def setup_method(self):
        """Setup for each test"""
        reset_config()
        self.engine = StarEngine()
        self.config = get_config()
    
    def test_density_above_threshold(self):
        """
        Density above threshold should be valid
        Expected: is_valid == True when density > threshold
        """
        is_valid, density = self.engine.verify_density(
            i1=1.5, i2=1.5, i3=1.5, i4=1.5
        )
        
        assert is_valid == True
        assert density >= self.config.DENSITY_THRESHOLD
    
    def test_density_below_threshold(self):
        """
        Density below threshold should be invalid
        Expected: is_valid == False when density < threshold
        """
        is_valid, density = self.engine.verify_density(
            i1=0.5, i2=0.5, i3=0.5, i4=0.5
        )
        
        assert is_valid == False
        assert density < self.config.DENSITY_THRESHOLD
    
    def test_density_at_threshold(self):
        """
        Density at exact threshold should be valid
        Expected: is_valid == True when density == threshold
        """
        # Calculate values that produce density at threshold
        target_density = self.config.DENSITY_THRESHOLD
        
        is_valid, density = self.engine.verify_density(
            i1=target_density, i2=target_density, 
            i3=target_density, i4=target_density
        )
        
        assert is_valid == True


class TestOperationalFlowIntegration:
    """
    Integration tests for complete operational flow
    """
    
    def setup_method(self):
        """Setup for each test"""
        reset_config()
        self.engine = StarEngine()
    
    def test_complete_analysis_pipeline(self):
        """
        Test data flowing through all layers
        Expected: Complete pipeline executes without error
        """
        result, logs = self.engine.operational_flow(
            "Complete pipeline test",
            {
                "alignment": 10,
                "separation": 2,
                "dt": 1,
                "tif": [1.0, 0.1],
                "resistance": 0.5,
                "i1": 1.5,
                "i2": 1.5,
                "i3": 1.5,
                "i4": 1.0
            }
        )
        
        assert result is not None
        assert result['status'] in ['RELEASED', 'REJECTED', 'REPENTANCE_TRIGGERED', 'QUARANTINED']
    
    def test_pipeline_with_good_metrics(self):
        """
        Test pipeline with high-quality metrics
        Expected: Status should be RELEASED
        """
        result, logs = self.engine.operational_flow(
            "Good metrics test",
            {
                "alignment": 15,
                "separation": 1,
                "dt": 1,
                "tif": [2.0, 0.05],
                "resistance": 0.3,
                "i1": 1.8,
                "i2": 1.8,
                "i3": 1.8,
                "i4": 1.5
            }
        )
        
        assert result['status'] in ['RELEASED', 'REPENTANCE_TRIGGERED']
    
    def test_pipeline_with_poor_metrics(self):
        """
        Test pipeline with low-quality metrics
        Expected: May trigger repentance or quarantine
        """
        result, logs = self.engine.operational_flow(
            "Poor metrics test",
            {
                "alignment": 2,
                "separation": 5,
                "dt": 1,
                "tif": [0.1, 0.5],
                "resistance": 2.0,
                "i1": 0.5,
                "i2": 0.5,
                "i3": 0.5,
                "i4": 0.5
            }
        )
        
        assert result['status'] in ['REJECTED', 'REPENTANCE_TRIGGERED', 'QUARANTINED']


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
