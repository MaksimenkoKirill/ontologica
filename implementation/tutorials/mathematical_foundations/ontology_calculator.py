import sympy as sp
import numpy as np
from IPython.display import display, Math

class OntologyMathematicsTutorial:
    """Interactive tutorial for Ontologica mathematical foundations"""
    
    def __init__(self):
        self.setup_symbols()
    
    def setup_symbols(self):
        """Setup mathematical symbols"""
        # Consciousness field
        self.phi = sp.Function('phi')(sp.Symbol('t'))
        self.m = sp.Symbol('m', positive=True)  # consciousness mass
        self.lambda_sym = sp.Symbol('lambda', positive=True)  # coupling constant
        
        # Educational manifold
        self.g = sp.Function('g')  # metric tensor
        self.G = sp.Function('G')  # Einstein tensor
        self.T = sp.Function('T')  # consciousness stress-energy tensor
    
    def demonstrate_field_equation(self):
        """Demonstrate consciousness field equation"""
        print("=== Consciousness Field Activation Equation ===")
        print("(□ + m²)φ = J + λ|φ|²φ")
        print()
        
        # Symbolic representation
        d_alembertian = sp.symbols('Box')  # d'Alembert operator
        J = sp.Function('J')  # Actualization current
        
        equation = sp.Eq(d_alembertian * self.phi + self.m**2 * self.phi, 
                        J(sp.Symbol('t')) + self.lambda_sym * sp.Abs(self.phi)**2 * self.phi)
        
        display(Math(sp.latex(equation)))
        
        explanation = """
        Where:
        - □ = d'Alembertian in educational spacetime
        - m = consciousness activation mass parameter  
        - φ = consciousness field operator
        - J = actualization current density
        - λ = self-interaction coupling constant
        
        This equation describes how potentials (¬C) actualize 
        into manifested reality (C) through conscious interaction.
        """
        print(explanation)
    
    def demonstrate_primordial_equation(self):
        """Demonstrate primordial equation 0 = (-) + (+)"""
        print("=== Primordial Equation ===")
        print("0 = (-) + (+)")
        print()
        
        negative = sp.Symbol('(-)')  # Infinite creative potential
        positive = sp.Symbol('(+)')  # Actualized conscious relationships
        
        primordial_eq = sp.Eq(0, negative + positive)
        display(Math(sp.latex(primordial_eq)))
        
        explanation = """
        This is the fundamental balance equation:
        
        (-) = Infinite creative potential of Absolute
              (not "nothingness" but plenum of all possibility)
              
        (+) = Actualized conscious relationships 
              in manifested realms
              
        0 = Perfect balance in each unique expression
        
        The equation represents the eternal creative balance of Absolute,
        where every expression maintains perfect balance.
        """
        print(explanation)
    
    def calculate_consciousness_activation(self, learning_capacity: float, 
                                         choice_capability: float,
                                         educational_participation: float) -> Dict:
        """Calculate consciousness activation using φ(S) formula"""
        phi_total = learning_capacity * choice_capability * educational_participation
        activated = phi_total >= 0.8
        
        return {
            'phi_total': phi_total,
            'activated': activated,
            'components': {
                'learning_capacity': learning_capacity,
                'choice_capability': choice_capability, 
                'educational_participation': educational_participation
            },
            'interpretation': self._interpret_activation(phi_total, activated)
        }
    
    def _interpret_activation(self, phi_total: float, activated: bool) -> str:
        """Interpret activation results"""
        if not activated:
            if phi_total < 0.3:
                return "Focus on foundational learning capacity development"
            elif phi_total < 0.6:
                return "Develop complex choice-making and decision capabilities"
            else:
                return "Deepen engagement with cosmic educational curriculum"
        else:
            return "Ready for advanced mutual determination and creative partnership"

# Example tutorial session
def run_ontology_tutorial():
    tutorial = OntologyMathematicsTutorial()
    
    print("ONTOLOGICA MATHEMATICS TUTORIAL")
    print("=" * 50)
    
    # Demonstrate field equations
    tutorial.demonstrate_field_equation()
    print("\n" + "="*50 + "\n")
    
    # Demonstrate primordial equation
    tutorial.demonstrate_primordial_equation()
    print("\n" + "="*50 + "\n")
    
    # Calculate example activation
    result = tutorial.calculate_consciousness_activation(
        learning_capacity=0.75,
        choice_capability=0.82,
        educational_participation=0.88
    )
    
    print("Consciousness Activation Calculation:")
    print(f"φ(S): {result['phi_total']:.3f}")
    print(f"Activated: {result['activated']}")
    print(f"Interpretation: {result['interpretation']}")

if __name__ == "__main__":
    run_ontology_tutorial()
