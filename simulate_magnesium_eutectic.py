import openterrace
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
from scipy.integrate import cumulative_trapezoid 

def main():
    
    #pcm
    pcm_name = "magnesium_eutectic" 
    #parámetros
    D = 0.3 
    H = 1.5  
    phi = 0.4  #porosidad
    R_inner = 0.01  
    R_outer = 0.03  
    n_fluid = 100  
    n_bed = 20  
    flow_rate = -0.01 
    h_value = 200 
    simulation_time = 4 * 3600  
    dt = 0.1 
    output_interval = 300 
    T_init = 273.15 + 80.0     #temperatura inicial del estanque y PCM a 80°C 
    T_cold = 273.15 + 20.0     #temperatura del agua fría de entrada a 20°C 
    cp_fluid = 4200 

    print(f"Iniciando simulación para: {pcm_name} ")

    ot = openterrace.Simulate(t_end=simulation_time, dt=dt)

    #definiendo fase fluida
    fluid = ot.create_phase(n=n_fluid, type='fluid')
    fluid.select_substance(substance='water')
    fluid.select_domain_shape(domain='cylinder_1d', D=D, H=H)
    fluid.select_porosity(phi=phi)
    fluid.select_schemes(diff='central_difference_1d', conv='upwind_1d')
    fluid.select_initial_conditions(T=T_init) 
    fluid.select_massflow(mdot=flow_rate)
    #condición de borde: Salida de agua caliente (zero gradient) en el nodo 0 (abajo)
    fluid.select_bc(bc_type='zero_gradient',
                    parameter='T',
                    position=(slice(None, None, None), 0))
    
    #condición de borde: Entrada de agua fría (fixed value) en el nodo -1 (arriba)
    fluid.select_bc(bc_type='fixed_value',
                    parameter='T',
                    position=(slice(None, None, None), -1),
                    value=T_cold)
    
    output_times = np.arange(0, simulation_time + output_interval, output_interval)
    fluid.select_output(times=output_times)

    #definiendo fase sólida pcm
    bed = ot.create_phase(n=n_bed, n_other=n_fluid, type='bed')
    bed.select_substance(pcm_name)
    bed.select_domain_shape(domain='hollow_sphere_1d', Rinner=R_inner, Router=R_outer)
    bed.select_schemes(diff='central_difference_1d')
    bed.select_initial_conditions(T=T_init)
    bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), 0))
    bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), -1))

    #acoplamiento pcm y fluido
    ot.select_coupling(fluid_phase=0, bed_phase=1, h_exp='constant', h_value=h_value)
    
    #simulacion
    ot.run_simulation()
    
    print(f" Simulación para {pcm_name} terminada. ")

    #resultados 
    print("Generando gráfico...")
    
    time_seconds = fluid.data.time 
    time_hours = time_seconds / 3600 
    outlet_temperature_C = fluid.data.T[:, 0, 0] - 273.15 
    
    #cálculo de Energía Liberada 
    power_from_tank = abs(flow_rate) * cp_fluid * (outlet_temperature_C - (T_cold - 273.15))
    energy_released = cumulative_trapezoid(power_from_tank, time_seconds, initial=0)[-1] / 1e6  
    
    print(f"Energía Total Liberada ({pcm_name}): {energy_released:.2f} MJ")

    #guardamos datos usando .npz para guardar múltiples arrays en un mismo archivo
    np.savez(f"results_{pcm_name}.npz", 
             energy=energy_released, 
             times=time_hours, 
             Tout=outlet_temperature_C)
    print(f"Resultados de datos guardados en results_{pcm_name}.npz")

    plt.figure(figsize=(10, 7))
    plt.plot(time_hours, outlet_temperature_C, label=pcm_name, linewidth=2)   
    plt.legend(title='Material PCM')
    plt.title(f'Simulación de Descarga: {pcm_name}', fontsize=16)
    plt.xlabel('Tiempo de Descarga (horas)', fontsize=12)
    plt.ylabel(u'Temperatura de Salida del Agua (°C)', fontsize=12)
    plt.grid(which='major', color='#DDDDDD', linewidth=1)
    plt.minorticks_on()
    plt.ylim(45,85) 
    
    plt.savefig(f'grafico_descarga_{pcm_name}.svg')
    print(f"Gráfico 'grafico_descarga_{pcm_name}.svg' guardado.")
    plt.show()

if __name__ == "__main__":
    main()