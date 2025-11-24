"""
Educational Manifold API for Ontologica
Implementation of 𝔼 = (M, g, ∇) educational space geometry
"""

from .geodesic_navigator import (
    EducationalManifold,
    LearningState,
    LearningPathVisualizer,
    demonstrate_educational_navigation
)

__all__ = [
    'EducationalManifold',
    'LearningState', 
    'LearningPathVisualizer',
    'demonstrate_educational_navigation'
]

__version__ = "1.0.0"
