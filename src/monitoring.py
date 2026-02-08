"""
Performance monitoring for Star Engine
Automatic tracking of function execution time and resource usage
"""

import time
from functools import wraps
from typing import Callable, Any, Dict
from logging_module import get_logger


def monitor_performance(func: Callable) -> Callable:
    """
    Decorator to monitor function performance
    Logs execution time, memory usage, and any exceptions
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        logger = get_logger()
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            duration_ms = (time.time() - start_time) * 1000
            
            # Log performance
            logger.log_calculation(
                func.__name__,
                {
                    'args_count': len(args),
                    'kwargs_keys': list(kwargs.keys())
                },
                result,
                duration_ms
            )
            
            return result
        
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.log_error(
                'calculation_error',
                str(e),
                {
                    'function': func.__name__,
                    'duration_ms': round(duration_ms, 2),
                    'error_type': type(e).__name__
                }
            )
            raise
    
    return wrapper


def monitor_repentance(func: Callable) -> Callable:
    """
    Decorator specifically for repentance protocol monitoring
    Tracks QCI improvement and step execution
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        logger = get_logger()
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            duration_ms = (time.time() - start_time) * 1000
            
            # Log repentance if result contains QCI data
            if isinstance(result, dict) and 'qci_after' in result:
                logger.log_repentance(
                    result.get('expose', 'Unknown'),
                    result.get('qci_before', 0),
                    result.get('qci_after', 0),
                    duration_ms,
                    {
                        'expose': result.get('expose') is not None,
                        'recompile': result.get('recompile') is not None,
                        'purge': result.get('purge', False),
                        'reset': result.get('reset', False)
                    }
                )
            
            return result
        
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.log_error(
                'repentance_error',
                str(e),
                {
                    'function': func.__name__,
                    'duration_ms': round(duration_ms, 2),
                    'error_type': type(e).__name__
                }
            )
            raise
    
    return wrapper


def monitor_operational_flow(func: Callable) -> Callable:
    """
    Decorator for operational flow monitoring
    Tracks complete analysis pipeline
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        logger = get_logger()
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            duration_ms = (time.time() - start_time) * 1000
            
            # Extract metrics if available
            metrics = {}
            if isinstance(result, tuple) and len(result) > 0:
                if isinstance(result[0], dict):
                    metrics = result[0]
            elif isinstance(result, dict):
                metrics = result
            
            # Log operational flow
            input_data = str(args[1]) if len(args) > 1 else "unknown"
            status = metrics.get('status', 'UNKNOWN')
            
            logger.log_operational_flow(
                input_data,
                status,
                metrics,
                duration_ms
            )
            
            return result
        
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.log_error(
                'operational_flow_error',
                str(e),
                {
                    'function': func.__name__,
                    'duration_ms': round(duration_ms, 2),
                    'error_type': type(e).__name__
                }
            )
            raise
    
    return wrapper


class PerformanceTracker:
    """Track and aggregate performance metrics"""
    
    def __init__(self):
        self.metrics: Dict[str, list] = {}
    
    def record(self, function_name: str, duration_ms: float):
        """Record a function execution"""
        if function_name not in self.metrics:
            self.metrics[function_name] = []
        self.metrics[function_name].append(duration_ms)
    
    def get_stats(self, function_name: str) -> Dict[str, float]:
        """Get statistics for a function"""
        if function_name not in self.metrics:
            return {}
        
        durations = self.metrics[function_name]
        return {
            'count': len(durations),
            'total_ms': sum(durations),
            'average_ms': sum(durations) / len(durations),
            'min_ms': min(durations),
            'max_ms': max(durations)
        }
    
    def get_all_stats(self) -> Dict[str, Dict[str, float]]:
        """Get statistics for all functions"""
        return {
            func: self.get_stats(func)
            for func in self.metrics.keys()
        }
    
    def reset(self):
        """Reset all metrics"""
        self.metrics = {}


# Global performance tracker
_tracker = PerformanceTracker()


def get_tracker() -> PerformanceTracker:
    """Get global performance tracker"""
    return _tracker
