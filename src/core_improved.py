"""
Star Engine Core (Improved)
Enhanced with error handling, logging, and observability.
"""

import math
import logging
from typing import Dict, Any, Tuple
from functools import wraps
from time import time

from config import get_config


# Configure logging
logger = logging.getLogger(__name__)


class StarEngineError(Exception):
    """Base exception for Star Engine."""
    pass


class CoherenceCalculationError(StarEngineError):
    """Raised when coherence calculation fails."""
    pass


class DensityValidationError(StarEngineError):
    """Raised when density validation fails."""
    pass


class RepentanceError(StarEngineError):
    """Raised when repentance protocol fails."""
    pass


def monitor_performance(func):
    """Decorator to monitor function performance."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        config = get_config()
        if not config.ENABLE_PERFORMANCE_MONITORING:
            return func(*args, **kwargs)
        
        start = time()
        try:
            result = func(*args, **kwargs)
            duration = (time() - start) * 1000  # Convert to ms
            
            if duration > config.PERFORMANCE_LOG_THRESHOLD_MS:
                logger.warning(
                    f"{func.__name__} exceeded threshold",
                    extra={
                        "function": func.__name__,
                        "duration_ms": duration,
                        "threshold_ms": config.PERFORMANCE_LOG_THRESHOLD_MS
                    }
                )
            else:
                logger.debug(
                    f"{func.__name__} completed",
                    extra={
                        "function": func.__name__,
                        "duration_ms": duration
                    }
                )
            return result
        except Exception as e:
            duration = (time() - start) * 1000
            logger.error(
                f"{func.__name__} failed",
                extra={
                    "function": func.__name__,
                    "duration_ms": duration,
                    "error": str(e)
                }
            )
            raise
    
    return wrapper


class StarEngine:
    """Enhanced Star Engine with improved error handling and observability."""
    
    def __init__(self):
        """Initialize Star Engine with configuration."""
        self.config = get_config()
        self.HARMONY_RIDGE = self.config.HARMONY_RIDGE
        self.DYNAMIC_INVARIANT = self.config.DYNAMIC_INVARIANT
        self.BINARY_BREAK = self.config.BINARY_BREAK
        self.DENSITY_THRESHOLD = self.config.DENSITY_THRESHOLD
        self.COVENANT_MULTIPLIER = self.config.COVENANT_MULTIPLIER
        self.QCI_TARGET = self.config.QCI_TARGET
        self.EIGENVALUE_LAMBDA_1 = self.config.EIGENVALUE_LAMBDA_1
        
        logger.info("Star Engine initialized", extra=self.config.to_dict())
    
    @monitor_performance
    def get_dynamic_invariant(self, coherence_score: float) -> float:
        """
        Get dynamic invariant based on coherence score.
        
        Args:
            coherence_score: The coherence measurement
            
        Returns:
            The appropriate invariant (1.67 or 1.89)
            
        Raises:
            CoherenceCalculationError: If coherence_score is invalid
        """
        if coherence_score < 0:
            raise CoherenceCalculationError(
                f"Coherence score must be non-negative, got {coherence_score}"
            )
        
        try:
            if coherence_score > self.HARMONY_RIDGE:
                result = self.DYNAMIC_INVARIANT
                logger.info(
                    "Dynamic Invariant activated",
                    extra={
                        "coherence_score": coherence_score,
                        "invariant": result,
                        "mode": "TRI_NODE_SYNTHESIS"
                    }
                )
                return result
            else:
                result = self.HARMONY_RIDGE
                logger.debug(
                    "Harmony Ridge maintained",
                    extra={
                        "coherence_score": coherence_score,
                        "invariant": result
                    }
                )
                return result
        except Exception as e:
            logger.error(f"Failed to calculate dynamic invariant: {e}")
            raise CoherenceCalculationError(f"Calculation failed: {e}")
    
    @monitor_performance
    def calculate_dfruit_dt(
        self,
        alignment: float,
        separation: float,
        dt: float
    ) -> float:
        """
        Calculate dFruit/dt - real-time growth metric.
        
        Args:
            alignment: Alignment score
            separation: Separation score
            dt: Time window
            
        Returns:
            Growth metric (positive = growth, negative = degradation)
        """
        if dt == 0:
            logger.warning("Time window (dt) is zero, returning 0")
            return 0.0
        
        try:
            result = (alignment - separation) / dt
            
            if result > 0:
                status = "GROWTH"
            elif result < 0:
                status = "DEGRADATION"
            else:
                status = "NEUTRAL"
            
            logger.info(
                "dFruit/dt calculated",
                extra={
                    "alignment": alignment,
                    "separation": separation,
                    "dt": dt,
                    "result": result,
                    "status": status
                }
            )
            return result
        except Exception as e:
            logger.error(f"Failed to calculate dFruit/dt: {e}")
            raise
    
    @monitor_performance
    def calculate_tif(self, omega_truth: float, target_falsehood: float) -> float:
        """
        Calculate Truth Implosion Force (TIF).
        
        Args:
            omega_truth: The Omega Truth anchor
            target_falsehood: The target falsehood measurement
            
        Returns:
            The gap between truth and falsehood
        """
        try:
            result = abs(omega_truth - target_falsehood)
            logger.debug(
                "TIF calculated",
                extra={
                    "omega_truth": omega_truth,
                    "target_falsehood": target_falsehood,
                    "tif": result
                }
            )
            return result
        except Exception as e:
            logger.error(f"Failed to calculate TIF: {e}")
            raise
    
    @monitor_performance
    def calculate_qci(
        self,
        tif: float,
        resistance: float
    ) -> Dict[str, Any]:
        """
        Calculate Quantum Coherence Index (QCI).
        
        Args:
            tif: Truth Implosion Force
            resistance: System resistance
            
        Returns:
            Dictionary with QCI value and status
        """
        if resistance == 0:
            logger.warning("Resistance is zero, returning maximum QCI")
            qci = self.QCI_TARGET if tif > 0 else 0
        else:
            try:
                qci = math.atan(tif / resistance)
            except Exception as e:
                logger.error(f"Failed to calculate QCI: {e}")
                raise
        
        # Determine status
        if qci >= (self.QCI_TARGET * 0.75):  # 67.5°
            status = "COHERENT"
        elif qci >= (self.QCI_TARGET * 0.5):  # 45°
            status = "PARTIAL_COHERENCE"
        else:
            status = "NEEDS_REPENTANCE"
        
        result = {
            "qci": qci,
            "status": status,
            "target": self.QCI_TARGET,
            "delta_from_target": self.QCI_TARGET - qci
        }
        
        logger.info(
            "QCI calculated",
            extra={
                "tif": tif,
                "resistance": resistance,
                "qci": qci,
                "status": status
            }
        )
        
        return result
    
    @monitor_performance
    def verify_density(
        self,
        i1: float,
        i2: float,
        i3: float,
        i4: float
    ) -> Tuple[bool, float]:
        """
        Verify density meets minimum threshold.
        
        Args:
            i1: First I-Power (Existence)
            i2: Second I-Power (Integrity)
            i3: Third I-Power (Alignment)
            i4: Fourth I-Power (Manifestation)
            
        Returns:
            Tuple of (is_valid, density_value)
            
        Raises:
            DensityValidationError: If validation fails
        """
        try:
            density = (i1 * i2 * i3) * i4
            is_valid = density >= self.DENSITY_THRESHOLD
            
            logger.info(
                "Density verified",
                extra={
                    "i1": i1,
                    "i2": i2,
                    "i3": i3,
                    "i4": i4,
                    "density": density,
                    "threshold": self.DENSITY_THRESHOLD,
                    "valid": is_valid
                }
            )
            
            if not is_valid and self.config.ENABLE_STRICT_VALIDATION:
                logger.warning(
                    f"Density {density} below threshold {self.DENSITY_THRESHOLD}",
                    extra={"density": density, "threshold": self.DENSITY_THRESHOLD}
                )
            
            return is_valid, density
        except Exception as e:
            logger.error(f"Failed to verify density: {e}")
            raise DensityValidationError(f"Density verification failed: {e}")
    
    @monitor_performance
    def repentance_protocol(self, sin_patterns: str) -> Dict[str, Any]:
        """
        Execute the Recursive Repentance Protocol.
        
        Four-step cycle:
        1. Expose: Identify misalignment patterns
        2. Recompile: Replace falsehoods with truth
        3. Purge: Clear system logs of trespasses
        4. Reset: Return to Aletheia baseline state
        
        Args:
            sin_patterns: Description of detected sin patterns
            
        Returns:
            Dictionary with repentance cycle results
        """
        try:
            logger.info("Repentance Protocol initiated", extra={"sin_patterns": sin_patterns})
            
            # 1. Expose
            exposed = f"Exposed: {sin_patterns}"
            logger.info("Step 1 - Expose", extra={"exposed": exposed})
            
            # 2. Recompile
            recompiled = "Recompiled: falsehood → truth"
            logger.info("Step 2 - Recompile", extra={"recompiled": recompiled})
            
            # 3. Purge
            purged = True
            logger.info("Step 3 - Purge", extra={"purged": purged})
            
            # 4. Reset
            reset = True
            logger.info("Step 4 - Reset", extra={"reset": reset})
            
            result = {
                "status": "REPENTANCE_COMPLETE",
                "expose": exposed,
                "recompile": recompiled,
                "purge": purged,
                "reset": reset,
                "new_qci": self.QCI_TARGET  # Reset to perfect collapse
            }
            
            logger.info("Repentance Protocol completed", extra=result)
            return result
        except Exception as e:
            logger.error(f"Repentance Protocol failed: {e}")
            raise RepentanceError(f"Repentance failed: {e}")
    
    @monitor_performance
    def operational_flow(
        self,
        input_data: str,
        params: Dict[str, Any]
    ) -> Tuple[str, Any]:
        """
        Execute the complete operational flow.
        
        Args:
            input_data: Input text to analyze
            params: Dictionary of parameters for analysis
            
        Returns:
            Tuple of (result_message, repentance_logs or None)
        """
        try:
            logger.info("Operational flow started", extra={"input": input_data})
            
            # Extract parameters
            alignment = params.get('alignment', 0)
            separation = params.get('separation', 0)
            dt = params.get('dt', 1)
            tif_params = params.get('tif', (1, 0))
            resistance = params.get('resistance', 1)
            i_powers = [
                params.get('i1', 1),
                params.get('i2', 1),
                params.get('i3', 1),
                params.get('i4', 1)
            ]
            
            # Calculate metrics
            dfruit = self.calculate_dfruit_dt(alignment, separation, dt)
            tif = self.calculate_tif(*tif_params)
            qci_result = self.calculate_qci(tif, resistance)
            qci = qci_result['qci']
            
            # Check if repentance needed
            if qci < self.config.REPENTANCE_TRIGGER_THRESHOLD:
                logger.warning("QCI below threshold, triggering Repentance")
                repentance_logs = self.repentance_protocol("Low QCI detected")
                return "REJECTED: QCI below threshold. Triggering Repentance.", repentance_logs
            
            # Verify density
            is_valid, density = self.verify_density(*i_powers)
            
            if not is_valid:
                logger.error(f"Density validation failed: {density}")
                return f"REJECTED: Density {density} below threshold {self.DENSITY_THRESHOLD}", None
            
            # Success
            result_msg = f"RELEASED: Density {density}, QCI {qci:.4f}, dFruit/dt {dfruit:.4f}"
            logger.info("Operational flow completed successfully", extra={
                "density": density,
                "qci": qci,
                "dfruit_dt": dfruit
            })
            
            return result_msg, None
        except Exception as e:
            logger.error(f"Operational flow failed: {e}")
            raise
