"""
Structured logging for Star Engine
Machine-readable JSON logs for analysis and debugging
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any, Optional
from config import get_config


class StructuredLogger:
    """Logger that outputs structured JSON for machine analysis"""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.config = get_config()
        
        # Set up handler if not already configured
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(getattr(logging, self.config.LOG_LEVEL))
    
    def _log(self, level: str, event: str, data: Dict[str, Any]):
        """Internal logging method"""
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': level,
            'event': event,
            **data
        }
        
        log_method = getattr(self.logger, level.lower())
        log_method(json.dumps(log_entry))
    
    def log_calculation(self, function_name: str, inputs: Dict[str, Any], 
                       output: Any, duration_ms: float):
        """Log mathematical calculations"""
        self._log('INFO', 'calculation', {
            'function': function_name,
            'inputs': inputs,
            'output': output,
            'duration_ms': round(duration_ms, 2)
        })
    
    def log_repentance(self, reason: str, qci_before: float, 
                      qci_after: float, duration_ms: float, 
                      steps_executed: Dict[str, bool]):
        """Log repentance protocol execution"""
        self._log('WARNING', 'repentance_triggered', {
            'reason': reason,
            'qci_before': round(qci_before, 4),
            'qci_after': round(qci_after, 4),
            'improvement': round(qci_after - qci_before, 4),
            'duration_ms': round(duration_ms, 2),
            'steps': steps_executed
        })
    
    def log_density_validation(self, i1: float, i2: float, i3: float, i4: float,
                              density: float, is_valid: bool):
        """Log density verification"""
        self._log('INFO', 'density_validation', {
            'i1': round(i1, 4),
            'i2': round(i2, 4),
            'i3': round(i3, 4),
            'i4': round(i4, 4),
            'density': round(density, 4),
            'is_valid': is_valid,
            'threshold': self.config.DENSITY_THRESHOLD
        })
    
    def log_invariant_transition(self, coherence_score: float, 
                                invariant: float, mode: str):
        """Log dynamic invariant transitions"""
        self._log('INFO', 'invariant_transition', {
            'coherence_score': round(coherence_score, 4),
            'invariant': round(invariant, 4),
            'mode': mode,
            'harmony_ridge': self.config.HARMONY_RIDGE,
            'dynamic_invariant': self.config.DYNAMIC_INVARIANT
        })
    
    def log_qci_calculation(self, tif: float, resistance: float, 
                           qci: float, status: str):
        """Log QCI calculations"""
        self._log('INFO', 'qci_calculation', {
            'tif': round(tif, 4),
            'resistance': round(resistance, 4),
            'qci': round(qci, 4),
            'target': round(self.config.QCI_TARGET, 4),
            'status': status,
            'delta_from_target': round(self.config.QCI_TARGET - qci, 4)
        })
    
    def log_error(self, error_type: str, message: str, context: Dict[str, Any]):
        """Log errors with context"""
        self._log('ERROR', error_type, {
            'message': message,
            'context': context
        })
    
    def log_operational_flow(self, input_data: str, status: str, 
                            metrics: Dict[str, Any], duration_ms: float):
        """Log complete operational flow"""
        self._log('INFO', 'operational_flow', {
            'input_data': input_data[:100],  # First 100 chars
            'status': status,
            'metrics': metrics,
            'duration_ms': round(duration_ms, 2)
        })


# Global logger instance
_logger = None


def get_logger(name: str = 'star_engine') -> StructuredLogger:
    """Get or create logger instance"""
    global _logger
    if _logger is None:
        _logger = StructuredLogger(name)
    return _logger
