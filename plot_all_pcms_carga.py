import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg') 

def main():

    archivos_a_comparar = {
        "Acetato de Sodio": "results_CARGA_CONDUCCION_sodium_acetate_trihydrate.npz",
        "Bario Octahidratado": "results_CARGA_CONDUCCION_barium_hydroxide_octahydrate.npz",
        "Cloruro de magnesio": "results_CARGA_CONDUCCION_magnesium_chloride_hexahydrate.npz",
        "Nitrato de magnesio": "results_CARGA_CONDUCCION_magnesium_nitrate_hexahydrate.npz",
        "Magnesio eutectico": "results_CARGA_CONDUCCION_magnesium_eutectic.npz"}


    print("Iniciando Script de Comparación (Solo Temp. Fondo - Nodo 1)")
    
    #figura creada
    fig, ax_temp = plt.subplots(figsize=(12, 8))
    
    #colores
    colores = plt.cm.viridis(np.linspace(0, 1, len(archivos_a_comparar)))
    max_time = 0 

    #for para cargar archivos
    
    for i, (etiqueta, nombre_archivo) in enumerate(archivos_a_comparar.items()):
        
        print(f"Cargando {nombre_archivo} (para '{etiqueta}')...")
        
        try:
        
            data = np.load(nombre_archivo)
            times = data['times_hours']
            
            temp_a_graficar = data['T_fondo_C']
            ax_temp.plot(times, temp_a_graficar, label=f'Temp. Fondo: {etiqueta}', 
                         linestyle='-', linewidth=2.5, color=colores[i])
          
            
            #tiempo de eje x
            if times.max() > max_time:
                max_time = times.max()

        except FileNotFoundError:
            print(f"advertencia:No se encontró el archivo: {nombre_archivo}.")
            print("  Asegúrate de haber corrido la simulación primero.")
            print("  Se omitirá este archivo del gráfico.")
        except KeyError as e:
            print(f"  error:El archivo {nombre_archivo} no contiene la variable esperada: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado cargando {nombre_archivo}: {e}")

    #grafico
    fig.suptitle("Comparación de Carga Estática de PCMs (Temp. Fondo Nodo 1)", fontsize=18)
    ax_temp.set_xlabel("Tiempo (horas)", fontsize=12)
    ax_temp.set_ylabel(u"Temperatura en el Fondo (Nodo 1) (°C)", fontsize=12)
    ax_temp.grid(True, which='major', linestyle='--', linewidth=0.5)
    ax_temp.legend(loc='best') 
    ax_temp.set_xlim(left=0, right=max_time)
    ax_temp.set_ylim(bottom=15) 
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    #nombre archivo a guardar
    output_filename = "grafico_comparativo_benchmark.svg"
    plt.savefig(output_filename)
    print(f"Gráfico comparativo guardado en '{output_filename}'")
    plt.show()

if __name__ == "__main__":
    main()
