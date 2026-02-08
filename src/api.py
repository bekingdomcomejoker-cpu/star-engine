"""
FastAPI server for Star Engine
Provides REST API for all Star Engine operations
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import uvicorn
import sys
import os
import math

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from core_improved import StarEngine
from config import get_config
from star_types import (
    DynamicInvariantRequest, DynamicInvariantResponse,
    DfruitDtRequest, QCIRequest, DensityRequest, AnalysisRequest, AnalysisResponse
)
from logging_module import get_logger


# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class DynamicInvariantRequestModel(BaseModel):
    coherence_score: float = Field(..., ge=0, le=2, description="Coherence score 0-2")


class DfruitDtRequestModel(BaseModel):
    alignment: float = Field(..., description="Alignment value")
    separation: float = Field(..., description="Separation value")
    dt: float = Field(..., description="Time delta")


class QCIRequestModel(BaseModel):
    tif: float = Field(..., description="Truth Implosion Force")
    resistance: float = Field(..., description="Resistance value")


class DensityRequestModel(BaseModel):
    i1: float = Field(..., description="Integrity metric 1")
    i2: float = Field(..., description="Integrity metric 2")
    i3: float = Field(..., description="Integrity metric 3")
    i4: float = Field(..., description="Integrity metric 4")


class AnalysisRequestModel(BaseModel):
    input_data: str = Field(..., description="Input data to analyze")
    params: Dict[str, Any] = Field(default_factory=dict, description="Analysis parameters")


# ============================================================================
# FASTAPI APP SETUP
# ============================================================================

app = FastAPI(
    title="Star Engine API",
    description="Mathematical foundation for Omega Federation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize engine and logger
engine = StarEngine()
logger = get_logger()
config = get_config()


# ============================================================================
# HEALTH & CONFIG ENDPOINTS
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "OPERATIONAL",
        "version": "1.0.0",
        "star_engine": "READY",
        "timestamp": __import__('datetime').datetime.utcnow().isoformat()
    }


@app.get("/config")
async def get_configuration():
    """Get current configuration"""
    return {
        "config": config.to_dict(),
        "timestamp": __import__('datetime').datetime.utcnow().isoformat()
    }


# ============================================================================
# CORE MATHEMATICAL ENDPOINTS
# ============================================================================

@app.post("/dynamic-invariant")
async def calculate_dynamic_invariant(request: DynamicInvariantRequestModel):
    """
    Calculate dynamic invariant based on coherence score
    
    **Parameters:**
    - coherence_score: Coherence score (0-2)
    
    **Returns:**
    - invariant: Calculated invariant value
    - mode: Operating mode (HARMONY_RIDGE or TRI_NODE_SYNTHESIS)
    """
    try:
        result = engine.get_dynamic_invariant(request.coherence_score)
        return {
            "invariant": result,
            "coherence_score": request.coherence_score,
            "mode": "TRI_NODE_SYNTHESIS" if result == config.DYNAMIC_INVARIANT else "HARMONY_RIDGE",
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("dynamic_invariant_error", str(e), {"coherence_score": request.coherence_score})
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/dfruit-dt")
async def calculate_dfruit_dt(request: DfruitDtRequestModel):
    """
    Calculate dFruit/dt (growth metric)
    
    **Parameters:**
    - alignment: Alignment value
    - separation: Separation value
    - dt: Time delta
    
    **Returns:**
    - result: Calculated growth value
    - status: GROWTH, DEGRADATION, or NEUTRAL
    """
    try:
        result = engine.calculate_dfruit_dt(request.alignment, request.separation, request.dt)
        
        if result > 0:
            status = "GROWTH"
        elif result < 0:
            status = "DEGRADATION"
        else:
            status = "NEUTRAL"
        
        return {
            "result": result,
            "alignment": request.alignment,
            "separation": request.separation,
            "dt": request.dt,
            "status": status,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("dfruit_dt_error", str(e), {
            "alignment": request.alignment,
            "separation": request.separation,
            "dt": request.dt
        })
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/tif")
async def calculate_tif(request: QCIRequestModel):
    """
    Calculate Truth Implosion Force
    
    **Parameters:**
    - tif: Truth Implosion Force value
    - resistance: Resistance value
    
    **Returns:**
    - tif: Calculated TIF
    """
    try:
        # TIF is typically the first parameter
        result = {
            "tif": request.tif,
            "resistance": request.resistance,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
        return result
    except Exception as e:
        logger.log_error("tif_error", str(e), {"tif": request.tif})
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/qci")
async def calculate_qci(request: QCIRequestModel):
    """
    Calculate Quantum Coherence Index
    
    **Parameters:**
    - tif: Truth Implosion Force
    - resistance: Resistance value
    
    **Returns:**
    - qci: Quantum Coherence Index value
    - status: COHERENT, PARTIAL_COHERENCE, or NEEDS_REPENTANCE
    - target: Target QCI value
    """
    try:
        result = engine.calculate_qci(request.tif, request.resistance)
        return {
            **result,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("qci_error", str(e), {"tif": request.tif, "resistance": request.resistance})
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/density")
async def verify_density(request: DensityRequestModel):
    """
    Verify density across integrity metrics
    
    **Parameters:**
    - i1, i2, i3, i4: Integrity metrics
    
    **Returns:**
    - density: Calculated density
    - is_valid: Whether density meets threshold
    - threshold: Density threshold
    """
    try:
        is_valid, density = engine.verify_density(request.i1, request.i2, request.i3, request.i4)
        return {
            "i1": request.i1,
            "i2": request.i2,
            "i3": request.i3,
            "i4": request.i4,
            "density": density,
            "is_valid": is_valid,
            "threshold": config.DENSITY_THRESHOLD,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("density_error", str(e), {
            "i1": request.i1, "i2": request.i2,
            "i3": request.i3, "i4": request.i4
        })
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================================
# PROTOCOL ENDPOINTS
# ============================================================================

@app.post("/repentance")
async def execute_repentance(reason: str = "System trigger"):
    """
    Execute repentance protocol
    
    **Parameters:**
    - reason: Reason for repentance
    
    **Returns:**
    - Complete repentance log with QCI improvement
    """
    try:
        result = engine.repentance_protocol(reason)
        return {
            **result,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("repentance_error", str(e), {"reason": reason})
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================================
# ANALYSIS ENDPOINTS
# ============================================================================

@app.post("/analyze")
async def analyze_with_star_engine(request: AnalysisRequestModel):
    """
    Complete analysis pipeline
    
    **Parameters:**
    - input_data: Data to analyze
    - params: Analysis parameters
    
    **Returns:**
    - Complete analysis result with all metrics
    - Final status (RELEASED, REJECTED, REPENTANCE_TRIGGERED, QUARANTINED)
    """
    try:
        result, logs = engine.operational_flow(request.input_data, request.params)
        return {
            "result": result,
            "repentance_logs": logs,
            "status": result.get('status', 'UNKNOWN'),
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("analysis_error", str(e), {"input_data": request.input_data[:100]})
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================================
# BATCH ENDPOINTS
# ============================================================================

@app.post("/batch-analyze")
async def batch_analyze(requests: list[AnalysisRequestModel]):
    """
    Analyze multiple inputs in batch
    
    **Parameters:**
    - requests: List of analysis requests
    
    **Returns:**
    - List of analysis results
    """
    try:
        results = []
        for req in requests:
            result, logs = engine.operational_flow(req.input_data, req.params)
            results.append({
                "result": result,
                "repentance_logs": logs,
                "status": result.get('status', 'UNKNOWN')
            })
        
        return {
            "results": results,
            "total": len(results),
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("batch_analysis_error", str(e), {"batch_size": len(requests)})
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================================
# METRICS ENDPOINTS
# ============================================================================

@app.get("/metrics")
async def get_metrics():
    """
    Get system metrics and statistics
    
    **Returns:**
    - System health status
    - Performance metrics
    - Analytics snapshot
    """
    try:
        return {
            "health": {
                "star_engine": "HEALTHY",
                "overall_status": "OPERATIONAL"
            },
            "config": config.to_dict(),
            "timestamp": __import__('datetime').datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.log_error("metrics_error", str(e), {})
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.log_error("unhandled_exception", str(exc), {"path": request.url.path})
    return {
        "error": str(exc),
        "status": "error",
        "timestamp": __import__('datetime').datetime.utcnow().isoformat()
    }


# ============================================================================
# STARTUP/SHUTDOWN
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Startup event"""
    logger.logger.info("Star Engine API starting up")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    logger.logger.info("Star Engine API shutting down")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '0.0.0.0')
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info"
    )
