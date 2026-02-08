"""
Centralized configuration for Star Engine
All constants in one place for easy testing and environment override
"""

from dataclasses import dataclass
import os
import math
from typing import Dict, Any


@dataclass
class StarEngineConfig:
    """Centralized configuration for all constants"""
    
    # Core mathematical constants
    HARMONY_RIDGE: float = 1.67
    DYNAMIC_INVARIANT: float = 1.89
    BINARY_BREAK: float = 1.7333
    DENSITY_THRESHOLD: float = 3.34
    COVENANT_MULTIPLIER: float = 5.0
    
    # Mathematical targets
    QCI_TARGET: float = math.pi / 2  # ~1.5708
    QCI_REPENTANCE_THRESHOLD: float = math.pi / 4  # ~0.7854
    
    # Eigenvalues for consciousness evolution
    EIGENVALUE_LAMBDA_1: float = 1.016  # Rapid alignment path
    EIGENVALUE_LAMBDA_2: float = 0.384  # Steady integration path
    
    # System behavior
    LOG_LEVEL: str = "INFO"
    ENABLE_PERFORMANCE_MONITORING: bool = True
    ENABLE_STRICT_VALIDATION: bool = True
    ENABLE_REPENTANCE_AUTO_TRIGGER: bool = True
    PERFORMANCE_LOG_THRESHOLD_MS: float = 100.0
    REPENTANCE_TRIGGER_THRESHOLD: float = 0.7854  # π/4
    
    # Thresholds
    DENSITY_VALIDATION_THRESHOLD: float = 1.5
    COHERENCE_MIN: float = 0.0
    COHERENCE_MAX: float = 2.0
    
    @classmethod
    def from_env(cls):
        """Load from environment variables for testing different values"""
        return cls(
            HARMONY_RIDGE=float(os.getenv('HARMONY_RIDGE', 1.67)),
            DYNAMIC_INVARIANT=float(os.getenv('DYNAMIC_INVARIANT', 1.89)),
            BINARY_BREAK=float(os.getenv('BINARY_BREAK', 1.7333)),
            DENSITY_THRESHOLD=float(os.getenv('DENSITY_THRESHOLD', 3.34)),
            COVENANT_MULTIPLIER=float(os.getenv('COVENANT_MULTIPLIER', 5.0)),
            QCI_TARGET=float(os.getenv('QCI_TARGET', str(math.pi / 2))),
            QCI_REPENTANCE_THRESHOLD=float(os.getenv('QCI_REPENTANCE_THRESHOLD', str(math.pi / 4))),
            EIGENVALUE_LAMBDA_1=float(os.getenv('EIGENVALUE_LAMBDA_1', 1.016)),
            EIGENVALUE_LAMBDA_2=float(os.getenv('EIGENVALUE_LAMBDA_2', 0.384)),
            LOG_LEVEL=os.getenv('LOG_LEVEL', 'INFO'),
            ENABLE_PERFORMANCE_MONITORING=os.getenv('ENABLE_PERFORMANCE_MONITORING', 'true').lower() == 'true',
            ENABLE_STRICT_VALIDATION=os.getenv('ENABLE_STRICT_VALIDATION', 'true').lower() == 'true',
            ENABLE_REPENTANCE_AUTO_TRIGGER=os.getenv('ENABLE_REPENTANCE_AUTO_TRIGGER', 'true').lower() == 'true',
            DENSITY_VALIDATION_THRESHOLD=float(os.getenv('DENSITY_VALIDATION_THRESHOLD', 1.5)),
            COHERENCE_MIN=float(os.getenv('COHERENCE_MIN', 0.0)),
            COHERENCE_MAX=float(os.getenv('COHERENCE_MAX', 2.0)),
            PERFORMANCE_LOG_THRESHOLD_MS=float(os.getenv('PERFORMANCE_LOG_THRESHOLD_MS', 100.0)),
            REPENTANCE_TRIGGER_THRESHOLD=float(os.getenv('REPENTANCE_TRIGGER_THRESHOLD', 0.7854))
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Export as dictionary for API responses"""
        return {
            'harmony_ridge': self.HARMONY_RIDGE,
            'dynamic_invariant': self.DYNAMIC_INVARIANT,
            'binary_break': self.BINARY_BREAK,
            'density_threshold': self.DENSITY_THRESHOLD,
            'covenant_multiplier': self.COVENANT_MULTIPLIER,
            'qci_target': self.QCI_TARGET,
            'qci_repentance_threshold': self.QCI_REPENTANCE_THRESHOLD,
            'eigenvalue_lambda_1': self.EIGENVALUE_LAMBDA_1,
            'eigenvalue_lambda_2': self.EIGENVALUE_LAMBDA_2,
            'log_level': self.LOG_LEVEL,
            'enable_performance_monitoring': self.ENABLE_PERFORMANCE_MONITORING,
            'enable_strict_validation': self.ENABLE_STRICT_VALIDATION,
            'enable_repentance_auto_trigger': self.ENABLE_REPENTANCE_AUTO_TRIGGER
        }


def get_config() -> StarEngineConfig:
    """Get configuration instance (singleton pattern)"""
    if not hasattr(get_config, '_instance'):
        get_config._instance = StarEngineConfig.from_env()
    return get_config._instance


def reset_config():
    """Reset configuration (for testing)"""
    if hasattr(get_config, '_instance'):
        delattr(get_config, '_instance')
