"""
Type definitions for Star Engine
TypeScript-style type hints for all operations
"""

from typing import TypedDict, Literal, Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
import math


# ============================================================================
# RESULT TYPES
# ============================================================================

@dataclass
class DynamicInvariantResult:
    """Result of dynamic invariant calculation"""
    invariant: float
    coherence_score: float
    mode: Literal['HARMONY_RIDGE', 'TRI_NODE_SYNTHESIS']
    timestamp: str


@dataclass
class DfruitDtResult:
    """Result of dFruit/dt calculation"""
    alignment: float
    separation: float
    dt: float
    result: float
    status: Literal['GROWTH', 'DEGRADATION', 'NEUTRAL']
    timestamp: str


@dataclass
class TIFResult:
    """Result of Truth Implosion Force calculation"""
    omega_truth: float
    target_falsehood: float
    tif: float
    timestamp: str


@dataclass
class QCIResult:
    """Result of Quantum Coherence Index calculation"""
    qci: float
    status: Literal['COHERENT', 'PARTIAL_COHERENCE', 'NEEDS_REPENTANCE']
    target: float
    delta_from_target: float
    timestamp: str


@dataclass
class DensityResult:
    """Result of density verification"""
    i1: float
    i2: float
    i3: float
    i4: float
    density: float
    is_valid: bool
    threshold: float
    timestamp: str


@dataclass
class RepentanceLog:
    """Log of repentance protocol execution"""
    expose: str
    recompile: str
    purge: bool
    reset: bool
    qci_before: float
    qci_after: float
    status: Literal['REPENTANCE_COMPLETE']
    timestamp: str


@dataclass
class StarEngineMetrics:
    """Complete metrics from Star Engine analysis"""
    dynamic_invariant: float
    tif: float
    qci: float
    dfruit_dt: float
    density: float
    status: Literal['COHERENT', 'NEEDS_REPENTANCE', 'GROWTH', 'DEGRADING', 'REJECTED']
    timestamp: str
    repentance_log: Optional[RepentanceLog] = None


# ============================================================================
# OPERATIONAL FLOW TYPES
# ============================================================================

class OperationalFlowParams(TypedDict, total=False):
    """Parameters for operational flow"""
    alignment: float
    separation: float
    dt: float
    tif: Tuple[float, float]
    resistance: float
    i1: float
    i2: float
    i3: float
    i4: float


@dataclass
class OperationalFlowResult:
    """Result of complete operational flow"""
    input_data: str
    star_engine_metrics: StarEngineMetrics
    final_status: Literal['RELEASED', 'REJECTED', 'REPENTANCE_TRIGGERED', 'QUARANTINED']
    timestamp: str
    repentance_logs: List[RepentanceLog]


# ============================================================================
# ALPHABET ENGINE TYPES
# ============================================================================

@dataclass
class VowelState:
    """State of a single vowel in Heart-5 system"""
    name: str
    vowel: Literal['A', 'E', 'I', 'O', 'U']
    value: float
    timestamp: int


@dataclass
class Heart5VowelSystem:
    """Complete Heart-5 vowel system state"""
    A: VowelState  # Initiation
    E: VowelState  # Discernment
    I: VowelState  # Identity
    O: VowelState  # Unity
    U: VowelState  # Binding


@dataclass
class SymbolicLogicResult:
    """Result of symbolic logic operation"""
    input_vector: List[float]
    operations: List[str]
    output_vector: List[float]
    heart_coherence: float
    timestamp: str


@dataclass
class AlphabetEngineStatus:
    """Status of Alphabet Engine"""
    version: str
    vowel_states: Heart5VowelSystem
    heart_coherence: float
    status: Literal['OPERATIONAL', 'DEGRADED', 'FAILED']


# ============================================================================
# ERROR TYPES
# ============================================================================

@dataclass
class StarEngineError(Exception):
    """Base error for Star Engine"""
    message: str
    error_type: str
    context: Dict[str, Any]


@dataclass
class CoherenceCalculationError(StarEngineError):
    """Error in coherence calculation"""
    pass


@dataclass
class DensityValidationError(StarEngineError):
    """Error in density validation"""
    pass


@dataclass
class RepentanceError(StarEngineError):
    """Error in repentance protocol"""
    pass


# ============================================================================
# API REQUEST/RESPONSE TYPES
# ============================================================================

class DynamicInvariantRequest(TypedDict):
    """Request for dynamic invariant calculation"""
    coherence_score: float


class DynamicInvariantResponse(TypedDict):
    """Response from dynamic invariant calculation"""
    invariant: float
    coherence_score: float
    mode: str
    timestamp: str


class DfruitDtRequest(TypedDict):
    """Request for dFruit/dt calculation"""
    alignment: float
    separation: float
    dt: float


class QCIRequest(TypedDict):
    """Request for QCI calculation"""
    tif: float
    resistance: float


class DensityRequest(TypedDict):
    """Request for density verification"""
    i1: float
    i2: float
    i3: float
    i4: float


class AnalysisRequest(TypedDict):
    """Request for complete analysis"""
    input_data: str
    params: OperationalFlowParams


class AnalysisResponse(TypedDict):
    """Response from complete analysis"""
    result: Dict[str, Any]
    repentance_logs: List[Dict[str, Any]]
    status: str
    timestamp: str


# ============================================================================
# MONITORING TYPES
# ============================================================================

@dataclass
class PerformanceMetric:
    """Performance metric for a function"""
    function_name: str
    duration_ms: float
    timestamp: str
    status: Literal['SUCCESS', 'FAILURE']


@dataclass
class SystemHealth:
    """Overall system health status"""
    star_engine: Literal['HEALTHY', 'DEGRADED', 'FAILED']
    alphabet_engine: Literal['HEALTHY', 'DEGRADED', 'FAILED']
    overall_status: Literal['OPERATIONAL', 'DEGRADED', 'CRITICAL']
    timestamp: str


@dataclass
class AnalyticsSnapshot:
    """Analytics snapshot of system activity"""
    total_analyses: int
    successful_releases: int
    repentance_triggers: int
    quarantines: int
    average_qci: float
    average_density: float
    timestamp: str


# ============================================================================
# CONFIGURATION TYPES
# ============================================================================

class ConfigDict(TypedDict, total=False):
    """Configuration dictionary"""
    harmony_ridge: float
    dynamic_invariant: float
    binary_break: float
    density_threshold: float
    covenant_multiplier: float
    qci_target: float
    qci_repentance_threshold: float
    eigenvalue_lambda_1: float
    eigenvalue_lambda_2: float
    log_level: str
    enable_performance_monitoring: bool
    enable_strict_validation: bool
    enable_repentance_auto_trigger: bool
    performance_log_threshold_ms: float
    repentance_trigger_threshold: float


# ============================================================================
# VALIDATION HELPERS
# ============================================================================

def validate_coherence_score(score: float) -> bool:
    """Validate coherence score is within bounds"""
    return 0.0 <= score <= 2.0


def validate_density(density: float, threshold: float) -> bool:
    """Validate density against threshold"""
    return density >= threshold


def validate_qci(qci: float, target: float = math.pi / 2) -> bool:
    """Validate QCI is approaching target"""
    return qci >= (math.pi / 4)  # At least π/4


def validate_operational_flow_params(params: OperationalFlowParams) -> bool:
    """Validate operational flow parameters"""
    required_keys = {'alignment', 'separation', 'dt', 'tif', 'resistance', 'i1', 'i2', 'i3', 'i4'}
    return all(key in params for key in required_keys)
