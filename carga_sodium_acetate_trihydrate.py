import openterrace
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg') 
import numpy as np
import sys

def main():
    
    #pcm usado
    pcm_name = "sodium_acetate_trihydrate" 
    
    #parámetros 
    D = 0.3 
    H = 1.5  
    phi = 0.4  
    R_inner = 0.01  
    R_outer = 0.03  
    n_fluid = 100  
    n_bed = 20  
    h_value = 200 
    simulation_time = 4 * 3600  
    dt = 0.1 
    output_interval = 300 

    #carga térmica estática 
    T_init = 273.15 + 20.0 #estanque empieza frío
    T_hot = 273.15 + 80.0  #el calentador a 80°C
    flow_rate = 0.0        #no hay flujo de masa

    print(f"Iniciando simulación de CARGA ESTÁTICA para: {pcm_name} ")

    ot = openterrace.Simulate(t_end=simulation_time, dt=dt)

    #definiendo fase fluida (agua)
    fluid = ot.create_phase(n=n_fluid, type='fluid')
    fluid.select_substance(substance='water')
    fluid.select_domain_shape(domain='cylinder_1d', D=D, H=H)
    fluid.select_porosity(phi=phi)
    fluid.select_schemes(diff='central_difference_1d')
    fluid.select_initial_conditions(T=T_init) 
    fluid.select_massflow(mdot=flow_rate)
    #Nodo 0 es el calentador a 80°C (abajo)
    fluid.select_bc(bc_type='fixed_value',
                     parameter='T',
                     position=(slice(None, None, None), 0),
                     value=T_hot)
    
    #Nodo -1 está aislado (no pierde calor y está arriba)
    fluid.select_bc(bc_type='zero_gradient',
                     parameter='T',
                     position=(slice(None, None, None), -1))
    
    output_times = np.arange(0, simulation_time + output_interval, output_interval)
    fluid.select_output(times=output_times)

    #definiendo fase sólida pcm
    bed = ot.create_phase(n=n_bed, n_other=n_fluid, type='bed')
    bed.select_substance(pcm_name)
    bed.select_domain_shape(domain='hollow_sphere_1d', Rinner=R_inner, Router=R_outer)
    bed.select_schemes(diff='central_difference_1d') 
    bed.select_initial_conditions(T=T_init)
    bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), 0))

    #acoplamiento entre fase fluida y pcm
    ot.select_coupling(fluid_phase=0, bed_phase=1, h_exp='constant', h_value=h_value)
    
    #simulación
    ot.run_simulation()
    
    print(f"Simulación de CARGA ESTÁTICA terminada.")

    #resultados  
    time_seconds = fluid.data.time 
    time_hours = time_seconds / 3600 

    #temperatura en 3 puntos del estanque:
    T_fondo = fluid.data.T[:, 0, 1] - 273.15  
    T_medio = fluid.data.T[:, 0, int(n_fluid/2)] - 273.15 #nodo 50 (la mitad)
    T_cima = fluid.data.T[:, 0, -1] - 273.15 #nodo -1 (la cima, n_fluid-1)

    #guarda resultados en archivo .npz ---
    print("Guardando resultados (solo T y tiempo)")
    
    output_filename_data = f"results_CARGA_CONDUCCION_{pcm_name}.npz"
    #guarda resultados
    np.savez(output_filename_data, 
             times_hours=time_hours, 
             T_fondo_C=T_fondo,
             T_medio_C=T_medio,
             T_cima_C=T_cima)
    
    print(f"Resultados guardados en {output_filename_data}")

    #gráficos
    print("Generando gráfico...")
    plt.figure(figsize=(10, 7))
    plt.plot(time_hours, T_fondo, label=f'Fondo (Nodo 1)', linestyle='--')  
    plt.legend(title='Posición en el Estanque')
    plt.title(f'Simulación de Carga Estática (Solo Conducción): {pcm_name}', fontsize=16)
    
    #agregar leyenda de pcms
    pcm_nombre_bonito = pcm_name.replace("_", " ").title()
    plt.text(0.05, 0.95, f'PCM Utilizado: {pcm_nombre_bonito}',
             transform=plt.gca().transAxes, 
             fontsize=12,
             verticalalignment='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.5))

    plt.xlabel('Tiempo de Carga (horas)', fontsize=12)
    plt.ylabel(u'Temperatura del Agua (°C)', fontsize=12)
    plt.grid(which='major', color='#DDDDDD', linewidth=1)
    plt.minorticks_on()
    plt.ylim(T_init - 273.15 - 5, T_hot - 273.15 + 5) 
    plt.xlim(0, simulation_time / 3600)

    #guardar el gráfico
    output_filename_plot = f'grafico_CARGA_CONDUCCION_{pcm_name}.svg'
    plt.savefig(output_filename_plot)
    print(f"Gráfico '{output_filename_plot}' guardado.")
    plt.show()

if __name__ == "__main__":
    main()