import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
import os

def plot_and_summarize():
    
    pcms = [
        "sodium_acetate_trihydrate",
        "magnesium_eutectic",
        "barium_hydroxide_octahydrate",
        "magnesium_nitrate_hexahydrate",
        "magnesium_chloride_hexahydrate"
    ]
    
    #guardar los resultados para la tabla
    results_table = {}
    #configuración del gráfico
    plt.figure(figsize=(12, 8))
    
    for pcm in pcms:
        file_name = f"results_{pcm}.npz"
        
        #se verifica si el archivo de resultados existe
        if not os.path.exists(file_name):
            print(f"ADVERTENCIA: No se encontró '{file_name}'.")
            print(f"Por favor, ejecuta primero el script de simulación para '{pcm}'.")
            continue
            
        #cargar los datos del archivo .npz
        data = np.load(file_name)
        
        energy_released = data['energy']
        times_discharge_hours = data['times']
        Tout_discharge = data['Tout']
        
        #guardar para la tabla
        results_table[pcm] = energy_released
        
        plt.plot(times_discharge_hours, Tout_discharge, label=pcm, linewidth=2.5)

    #gráfico

    plt.legend(title='Material PCM')
    plt.title('Comparativa de Descarga de PCMs')
    plt.xlabel('Tiempo (horas)')
    plt.ylabel('Temperatura de Salida del Agua (°C)')
    plt.grid(True, which='major', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.ylim(45, 85) 
    plt.xlim(0, 4)  
    plt.tight_layout()
    plt.savefig('comparacion_descarga_FINAL.png') 
    plt.show()

    #Resultados
    print("\nResultados del Benchmark (Energía Total Liberada):")
    print("=" * 60)
    print(f"{'PCM':<35} | {'Energía Liberada (MJ)':<20}")
    print("-" * 60)
    
    #ordenen de los resultados de mejor a peor
    sorted_results = sorted(results_table.items(), key=lambda item: item[1], reverse=True)
    
    for pcm_name, energy in sorted_results:
        print(f"{pcm_name:<35} | {energy:<20.2f}")

if __name__ == "__main__":
    plot_and_summarize()