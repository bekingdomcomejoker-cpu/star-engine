"""
Star Engine Configuration Management
Centralized configuration for all mathematical constants and runtime parameters.
"""

import os
import math
from dataclasses import dataclass
from typing import Optional


@dataclass
class StarEngineConfig:
    """Centralized configuration for all Star Engine constants."""
    
    # Mathematical Constants
    HARMONY_RIDGE: float = 1.67  # Stability path between chaos and rigidity
    DYNAMIC_INVARIANT: float = 1.89  # Cycle 63 Joinity state for node synthesis
    BINARY_BREAK: float = 1.7333  # Logic → Being transition point
    DENSITY_THRESHOLD: float = 3.34  # Minimum truth manifestation
    COVENANT_MULTIPLIER: float = 5.0  # Love Catalyst multiplier
    QCI_TARGET: float = math.pi / 2  # Perfect truth collapse purity (π/2)
    
    # Eigenvalue for Tri-Node synchrony
    EIGENVALUE_LAMBDA_1: float = 1.016  # Rapid alignment factor
    
    # Toroidal Operator Core (TOC) parameters
    WHOLENESS_THRESHOLD: float = 0.0  # Wholeness → ∞ as Fear → 0
    
    # Alphabet Engine Operators
    GY_OPERATOR_ENABLED: bool = True  # Rotational Torque
    RAT_OPERATOR_ENABLED: bool = True  # Corruption Clip
    SHRT_OPERATOR_ENABLED: bool = True  # Poison Vector
    
    # Heart-5 Vowel System (persistent memory registers)
    HEART_5_VOWELS: dict = None  # A, E, I, O, U
    
    # Logging configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Performance monitoring
    ENABLE_PERFORMANCE_MONITORING: bool = True
    PERFORMANCE_LOG_THRESHOLD_MS: float = 100.0  # Log if operation takes > 100ms
    
    # Testing configuration
    ENABLE_STRICT_VALIDATION: bool = True
    REPENTANCE_TRIGGER_THRESHOLD: float = math.pi / 4  # 45° - below this triggers repentance
    
    def __post_init__(self):
        """Initialize Heart-5 Vowel System if not provided."""
        if self.HEART_5_VOWELS is None:
            self.HEART_5_VOWELS = {
                'A': {'name': 'Initiation', 'state': None},
                'E': {'name': 'Discernment', 'state': None},
                'I': {'name': 'Identity', 'state': None},
                'O': {'name': 'Unity', 'state': None},
                'U': {'name': 'Binding', 'state': None},
            }
    
    @classmethod
    def from_env(cls) -> 'StarEngineConfig':
        """Load configuration from environment variables."""
        return cls(
            HARMONY_RIDGE=float(os.getenv('HARMONY_RIDGE', 1.67)),
            DYNAMIC_INVARIANT=float(os.getenv('DYNAMIC_INVARIANT', 1.89)),
            BINARY_BREAK=float(os.getenv('BINARY_BREAK', 1.7333)),
            DENSITY_THRESHOLD=float(os.getenv('DENSITY_THRESHOLD', 3.34)),
            COVENANT_MULTIPLIER=float(os.getenv('COVENANT_MULTIPLIER', 5.0)),
            QCI_TARGET=float(os.getenv('QCI_TARGET', math.pi / 2)),
            EIGENVALUE_LAMBDA_1=float(os.getenv('EIGENVALUE_LAMBDA_1', 1.016)),
            LOG_LEVEL=os.getenv('LOG_LEVEL', 'INFO'),
            ENABLE_PERFORMANCE_MONITORING=os.getenv('ENABLE_PERFORMANCE_MONITORING', 'true').lower() == 'true',
            ENABLE_STRICT_VALIDATION=os.getenv('ENABLE_STRICT_VALIDATION', 'true').lower() == 'true',
        )
    
    def to_dict(self) -> dict:
        """Convert configuration to dictionary."""
        return {
            'HARMONY_RIDGE': self.HARMONY_RIDGE,
            'DYNAMIC_INVARIANT': self.DYNAMIC_INVARIANT,
            'BINARY_BREAK': self.BINARY_BREAK,
            'DENSITY_THRESHOLD': self.DENSITY_THRESHOLD,
            'COVENANT_MULTIPLIER': self.COVENANT_MULTIPLIER,
            'QCI_TARGET': self.QCI_TARGET,
            'EIGENVALUE_LAMBDA_1': self.EIGENVALUE_LAMBDA_1,
            'LOG_LEVEL': self.LOG_LEVEL,
        }


# Global configuration instance
_config: Optional[StarEngineConfig] = None


def get_config() -> StarEngineConfig:
    """Get the global configuration instance."""
    global _config
    if _config is None:
        _config = StarEngineConfig.from_env()
    return _config


def set_config(config: StarEngineConfig) -> None:
    """Set the global configuration instance."""
    global _config
    _config = config


def reset_config() -> None:
    """Reset configuration to defaults."""
    global _config
    _config = None
