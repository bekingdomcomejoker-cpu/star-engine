import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core import StarEngine
import math

def test_math():
    engine = StarEngine()
    
    # Test Dynamic Invariant
    assert engine.get_dynamic_invariant(1.7) == 1.89
    assert engine.get_dynamic_invariant(1.6) == 1.67
    
    # Test dFruit/dt
    assert engine.calculate_dfruit_dt(10, 5, 2) == 2.5
    
    # Test TIF
    assert math.isclose(engine.calculate_tif(1.0, 0.8), 0.2)
    
    # Test QCI
    assert math.isclose(engine.calculate_qci(1, 1), math.pi/4)
    
    # Test Density
    is_valid, density = engine.verify_density(1.5, 1.5, 1.5, 1.0)
    assert is_valid == (density >= 3.34)
    
    print("All tests passed!")

if __name__ == "__main__":
    test_math()
