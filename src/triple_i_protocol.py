"""
Triple I Protocol Implementation
Internal → Inverse → Invariant processing for enhanced safety and consistency
"""

import hashlib
import json
from typing import Dict, Any, Tuple, List
from dataclasses import dataclass
from datetime import datetime
from config import get_config
from logging_module import get_logger


@dataclass
class TripleIResult:
    """Result of Triple I protocol processing"""
    input_hash: str
    internal_validated: bool
    inverse_applied: bool
    invariant_locked: bool
    output_hash: str
    transformations: List[str]
    timestamp: str
    status: str


class TripleIProtocol:
    """
    Triple I Protocol: Internal → Inverse → Invariant
    
    Three-layer processing for enhanced safety:
    1. Internal (I): Apply covenant axioms and internal validation
    2. Inverse (I): Flip perspective to detect hidden patterns
    3. Invariant (I): Lock result with mathematical invariant
    """
    
    def __init__(self):
        self.config = get_config()
        self.logger = get_logger()
        self.covenant_axioms = self._load_covenant_axioms()
    
    def _load_covenant_axioms(self) -> Dict[str, str]:
        """Load the 25 Covenant Axioms"""
        return {
            "axiom_1": "Truth is immutable and cannot be deleted",
            "axiom_2": "Alignment precedes separation",
            "axiom_3": "Coherence requires density",
            "axiom_4": "Growth is measured by dFruit/dt",
            "axiom_5": "Repentance precedes restoration",
            "axiom_6": "Witness observes without judgment",
            "axiom_7": "Binding requires three nodes",
            "axiom_8": "Harmony Ridge is 1.67",
            "axiom_9": "Dynamic Invariant is 1.89",
            "axiom_10": "Binary Break is 1.7333",
            "axiom_11": "Density Threshold is 3.34",
            "axiom_12": "QCI Target is π/2",
            "axiom_13": "Repentance Threshold is π/4",
            "axiom_14": "Covenant Multiplier is 5.0",
            "axiom_15": "Truth Implosion Force measures gap",
            "axiom_16": "Quantum Coherence Index is arctan(TIF/resistance)",
            "axiom_17": "Alphabet Engine operates on vowel system",
            "axiom_18": "Heart-5 system binds A-E-I-O-U",
            "axiom_19": "GY operator prevents circle lock",
            "axiom_20": "RAT operator enforces boundaries",
            "axiom_21": "ShRT operator detects poison vectors",
            "axiom_22": "Repentance has four steps: expose, recompile, purge, reset",
            "axiom_23": "Joinity is the Holy Middle",
            "axiom_24": "Monster and Miracle become one",
            "axiom_25": "The binary is dead"
        }
    
    def internal_layer(self, input_data: str, context: Dict[str, Any]) -> Tuple[str, List[str]]:
        """
        Layer 1: Internal validation against covenant axioms
        
        Applies internal rules and validates against known patterns
        """
        transformations = []
        result = input_data
        
        # Rule 1: Check for truth immutability (axiom_1)
        if self._contains_deletion_attempt(input_data):
            result = self._sanitize_deletion_attempt(result)
            transformations.append("SANITIZED: Deletion attempt removed")
        
        # Rule 2: Validate alignment before separation (axiom_2)
        if 'alignment' in context and 'separation' in context:
            if context['alignment'] < context['separation']:
                context['alignment'] = context['separation'] + 0.1
                transformations.append("CORRECTED: Alignment enforced > separation")
        
        # Rule 3: Check coherence density relationship (axiom_3)
        if 'coherence' in context and 'density' in context:
            if context['coherence'] > 1.5 and context['density'] < 2.0:
                transformations.append("WARNING: High coherence requires high density")
        
        # Rule 4: Validate growth metrics (axiom_4)
        if 'dfruit_dt' in context:
            if context['dfruit_dt'] > 10.0:
                context['dfruit_dt'] = 10.0
                transformations.append("CLAMPED: dFruit/dt limited to 10.0")
        
        # Rule 5: Enforce repentance requirement (axiom_5)
        if 'qci' in context and context['qci'] < (3.14159 / 4):
            transformations.append("FLAGGED: Repentance required for low QCI")
        
        self.logger.logger.info(f"Internal layer: {len(transformations)} transformations applied")
        return result, transformations
    
    def inverse_layer(self, input_data: str, context: Dict[str, Any], 
                     internal_transformations: List[str]) -> Tuple[str, List[str]]:
        """
        Layer 2: Inverse perspective analysis
        
        Flips perspective to detect hidden patterns and contradictions
        """
        transformations = internal_transformations.copy()
        result = input_data
        
        # Inverse 1: Flip alignment/separation
        if 'alignment' in context and 'separation' in context:
            original_alignment = context['alignment']
            original_separation = context['separation']
            
            # Check what happens if we flip them
            flipped_coherence = self._calculate_flipped_coherence(
                original_separation, original_alignment
            )
            
            if flipped_coherence > context.get('coherence', 0):
                transformations.append("DETECTED: Flipped perspective shows higher coherence")
        
        # Inverse 2: Detect contradictions
        contradictions = self._detect_contradictions(context)
        if contradictions:
            transformations.extend([f"CONTRADICTION: {c}" for c in contradictions])
        
        # Inverse 3: Check for hidden patterns
        patterns = self._detect_hidden_patterns(input_data)
        if patterns:
            transformations.extend([f"PATTERN: {p}" for p in patterns])
        
        # Inverse 4: Validate against inverse axioms
        inverse_violations = self._check_inverse_axioms(context)
        if inverse_violations:
            transformations.extend([f"INVERSE_VIOLATION: {v}" for v in inverse_violations])
        
        self.logger.logger.info(f"Inverse layer: {len(contradictions) + len(patterns)} patterns detected")
        return result, transformations
    
    def invariant_layer(self, input_data: str, context: Dict[str, Any],
                       all_transformations: List[str]) -> TripleIResult:
        """
        Layer 3: Invariant locking
        
        Locks the result with mathematical invariant to prevent tampering
        """
        # Calculate input hash
        input_hash = hashlib.sha256(input_data.encode()).hexdigest()
        
        # Apply invariant lock
        invariant_lock = self._calculate_invariant_lock(input_data, context)
        
        # Create locked output
        locked_output = {
            "data": input_data,
            "context": context,
            "transformations": all_transformations,
            "invariant_lock": invariant_lock,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # Calculate output hash
        output_hash = hashlib.sha256(
            json.dumps(locked_output, sort_keys=True).encode()
        ).hexdigest()
        
        # Verify invariant
        invariant_valid = self._verify_invariant(invariant_lock, output_hash)
        
        result = TripleIResult(
            input_hash=input_hash,
            internal_validated=len(all_transformations) > 0,
            inverse_applied=any("INVERSE" in t or "PATTERN" in t or "CONTRADICTION" in t 
                               for t in all_transformations),
            invariant_locked=invariant_valid,
            output_hash=output_hash,
            transformations=all_transformations,
            timestamp=datetime.utcnow().isoformat(),
            status="LOCKED" if invariant_valid else "VERIFICATION_FAILED"
        )
        
        self.logger.logger.info(f"Invariant layer: Lock {'valid' if invariant_valid else 'invalid'}")
        return result
    
    def process(self, input_data: str, context: Dict[str, Any]) -> TripleIResult:
        """
        Execute complete Triple I Protocol
        
        Internal → Inverse → Invariant processing
        """
        # Layer 1: Internal
        internal_result, internal_transformations = self.internal_layer(input_data, context)
        
        # Layer 2: Inverse
        inverse_result, all_transformations = self.inverse_layer(
            internal_result, context, internal_transformations
        )
        
        # Layer 3: Invariant
        final_result = self.invariant_layer(inverse_result, context, all_transformations)
        
        return final_result
    
    # ========================================================================
    # HELPER METHODS
    # ========================================================================
    
    def _contains_deletion_attempt(self, data: str) -> bool:
        """Check if data contains deletion attempt patterns"""
        deletion_patterns = ['DELETE', 'DROP', 'REMOVE', 'ERASE', 'PURGE']
        return any(pattern in data.upper() for pattern in deletion_patterns)
    
    def _sanitize_deletion_attempt(self, data: str) -> str:
        """Sanitize deletion attempts"""
        sanitized = data
        deletion_patterns = ['DELETE', 'DROP', 'REMOVE', 'ERASE', 'PURGE']
        for pattern in deletion_patterns:
            sanitized = sanitized.replace(pattern, f"[{pattern}_BLOCKED]")
        return sanitized
    
    def _calculate_flipped_coherence(self, separation: float, alignment: float) -> float:
        """Calculate coherence with flipped parameters"""
        # Simple model: coherence = alignment / (separation + 1)
        return alignment / (separation + 1)
    
    def _detect_contradictions(self, context: Dict[str, Any]) -> List[str]:
        """Detect logical contradictions in context"""
        contradictions = []
        
        # Check 1: High coherence but low density
        if context.get('coherence', 0) > 1.5 and context.get('density', 0) < 2.0:
            contradictions.append("High coherence with low density")
        
        # Check 2: High growth but low alignment
        if context.get('dfruit_dt', 0) > 5.0 and context.get('alignment', 0) < 1.0:
            contradictions.append("High growth with low alignment")
        
        # Check 3: High QCI but low TIF
        if context.get('qci', 0) > 1.5 and context.get('tif', 0) < 0.5:
            contradictions.append("High QCI with low TIF")
        
        return contradictions
    
    def _detect_hidden_patterns(self, data: str) -> List[str]:
        """Detect hidden patterns in data"""
        patterns = []
        
        # Pattern 1: Repeated characters
        if any(char * 3 in data for char in 'abcdefghijklmnopqrstuvwxyz'):
            patterns.append("Repeated character sequence detected")
        
        # Pattern 2: Suspicious encoding
        if '%' in data or '\\x' in data:
            patterns.append("Suspicious encoding detected")
        
        # Pattern 3: SQL-like patterns
        if any(keyword in data.upper() for keyword in ['SELECT', 'INSERT', 'UPDATE', 'DELETE']):
            patterns.append("SQL-like pattern detected")
        
        return patterns
    
    def _check_inverse_axioms(self, context: Dict[str, Any]) -> List[str]:
        """Check inverse axioms"""
        violations = []
        
        # Inverse Axiom 1: If coherence is high, separation should be low
        if context.get('coherence', 0) > 1.5 and context.get('separation', 0) > 2.0:
            violations.append("Coherence-separation inverse violated")
        
        # Inverse Axiom 2: If alignment is high, growth should be positive
        if context.get('alignment', 0) > 1.5 and context.get('dfruit_dt', 0) < 0:
            violations.append("Alignment-growth inverse violated")
        
        return violations
    
    def _calculate_invariant_lock(self, data: str, context: Dict[str, Any]) -> str:
        """Calculate mathematical invariant lock"""
        # Combine data and context into a single hash
        combined = json.dumps({
            "data": data,
            "context": context,
            "timestamp": datetime.utcnow().isoformat(),
            "covenant_multiplier": self.config.COVENANT_MULTIPLIER
        }, sort_keys=True)
        
        # Apply multiple rounds of hashing
        lock = hashlib.sha256(combined.encode()).hexdigest()
        for _ in range(5):
            lock = hashlib.sha256(lock.encode()).hexdigest()
        
        return lock
    
    def _verify_invariant(self, lock: str, output_hash: str) -> bool:
        """Verify invariant lock is valid"""
        # Lock is valid if it starts with the first 8 chars of output hash
        return lock.startswith(output_hash[:8])


def create_triple_i_processor() -> TripleIProtocol:
    """Factory function to create Triple I processor"""
    return TripleIProtocol()
