"""
Datasets module for Ontologica experimental data
Standardized data formats for consciousness research
"""

from .quantum_consciousness.experiment_recorder import (
    QuantumConsciousnessExperiment,
    demonstrate_experiment_recording
)

from .learning_geodesics.learning_trajectory_recorder import (
    LearningTrajectoryRecorder,
    LearningTrajectory,
    demonstrate_learning_trajectory_recording
)

from .relationship_networks.network_analyzer import (
    RelationshipNetworkAnalyzer,
    RelationshipNetwork,
    demonstrate_network_analysis
)

__all__ = [
    # Quantum consciousness experiments
    'QuantumConsciousnessExperiment',
    'demonstrate_experiment_recording',
    
    # Learning trajectories  
    'LearningTrajectoryRecorder',
    'LearningTrajectory',
    'demonstrate_learning_trajectory_recording',
    
    # Relationship networks
    'RelationshipNetworkAnalyzer', 
    'RelationshipNetwork',
    'demonstrate_network_analysis'
]

__version__ = "1.0.0"
