import unittest
import numpy as np
from implementation.api.consciousness_field.phi_calculator import PhiActivationCalculator, ConsciousnessState
from implementation.api.consciousness_field.field_operator import ConsciousnessFieldOperator, DoubleSlitSimulator

class TestConsciousnessField(unittest.TestCase):
    
    def setUp(self):
        self.phi_calculator = PhiActivationCalculator()
        self.field_operator = ConsciousnessFieldOperator(lattice_size=16)
        self.slit_simulator = DoubleSlitSimulator()
    
    def test_phi_activation_calculation(self):
        """Test consciousness activation φ(S) calculation"""
        state = ConsciousnessState(
            learning_capacity=0.8,
            choice_capability=0.7,
            educational_participation=0.9,
            coherence_time=3.0e-3,
            timestamp=1234567890
        )
        
        result = self.phi_calculator.calculate_phi_activation(state)
        
        self.assertIn('phi_total', result)
        self.assertIn('activated', result)
        self.assertIn('components', result)
        self.assertIn('recommendations', result)
        
        self.assertGreaterEqual(result['phi_total'], 0.0)
        self.assertLessEqual(result['phi_total'], 1.0)
        
        # Check components
        components = result['components']
        self.assertIn('learning_capacity', components)
        self.assertIn('choice_capability', components)
        self.assertIn('educational_participation', components)
    
    def test_activation_threshold(self):
        """Test consciousness activation threshold"""
        # Subthreshold state
        subthreshold = ConsciousnessState(0.4, 0.3, 0.5, 1.0e-3, 1234567890)
        result_low = self.phi_calculator.calculate_phi_activation(subthreshold)
        self.assertFalse(result_low['activated'])
        
        # Suprathreshold state
        suprathreshold = ConsciousnessState(0.9, 0.8, 0.95, 5.0e-3, 1234567890)
        result_high = self.phi_calculator.calculate_phi_activation(suprathreshold)
        self.assertTrue(result_high['activated'])
    
    def test_field_operator_initialization(self):
        """Test field operator initialization"""
        self.assertIsNotNone(self.field_operator.creation_operator)
        self.assertIsNotNone(self.field_operator.annihilation_operator)
        self.assertIsNotNone(self.field_operator.actualization_operator)
        
        self.assertEqual(self.field_operator.creation_operator.shape, (16, 16))
        self.assertEqual(self.field_operator.actualization_operator.shape, (16, 16))
    
    def test_actualization_operator(self):
        """Test actualization operator"""
        potential_state = np.random.normal(0, 0.1, 16)
        context = {'phi_activation': 0.85, 'coherence_level': 0.9}
        
        manifested = self.field_operator.apply_actualization_operator(
            potential_state, context
        )
        
        self.assertEqual(manifested.shape, (16,))
        
        # High activation should reduce noise
        low_context = {'phi_activation': 0.3, 'coherence_level': 0.4}
        manifested_low = self.field_operator.apply_actualization_operator(
            potential_state, low_context
        )
        
        # Check that high activation gives clearer actualization
        noise_high = np.std(manifested - potential_state)
        noise_low = np.std(manifested_low - potential_state)
        self.assertLess(noise_high, noise_low)
    
    def test_field_equation_solution(self):
        """Test field equation solution"""
        initial_phi = np.zeros(16)
        initial_phi[7:9] = 1.0  # Localized initial state
        J_actualization = np.random.normal(0, 0.01, 16)
        
        solution = self.field_operator.solve_field_equation(
            initial_phi, J_actualization, time_steps=100
        )
        
        self.assertIn('final_field', solution)
        self.assertIn('field_history', solution)
        self.assertIn('energy_history', solution)
        self.assertIn('quantum_properties', solution)
        
        self.assertEqual(len(solution['field_history']), 1)  # 100 steps saving every 100
        self.assertGreater(solution['energy_history'][0], 0)
    
    def test_double_slit_simulation(self):
        """Test double-slit experiment simulation"""
        consciousness_states = [
            {'phi_activation': 0.3, 'coherence_level': 0.4, 'description': 'Low'},
            {'phi_activation': 0.9, 'coherence_level': 0.9, 'description': 'High'}
        ]
        
        results = self.slit_simulator.simulate_experiment(consciousness_states)
        
        self.assertIn('experiment_results', results)
        self.assertIn('consciousness_correlation', results)
        self.assertIn('predicted_values', results)
        
        self.assertEqual(len(results['experiment_results']), 2)
        
        # Check predicted values
        predicted = results['predicted_values']
        self.assertAlmostEqual(predicted['fringe_spacing'], 8.3e-6)
        self.assertAlmostEqual(predicted['decoherence_time'], 3.2e-3)
        
        # Check consciousness-quantum effects correlation
        correlation = results['consciousness_correlation']
        self.assertIn('visibility_correlation', correlation)
        self.assertIn('which_path_correlation', correlation)
    
    def test_quantum_properties_analysis(self):
        """Test quantum properties analysis"""
        test_field = np.random.normal(0, 1.0, 32)
        properties = self.field_operator.analyze_quantum_properties(test_field)
        
        self.assertIn('power_spectrum', properties)
        self.assertIn('coherence_length', properties)
        self.assertIn('quantum_fluctuations', properties)
        self.assertIn('energy_levels', properties)
        self.assertIn('decoherence_time', properties)
        
        self.assertGreater(properties['coherence_length'], 0)
        self.assertGreater(properties['decoherence_time'], 0)
        self.assertEqual(len(properties['energy_levels']), 5)

if __name__ == '__main__':
    unittest.main()
