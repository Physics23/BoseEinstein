
# BEC Quantum Simulator 🌌

A Django web application for simulating Bose-Einstein Condensates and visualizing Bogoliubov-de Gennes equations.

## 🚀 Live Demo

[![Heroku Deployment](https://img.shields.io/badge/Heroku-Live_Demo-430098?style=for-the-badge&logo=heroku)](https://your-bec-simulator.herokuapp.com)

## ✨ Features

- **Interactive BEC Density Profiles** - Visualize condensate wavefunctions
- **Bogoliubov Excitation Spectrum** - Plot quantum quasiparticle energies
- **Real-time Parameter Adjustment** - Sliders for physical parameters
- **Beautiful Bootstrap UI** - Modern, responsive design
- **Heroku Ready** - One-click deployment

## 🛠️ Technologies Used

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-11557C?style=flat&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?style=flat&logo=numpy)

## 📦 Installation

### Prerequisites
- Python 3.9+
- pip package manager
- Git

### Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/bec-simulator.git
cd bec-simulator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver