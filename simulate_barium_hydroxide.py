import openterrace
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg') 
import numpy as np
from scipy.integrate import cumulative_trapezoid

def main():

    #pcm
    pcm_name = "barium_hydroxide_octahydrate" 
    #Parámetros de la simulación
    D = 0.3  
    H = 1.5  
    phi = 0.4  
    R_inner = 0.01  #radio interno del pcm
    R_outer = 0.03  #radio externo del pcm
    n_fluid = 100  #n° de nodos del fluido
    n_bed = 20  #n° de nodos pcm
    flow_rate = -0.01 #flujo hacia abajo
    h_value = 200 
    simulation_time = 4 * 3600  #4 horas
    dt = 0.1 #paso del tiempo
    output_interval = 300 
    T_init = 273.15 + 80.0 #temperatura inicial del estanque y PCM a 80°C 
    T_cold = 273.15 + 20.0 #temperatura del agua fría de entrada a 20°C 
    cp_fluid = 4200 #cp del agua
    print(f" Iniciando simulación para: {pcm_name} ")
    ot = openterrace.Simulate(t_end=simulation_time, dt=dt)

    # definiendo la fase Fluida (en este caso:Agua)
    fluid = ot.create_phase(n=n_fluid, type='fluid')
    fluid.select_substance(substance='water')
    fluid.select_domain_shape(domain='cylinder_1d', D=D, H=H) #dominio: cilindro vertical
    fluid.select_porosity(phi=phi)
    fluid.select_schemes(diff='central_difference_1d', conv='upwind_1d') #discretización
    fluid.select_initial_conditions(T=T_init) #condición inicial
    fluid.select_massflow(mdot=flow_rate) #flujo hacia abajo
    #Condición de Borde: salida de agua caliente en el nodo 0 (abajo)
    fluid.select_bc(bc_type='zero_gradient',
                    parameter='T',
                    position=(slice(None, None, None), 0))
    
    #Condición de Borde: entrada de agua fría (fixed value) en el nodo -1 (ARRIBA)
    fluid.select_bc(bc_type='fixed_value',
                    parameter='T',
                    position=(slice(None, None, None), -1),
                    value=T_cold)
    
    #tiempos para guardar los distintos resultados
    output_times = np.arange(0, simulation_time + output_interval, output_interval)
    fluid.select_output(times=output_times)

    # definiendo el pcm
    bed = ot.create_phase(n=n_bed, n_other=n_fluid, type='bed')
    bed.select_substance(pcm_name)
    bed.select_domain_shape(domain='hollow_sphere_1d', Rinner=R_inner, Router=R_outer)
    bed.select_schemes(diff='central_difference_1d') #discretización solo conducción
    bed.select_initial_conditions(T=T_init) #condición inicial
    bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), 0)) #condiciones bordes
    bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), -1))

    #acoplamiento fluido y pcm
    ot.select_coupling(fluid_phase=0, bed_phase=1, h_exp='constant', h_value=h_value) 
    #simulación
    ot.run_simulation()
    
    print(f"simulación para {pcm_name} terminada")

    #Resultados 
    print("Generando gráfico...")
    time_seconds = fluid.data.time 
    time_hours = time_seconds / 3600 
    outlet_temperature_C = fluid.data.T[:, 0, 0] - 273.15  #La salida del agua caliente es por el nodo 0
    
    #cálculo de Energía Liberada
    power_from_tank = abs(flow_rate) * cp_fluid * (outlet_temperature_C - (T_cold - 273.15))
    energy_released = cumulative_trapezoid(power_from_tank, time_seconds, initial=0)[-1] / 1e6  #la energía en MJ
    
    print(f"Energía Total Liberada ({pcm_name}): {energy_released:.2f} MJ")
#Para poder gráficar todos los pcms, se usa .npz para muchos arrays en un mismo archivo
    np.savez(f"results_{pcm_name}.npz", 
             energy=energy_released, 
             times=time_hours, 
             Tout=outlet_temperature_C)
    print(f"Resultados de datos guardados en results_{pcm_name}.npz")
#graficos
    plt.figure(figsize=(10, 7))
    plt.plot(time_hours, outlet_temperature_C, label=pcm_name, linewidth=2)   
    plt.legend(title='Material PCM')
    plt.title(f'Simulación de Descarga: {pcm_name}', fontsize=16)
    plt.xlabel('Tiempo de Descarga (horas)', fontsize=12)
    plt.ylabel(u'Temperatura de Salida del Agua (°C)', fontsize=12)
    plt.grid(which='major', color='#DDDDDD', linewidth=1)
    plt.minorticks_on()
    plt.ylim(45,85) 
    #guardar el gráfico con un nombre específico del pcm
    plt.savefig(f'grafico_descarga_{pcm_name}.svg')
    print(f"Gráfico 'grafico_descarga_{pcm_name}.svg' guardado.")
    plt.show()

if __name__ == "__main__":
    main()