"""
Data for Magnesium nitrate hexahydrate (Mg(NO3)2*6H2O).

Data primarily from 'Thermal Energy' (Table 3.9)
Reference: Thermal Energy Storage Methods, 3rd Ed. (Dinçer & Rosen, 2021)

T_m = 89 C (Melting temperature)
h_f = 162.8 kJ/kg (Latent heat of fusion)
k_s = 0.611 W/mK (Solid thermal conductivity )
k_l = 0.490 W/mK (Liquid thermal conductivity)
rho_s = 1636 kg/m^3 (Solid density)
rho_l = 1550 kg/m^3 (Liquid density)

OpenTerrace model (following ATS58.py como template):
- 2-degree melting range is assumed (88 C to 90 C).
- single average density is used: (1636+1550)/2 = 1593 kg/m^3.
"""

import numpy as np

_T_s = 88.0 + 273.15  #Solidification temperature (C a K)
_T_l = 90.0 + 273.15  #Liquid temperature (C a K)
_k_s = 0.611           #Solid thermal conductivity (W/mK)
_k_l = 0.490           #Liquid thermal conductivity (W/mK)
_h_f = 162800          #Latent heat of phase shift (J/kg)
_cp = 2165             #Specific heat capacity (J/kg*K) 
_rho_avg = 1593        #density (kg/m^3)
_rho_l = _rho_avg
_rho_s = _rho_avg

# Calculated enthalpy points
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
    # Linearly interpolates conductivity across the mushy zone
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
    # Template uses a single constant cp
    return _cp * h**0