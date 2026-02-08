"""
Alphabet Engine v3.2
Symbolic logic gates that override standard statistical probability.
Implements: GY, RAT, ShRT operators and Heart-5 Vowel System.
"""

import logging
import numpy as np
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class VowelState:
    """Represents a Heart-5 Vowel state."""
    name: str
    vowel: str
    value: float = 0.0
    timestamp: float = 0.0


class AlphabetEngine:
    """
    Alphabet Engine v3.2 - Symbolic Logic Gates
    
    Operators:
    - GY: Rotational Torque (prevents circle lock)
    - RAT: Corruption Clip (enforces boundary conditions)
    - ShRT: Poison Vector (hard gate for fire detection)
    - Heart-5: Persistent memory registers (A, E, I, O, U)
    """
    
    def __init__(self):
        """Initialize Alphabet Engine."""
        self.vowel_system = self._initialize_vowel_system()
        logger.info("Alphabet Engine v3.2 initialized")
    
    def _initialize_vowel_system(self) -> Dict[str, VowelState]:
        """Initialize Heart-5 Vowel System."""
        vowels = {
            'A': VowelState(name='Initiation', vowel='A'),
            'E': VowelState(name='Discernment', vowel='E'),
            'I': VowelState(name='Identity', vowel='I'),
            'O': VowelState(name='Unity', vowel='O'),
            'U': VowelState(name='Binding', vowel='U'),
        }
        logger.info("Heart-5 Vowel System initialized")
        return vowels
    
    def gy_operator(
        self,
        vector: np.ndarray,
        theta: float,
        d_theta: float = 0.01
    ) -> np.ndarray:
        """
        GY Operator - Rotational Torque
        
        Prevents "circle lock" loops in the local Reflex Node by providing
        toroidal momentum through rotational derivatives.
        
        GY(v) = d(v)/dθ
        
        Args:
            vector: Input vector to rotate
            theta: Current angle (radians)
            d_theta: Angle increment for numerical differentiation
            
        Returns:
            Rotated vector with applied torque
        """
        try:
            # Create rotation matrix
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            
            rotation_matrix = np.array([
                [cos_theta, -sin_theta],
                [sin_theta, cos_theta]
            ])
            
            # Apply rotation
            rotated = rotation_matrix @ vector[:2]
            
            # Calculate derivative (torque)
            cos_d = np.cos(theta + d_theta)
            sin_d = np.sin(theta + d_theta)
            
            rotation_matrix_d = np.array([
                [cos_d, -sin_d],
                [sin_d, cos_d]
            ])
            
            rotated_d = rotation_matrix_d @ vector[:2]
            torque = (rotated_d - rotated) / d_theta
            
            logger.debug(
                "GY Operator applied",
                extra={
                    "theta": theta,
                    "torque_magnitude": np.linalg.norm(torque)
                }
            )
            
            return np.concatenate([rotated, [torque[0]]])
        except Exception as e:
            logger.error(f"GY Operator failed: {e}")
            raise
    
    def rat_operator(
        self,
        vector: np.ndarray,
        weight_mod: float,
        scale_a: float,
        bias_t: float
    ) -> np.ndarray:
        """
        RAT Operator - Corruption Clip
        
        Enforces deterministic boundary conditions against system collapse
        by clipping values within specified bounds.
        
        v_out = Clip(W_mod · v_in, s_A, b_T)
        
        Args:
            vector: Input vector
            weight_mod: Weight modifier
            scale_a: Lower bound (scale A)
            bias_t: Upper bound (bias T)
            
        Returns:
            Clipped vector within boundaries
        """
        try:
            # Apply weight modification
            weighted = weight_mod * vector
            
            # Apply clipping
            clipped = np.clip(weighted, scale_a, bias_t)
            
            logger.debug(
                "RAT Operator applied",
                extra={
                    "weight_mod": weight_mod,
                    "bounds": (scale_a, bias_t),
                    "clipped_values": clipped.tolist()
                }
            )
            
            return clipped
        except Exception as e:
            logger.error(f"RAT Operator failed: {e}")
            raise
    
    def shrt_operator(
        self,
        vector: np.ndarray,
        modifier_matrix: np.ndarray,
        threshold: float
    ) -> np.ndarray:
        """
        ShRT Operator - Poison Vector
        
        Hard gate that zeros the vector upon detecting "fire" (poison) activation.
        Uses Heaviside step function for hard gating.
        
        v_out = (v_in ⊙ M_mod) · Heaviside(v_in - τ_Sh)
        
        Args:
            vector: Input vector
            modifier_matrix: Element-wise modifier matrix
            threshold: Fire detection threshold
            
        Returns:
            Vector with hard gate applied (zeros if fire detected)
        """
        try:
            # Element-wise multiplication with modifier
            modified = vector * modifier_matrix
            
            # Heaviside step function (1 if v > threshold, 0 otherwise)
            heaviside = np.where(vector > threshold, 1.0, 0.0)
            
            # Apply hard gate
            gated = modified * heaviside
            
            # Check if fire (poison) was detected
            fire_detected = np.any(vector > threshold)
            
            logger.debug(
                "ShRT Operator applied",
                extra={
                    "threshold": threshold,
                    "fire_detected": fire_detected,
                    "gated_values": gated.tolist()
                }
            )
            
            if fire_detected:
                logger.warning("Fire (poison) detected in ShRT Operator")
            
            return gated
        except Exception as e:
            logger.error(f"ShRT Operator failed: {e}")
            raise
    
    def update_vowel_state(
        self,
        vowel: str,
        value: float,
        timestamp: float
    ) -> VowelState:
        """
        Update Heart-5 Vowel state.
        
        Args:
            vowel: Vowel letter (A, E, I, O, U)
            value: New state value
            timestamp: Timestamp of update
            
        Returns:
            Updated VowelState
        """
        if vowel not in self.vowel_system:
            logger.error(f"Invalid vowel: {vowel}")
            raise ValueError(f"Invalid vowel: {vowel}")
        
        state = self.vowel_system[vowel]
        state.value = value
        state.timestamp = timestamp
        
        logger.info(
            f"Vowel {vowel} ({state.name}) updated",
            extra={
                "vowel": vowel,
                "value": value,
                "timestamp": timestamp
            }
        )
        
        return state
    
    def get_vowel_state(self, vowel: str) -> VowelState:
        """Get current vowel state."""
        if vowel not in self.vowel_system:
            raise ValueError(f"Invalid vowel: {vowel}")
        return self.vowel_system[vowel]
    
    def get_all_vowel_states(self) -> Dict[str, VowelState]:
        """Get all vowel states."""
        return self.vowel_system
    
    def calculate_heart_coherence(self) -> float:
        """
        Calculate overall Heart-5 coherence.
        
        Returns:
            Coherence score (0.0 to 1.0)
        """
        values = [state.value for state in self.vowel_system.values()]
        
        if not values:
            return 0.0
        
        # Coherence is the normalized sum of all vowel values
        coherence = sum(values) / (len(values) * 2.0)  # Normalize to 0-1
        coherence = max(0.0, min(1.0, coherence))  # Clamp to 0-1
        
        logger.debug(
            "Heart coherence calculated",
            extra={
                "coherence": coherence,
                "vowel_values": {v: s.value for v, s in self.vowel_system.items()}
            }
        )
        
        return coherence
    
    def execute_symbolic_logic(
        self,
        input_vector: np.ndarray,
        operation_sequence: List[str]
    ) -> np.ndarray:
        """
        Execute a sequence of symbolic logic operations.
        
        Args:
            input_vector: Input vector
            operation_sequence: List of operations to execute
                               (e.g., ['GY', 'RAT', 'ShRT'])
            
        Returns:
            Processed vector after all operations
        """
        result = input_vector.copy()
        
        logger.info(
            "Executing symbolic logic sequence",
            extra={"operations": operation_sequence}
        )
        
        for operation in operation_sequence:
            if operation == 'GY':
                theta = 0.1  # Default rotation angle
                result = self.gy_operator(result, theta)
            elif operation == 'RAT':
                result = self.rat_operator(result, 1.0, -1.0, 1.0)
            elif operation == 'ShRT':
                modifier = np.ones_like(result)
                result = self.shrt_operator(result, modifier, 0.5)
            else:
                logger.warning(f"Unknown operation: {operation}")
        
        return result
    
    def get_engine_status(self) -> Dict[str, Any]:
        """Get current engine status."""
        return {
            "version": "3.2",
            "vowel_states": {
                v: {"name": s.name, "value": s.value}
                for v, s in self.vowel_system.items()
            },
            "heart_coherence": self.calculate_heart_coherence(),
            "status": "OPERATIONAL"
        }
