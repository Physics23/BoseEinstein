
import numpy as np
from io import BytesIO
import base64
from django.shortcuts import render
from .forms import BECParametersForm

# MUST be at top - before any matplotlib imports
import matplotlib
matplotlib.use('Agg')  # ← This prevents GUI window creation
import matplotlib.pyplot as plt

def simulate_bec(alpha, g, mu, L=20, N=1000):
    """Simulates BEC density and Bogoliubov excitations."""
    x = np.linspace(-L/2, L/2, N)
    
    # Thomas-Fermi density with smoothing
    density = np.maximum((mu - alpha * x) / g, 0)
    
    # Simple smoothing (no scipy needed)
    def simple_smooth(y, window_size=5):
        return np.convolve(y, np.ones(window_size)/window_size, mode='same')
    
    density_smooth = simple_smooth(density)
    psi = np.sqrt(density_smooth)
    
    # Bogoliubov excitations
    k = np.linspace(-5, 5, 200)
    n0 = np.max(psi)**2  # Peak density
    
    # Correct Bogoliubov dispersion
    E = np.sqrt(k**2 * (k**2 + 2 * g * n0)) + alpha * k
    
    return x, psi, k, E, n0

def simulator(request):
    if request.method == 'POST':
        form = BECParametersForm(request.POST)
        if form.is_valid():
            alpha = form.cleaned_data['alpha']
            g = form.cleaned_data['g']
            mu = form.cleaned_data['mu']
            
            try:
                # Run simulation
                x, psi, k, E, n0 = simulate_bec(alpha, g, mu)
                
                # Create figure
                fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
                
                # Plot 1: Wave function
                ax1.plot(x, np.real(psi), 'b-', label='Real(ψ)', linewidth=2)
                ax1.plot(x, np.imag(psi), 'r-', label='Imag(ψ)', linewidth=2)
                ax1.set_xlabel("Position (x)")
                ax1.set_ylabel("Wavefunction ψ(x)")
                ax1.set_title("BEC Wave Function")
                ax1.legend()
                ax1.grid(True, alpha=0.3)
                
                # Plot 2: Density profile
                ax2.plot(x, np.abs(psi)**2, 'g-', linewidth=2)
                ax2.fill_between(x, np.abs(psi)**2, alpha=0.3, color='green')
                ax2.set_xlabel("Position (x)")
                ax2.set_ylabel("Density |ψ(x)|²")
                ax2.set_title("BEC Density Profile")
                ax2.grid(True, alpha=0.3)
                
                # Plot 3: Bogoliubov spectrum
                ax3.plot(k, E, 'purple', linewidth=2, label='E(k)')
                ax3.axhline(0, color='gray', linestyle='--', alpha=0.5)
                ax3.axvline(0, color='gray', linestyle='--', alpha=0.5)
                ax3.set_xlabel("Momentum (k)")
                ax3.set_ylabel("Energy E(k)")
                ax3.set_title("Bogoliubov Excitation Spectrum")
                ax3.legend()
                ax3.grid(True, alpha=0.3)
                
                # Plot 4: Phase
                phase = np.angle(psi)
                ax4.plot(x, phase, 'orange', linewidth=2)
                ax4.set_xlabel("Position (x)")
                ax4.set_ylabel("Phase (radians)")
                ax4.set_title("Wave Function Phase")
                ax4.grid(True, alpha=0.3)
                
                plt.tight_layout()
                
                # Convert to HTML
                buffer = BytesIO()
                plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
                buffer.close()
                
                # Close plot to free memory
                plt.close(fig)
                
                return render(request, 'bose/results.html', {
                    'plot': image_base64,
                    'alpha': alpha,
                    'g': g,
                    'mu': mu,
                    'n0': f"{n0:.3f}",
                })
                
            except Exception as e:
                # Handle any errors gracefully
                return render(request, 'bose/error.html', {
                    'error': str(e),
                    'form': form
                })
    else:
        form = BECParametersForm()
    
    return render(request, 'bose/bose1.html', {'form': form})