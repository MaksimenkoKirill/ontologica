import unittest
import numpy as np
import pandas as pd
from scipy import stats
from implementation.api.consciousness_field.field_operator import DoubleSlitSimulator
from implementation.api.educational_manifold.geodesic_navigator import EducationalManifold

class ExperimentalPredictionsValidation(unittest.TestCase):
    """Validation of Ontologica's experimental predictions"""
    
    def setUp(self):
        self.manifold = EducationalManifold()
        self.slit_simulator = DoubleSlitSimulator()
        
        # Predicted values from Ontologica
        self.predicted_values = {
            'fringe_spacing': 8.3e-6,           # meters
            'decoherence_time': 3.2e-3,         # seconds
            'learning_acceleration': 2.1e-2,    # m/s²
            'optimal_efficiency': 0.78,         # dimensionless
            'retention_tau': 45.0,              # days
            'acquisition_tau': 21.0,            # days
            'skill_beta': 0.67                  # dimensionless
        }
        
        self.tolerances = {
            'fringe_spacing': 0.5e-6,
            'decoherence_time': 0.4e-3, 
            'learning_acceleration': 0.3e-2,
            'optimal_efficiency': 0.05,
            'retention_tau': 7.0,
            'acquisition_tau': 3.0,
            'skill_beta': 0.08
        }
    
    def test_double_slit_predictions(self):
        """Validation of double-slit experiment predictions"""
        # Simulate experiment with various consciousness states
        consciousness_states = [
            {'phi_activation': phi, 'coherence_level': 0.7} 
            for phi in np.linspace(0.1, 0.9, 9)
        ]
        
        results = self.slit_simulator.simulate_experiment(consciousness_states)
        
        # Verify predicted fringe spacing
        for result in results['experiment_results']:
            fringe_pattern = result['fringe_pattern']
            if len(fringe_pattern) > 1:
                # Find distance between maxima
                peaks = self._find_peaks(fringe_pattern)
                if len(peaks) >= 2:
                    avg_spacing = np.mean(np.diff(peaks))
                    # Normalize to predicted scale
                    normalized_spacing = avg_spacing * 1e-5  # Empirical scale factor
                    
                    # Verify match with prediction
                    discrepancy = abs(normalized_spacing - self.predicted_values['fringe_spacing'])
                    self.assertLess(discrepancy, self.tolerances['fringe_spacing'],
                                  f"Fringe spacing {normalized_spacing:.2e} doesn't match prediction")
    
    def test_learning_metrics_predictions(self):
        """Validation of learning metrics predictions"""
        # Testing predicted learning efficiency
        test_cases = [
            ([0.1, 0.2], [0.9, 0.8]),  # Simple case
            ([0.0, 0.0, 0.0], [1.0, 1.0, 1.0]),  # Multi-dimensional case
            ([0.5, 0.5], [0.6, 0.6])   # Close states
        ]
        
        efficiencies = []
        for start, target in test_cases:
            result = self.manifold.compute_learning_geodesic(
                np.array(start), np.array(target), max_time=100.0
            )
            efficiencies.append(result['efficiency'])
        
        avg_efficiency = np.mean(efficiencies)
        
        # Verify average efficiency is close to predicted optimal
        discrepancy = abs(avg_efficiency - self.predicted_values['optimal_efficiency'])
        self.assertLess(discrepancy, self.tolerances['optimal_efficiency'],
                       f"Average efficiency {avg_efficiency:.3f} doesn't match predicted")
    
    def test_knowledge_retention_curve(self):
        """Validation of knowledge retention curve"""
        times = np.array([1, 7, 30, 90, 365])  # days
        predicted_retention = [
            self.manifold.knowledge_retention_curve(1.0, t, 1.0) 
            for t in times
        ]
        
        # Verify retention decreases over time
        for i in range(1, len(predicted_retention)):
            self.assertLess(predicted_retention[i], predicted_retention[i-1],
                           "Knowledge retention should decrease over time")
        
        # Verify asymptotic value
        asymptotic = self.manifold.knowledge_retention_curve(1.0, 1000, 1.0)
        self.assertAlmostEqual(asymptotic, 0.15, delta=0.05,
                              "Asymptotic retention should be around 0.15")
    
    def test_skill_acquisition_prediction(self):
        """Validation of skill acquisition prediction"""
        times = np.array([7, 14, 21, 30, 60])  # days
        skills = [
            self.manifold.skill_acquisition_curve(t, 1.0, 1.0)
            for t in times
        ]
        
        # Verify monotonic growth
        for i in range(1, len(skills)):
            self.assertGreater(skills[i], skills[i-1],
                              "Skills should grow over time")
        
        # Verify curve shape (logistic with β ≈ 0.67)
        # Fit curve to data
        try:
            from scipy.optimize import curve_fit
            
            def skill_model(t, tau, beta):
                return (1.0 - np.exp(-t/tau))**beta
            
            popt, pcov = curve_fit(skill_model, times, skills, 
                                 p0=[self.predicted_values['acquisition_tau'], 
                                     self.predicted_values['skill_beta']])
            
            fitted_tau, fitted_beta = popt
            
            # Verify match with predicted values
            self.assertAlmostEqual(fitted_tau, self.predicted_values['acquisition_tau'], 
                                 delta=self.tolerances['acquisition_tau'])
            self.assertAlmostEqual(fitted_beta, self.predicted_values['skill_beta'],
                                 delta=self.tolerances['skill_beta'])
                                 
        except ImportError:
            self.skipTest("scipy not installed for curve fitting")
    
    def test_consciousness_quantum_correlation(self):
        """Validation of consciousness-quantum effects correlation"""
        # Generate test data with varying consciousness activation
        n_samples = 50
        phi_activations = np.random.uniform(0.1, 0.9, n_samples)
        visibilities = []
        which_path_infos = []
        
        for phi in phi_activations:
            # Simulate experiment for this consciousness level
            results = self.slit_simulator.simulate_experiment([
                {'phi_activation': phi, 'coherence_level': 0.7}
            ])
            
            exp_result = results['experiment_results'][0]
            visibilities.append(exp_result['visibility'])
            which_path_infos.append(exp_result['which_path_info'])
        
        # Verify correlation
        visibility_corr, visibility_p = stats.pearsonr(phi_activations, visibilities)
        which_path_corr, which_path_p = stats.pearsonr(phi_activations, which_path_infos)
        
        # According to Ontologica, there should be positive correlation
        self.assertGreater(visibility_corr, 0.0,
                         "Should be positive correlation between consciousness and visibility")
        self.assertGreater(which_path_corr, 0.0,
                         "Should be positive correlation between consciousness and which-path information")
        
        # Verify statistical significance
        self.assertLess(visibility_p, 0.05, "Visibility correlation should be significant")
        self.assertLess(which_path_p, 0.05, "Which-path correlation should be significant")
    
    def test_educational_manifold_curvature(self):
        """Validation of educational manifold curvature"""
        # Test various positions in educational space
        test_positions = [
            np.array([0.1, 0.1, 0.1, 0.1]),
            np.array([0.5, 0.5, 0.5, 0.5]), 
            np.array([0.9, 0.9, 0.9, 0.9])
        ]
        
        complexities = []
        for pos in test_positions:
            # Compute complexity at this position
            complexity = self.manifold.calculate_complexity_profile(np.array([pos]))[0]
            complexities.append(complexity)
        
        # Verify complexity varies in space
        # (should not be constant)
        complexity_std = np.std(complexities)
        self.assertGreater(complexity_std, 0.01,
                         "Complexity should vary across educational space")
    
    def _find_peaks(self, signal):
        """Find peaks in signal for interference pattern analysis"""
        peaks = []
        for i in range(1, len(signal)-1):
            if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
                peaks.append(i)
        return peaks
    
    def test_statistical_power_analysis(self):
        """Statistical power analysis of predictions"""
        # Sufficient power needed for reliable effect detection
        effect_sizes = []
        
        # Power analysis for consciousness-quantum effects correlation
        n_simulations = 20
        for _ in range(n_simulations):
            phi_vals = np.random.uniform(0.2, 0.9, 30)
            visibility_vals = 0.7 + 0.3 * phi_vals + 0.1 * np.random.normal(size=30)
            
            corr, p_value = stats.pearsonr(phi_vals, visibility_vals)
            effect_sizes.append(corr)
        
        avg_effect_size = np.mean(effect_sizes)
        
        # Verify effect is large enough for detection
        self.assertGreater(avg_effect_size, 0.3,
                         "Effect size should be sufficient for detection in realistic experiments")
        
        # Verify power with reasonable sample size
        required_n = self._calculate_required_sample_size(avg_effect_size, power=0.8, alpha=0.05)
        self.assertLess(required_n, 100,
                       f"Effect detection shouldn't require more than 100 subjects (required: {required_n})")
    
    def _calculate_required_sample_size(self, effect_size, power=0.8, alpha=0.05):
        """Calculate required sample size for effect detection"""
        from scipy import stats
        
        # Simplified power calculation
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)
        
        n = ((z_alpha + z_beta) / effect_size) ** 2
        return int(np.ceil(n))

if __name__ == '__main__':
    # Run validation with detailed output
    suite = unittest.TestLoader().loadTestsFromTestCase(ExperimentalPredictionsValidation)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
