"""
Data for Barium hydroxide octahydrate (Ba(OH)2*8H2O).

Data primarily from 'Thermal Energy Storage' (Table 3.9)
Reference PDF: Thermal Energy Storage Methods, 3rd Ed. (Dinçer & Rosen, 2021)

T_m = 78 C (Melting temperature)
h_f = 265.7 kJ/kg (Latent heat of fusion )
k_s = 1.255 W/mK (Solid thermal conductivity)
k_l = 0.653 W/mK (Liquid thermal conductivity)
rho_s = 2070 kg/m^3 (Solid density)
rho_l = 1937 kg/m^3 (Liquid density)
"""

import numpy as np

_T_s = 77.0 + 273.15  # Solidification temperature (C a K)
_T_l = 79.0 + 273.15  # Liquid temperature (C a K)
_k_s = 1.255           # Solid thermal conductivity 
_k_l = 0.653           # Liquid thermal conductivity 
_h_f = 265700          # Latent heat of phase shift 
_cp = 2555             # Specific heat capacity 
_rho_avg = 2004        # Average density 
_rho_l = _rho_avg
_rho_s = _rho_avg

#Calculated enthalpy points
_h_s = _T_s * _cp      # Mass specific enthalpy at point of solidification
_h_l = _h_s + _h_f     # Mass specific enthalpy after phase shift

def h(T:float) -> float:
    """Mass specific enthalpy as function of temperature at 1 atm (fit assumes piecewise constant cp with phase change).

    Args:
        T (float): Temperature in K

    Returns:
        Specific enthalpy in J/kg
    """
    return np.piecewise(T, [T <= _T_s, (T > _T_s) & (T <= _T_l), T > _T_l], 
                        [lambda T: _cp*T, 
                         lambda T: _h_s + (T-_T_s)/(_T_l-_T_s)*_h_f, 
                         lambda T: _h_l + _cp*(T-_T_l)])

def T(h:float, p:float=None) -> float:
    """Temperature as function of mass specific enthalpy at 1 atm (fit assumes piecewise constant cp with phase change).

    Args:
        h (float): Specific enthalpy in J/kg
        p (float): Pressure in Pa

    Returns:
        Temperature in kelvin
    """
    return np.piecewise(h, [h <= _h_s, (h > _h_s) & (h <= _h_l), h > _h_l], 
                        [lambda h: 1/_cp*h, 
                         lambda h: _T_s + (_T_l-_T_s)*(h-_h_s)/(_h_l-_h_s), 
                         lambda h: _T_l + 1/_cp*(h-_h_l)])


def rho(h:float, p:float=None) -> float:
    """Density as function of mass specific enthalpy at 1 atm (fit assumes constant density).

    Args:
        h (float): Specific enthalpy in J/kg
        p (float): Pressure in Pa

    Returns:
        float: Density in kg/m^3
    """
    # Template uses a single constant density
    return _rho_avg * h**0

def k(h:float, p:float=None) -> float:
    """Thermal conductivity as function of mass specific enthalpy at 1 atm (fit assumes piecewise constant k).

    Args:
        h (float): Specific enthalpy in J/kg
        p (float): Pressure in Pa

    Returns:
        float: Thermal conductivity in W/(m K)
    """
    #Linearly interpolates conductivity across the mushy zone
    return np.piecewise(h, [h <= _h_s, (h > _h_s) & (h <= _h_l), h > _h_l], 
                        [_k_s, 
                         lambda h: _k_s + (_k_l-_k_s)/(_h_l-_h_s)*(h-_h_s), 
                         _k_l])

def cp(h:float, p:float=None) -> float:
    """Specific heat capacity as function of mass specific enthalpy at 1 atm (fit assumes constant cp).

    Args:
        h (float): Specific enthalpy in J/kg
        p (float): Pressure in Pa

    Returns:
        float: Specific heat capacity in J/(kg K)
    """
    #template uses a single constant cp
    return _cp * h**0