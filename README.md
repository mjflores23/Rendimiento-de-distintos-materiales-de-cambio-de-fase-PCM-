# Contexto:
<p align="justify">
La demanda energética en los sectores comerciales e industriales experimentan una variabilidad relevante tanto a diario como de forma estacional. Esta variación se ha intensificado con la creciente adopción de fuentes de energía renovables, como la energía solar, cuyo suministro es intermitente y cíclica. En particular, la energía solar no está disponible durante los periodos de alta demanda nocturna, y las cargas de refrigeración pueden extenderse después del atardecer (Dinçer & Rosen, 2011).
<p align="justify">
Para abordar este problema de desajuste entre la oferta y la demanda, los sistemas de almacenamiento de energía térmica (TES) se han consolidado como una tecnología clave. Los sistemas TES son fundamentales para garantizar la viabilidad de las aplicaciones solares. (Dinçer & Rosen, 2011). 
<p align="justify">
Dentro de las tecnologías TES, el almacenamiento de calor latente (LHTES) utilizando materiales de cambio de fase (PCM) se ha convertido en un tema de gran interés. Los PCM ofrecen ventajas significativas, como poseer una alta densidad de almacenamiento de energía por unidad de masa en comparación en comparación con los sistemas de calor sensible. Esta alta densidad, permite que el diseño de almacenamiento sea más compactos y ligeros. Además, el cambio de fase ocurre a una temperatura constante, lo que optimiza la eficiencia operativa. (Dinçer & Rosen, 2011). 

# Relevancia del Almacenamiento Térmico en aplicaciones residenciales:
<p align="justify">
La investigación y modelización de estanques de agua caliente sanitaria (ACS) utilizando Materiales de Cambio de Fase (PCM) adquiere una relevancia significativa debido a su potencial para optimizar el consumo energético en el ámbito residencial y reducir los costos operativos asociados. El consumo de energía en los edificios representa una porción considerable del consumo energético total en los países desarrollados, siendo el calentamiento de agua una de las principales fuentes de alta demanda energética, especialmente durante los períodos punta del día (Najafian, Haghighat, & Moreau, 2015). Estos picos de demanda exigen que la red eléctrica opere a su máxima capacidad, lo que incrementa el costo de la energía y ejerce presión sobre la infraestructura existente.
<p align="justify">
El uso de Sistemas de Almacenamiento de Energía Térmica (TES) en estanques residenciales es una tecnología prometedora destinada a mitigar este desafío. Al no usar electricidad en horas punta, dejas de estresar la red eléctrica. Eso ayuda a prevenir apagones y reduce la necesidad de usar las plantas de energía de emergencia, que son las más caras y contaminantes (Najafian, Haghighat, & Moreau, 2015). En particular, el almacenamiento de calor latente mediante PCM ofrece ventajas sustanciales sobre el almacenamiento sensible (como el de agua), principalmente debido a su capacidad para almacenar energía a alta densidad y liberarla con una variación mínima de temperatura.
<p align="justify">
La relevancia de esta tecnología radica, en primer lugar, en su capacidad para desplazar la demanda eléctrica durante los períodos de alto consumo. El sistema permite cargar el estanque (almacenar calor) en los períodos valle, aprovechando excedentes de energía solar durante el día o electricidad de bajo costo durante la noche. Posteriormente, el estanque puede descargar el calor almacenado en el PCM para proporcionar agua caliente en las horas de mayor demanda, sin necesidad de activar los calentadores eléctricos.
<p align="justify">
Como demuestra el estudio de referencia, un estanque residencial optimizado con PCM puede suministrar agua caliente durante todo el día y, lo más importante, desplazar completamente el consumo eléctrico durante los períodos punta, logrando así un ahorro energético neto en comparación con un estanque convencional (Najafian, Haghighat, & Moreau, 2015).
<p align="justify">
En el contexto chileno, la relevancia económica de esta tecnología se amplifica al considerar el desarrollo o la selección de materiales locales. El uso de PCMs de bajo costo y alta disponibilidad en el país, como las sales (por ejemplo, el acetato de sodio) o los hidratos de magnesio (como el nitrato o cloruro de magnesio provenientes de los salares del norte de Chile), permitiría reducir significativamente los costos de implementación de esta tecnología, convirtiéndola en una solución de eficiencia energética viable y escalable para las viviendas nacionales.

# Implementación de la Simulación de Descarga de Estanque con PCMs de Chile 
<p align="justify">
Este proyecto utiliza el software open-source openterrace para simular y comparar el rendimiento térmico de 5 Materiales de Cambio de Fase (PCMs) diferentes, con un enfoque en sales y compuestos relevantes para Chile.El objetivo es evaluar qué material ofrece el mejor almacenamiento y entrega de energía para un estanque de agua caliente sanitaria en un escenario de descarga estandarizado.

**Contexto del Benchmark**

Todas las simulaciones se basan en un benchmark estandarizado que representa la descarga de un estanque de lecho empacado:
- Geometría del Estanque: Cilindro vertical (Altura: 1.5 m, Diámetro: 0.3 m).
- PCM: Cápsulas esféricas huecas (Radio ext: 0.03 m, Radio int: 0.01 m).
- Condición Inicial: El estanque (agua + PCM) está completamente cargado a 80°C.
- Simulación de Descarga: Se inyecta agua fría a 20°C por la parte superior del estanque.
- Flujo: El agua fluye hacia abajo a -0.01 kg/s.
- Salida: El agua caliente se mide en la parte inferior (nodo 0).
- Duración: 4 horas (14400 segundos).
  
**Implementación (Paso a Paso)** 

Se debe seguir estos 3 pasos para replicar los resultados.

**Requisitos Previos**

Asegúrate de tener Python y las siguientes librerías instaladas:
```pip install openterrace numpy matplotlib scipy```

### Paso 1: "Instalar" los Paquetes de PCM
 ```OpenTerrace``` no incluye estos materiales por defecto. Se debe añadir manualmente a la librería.
 
1. Encuentra la librería: Encuentra la ruta de ```Openterrace``` para luego abrir la carpeta  ```bed_substances```

2. **Copia los 5 paquetes:**  
   Copia los 5 archivos `.py` de los materiales (que están en este repositorio) y pégalos dentro de la carpeta:  
   ```.../openterrace/bed_substances/.```

   - `sodium_acetate_trihydrate.py`  
   - `magnesium_eutectic.py`  
   - `barium_hydroxide_octahydrate.py`  
   - `magnesium_nitrate_hexahydrate.py`  
   - `magnesium_chloride_hexahydrate.py`

3. Ahora **OpenTerrace** “conoce” los 5 materiales (PCMs).

### Paso 2: Ejecutar las 5 Simulaciones (una por una)

Debido a un *bug de estado* en **OpenTerrace** que impide usar un bucle `for`, se debe ejecutar **cada simulación en un proceso de Python separado**.

En la terminal, ejecuta los siguientes 5 scripts, **uno por uno**. Cada script correrá una simulación de 4 horas y guardará los resultados en un archivo `.npz`.

# Simulación 1
`simulate_sodium_acetate.py`.
 → Espera a que termine... se creará "results_sodium_acetate_trihydrate.npz"

# Simulación 2
`simulate_magnesium_eutectic.py`
 → Espera a que termine... se creará "results_magnesium_eutectic.npz"

# Simulación 3
`simulate_barium_hydroxide.py`
 → Espera a que termine... se creará "results_barium_hydroxide_octahydrate.npz"

# Simulación 4
`simulate_magnesium_nitrate.py`
→ Espera a que termine... se creará "results_magnesium_nitrate_hexahydrate.npz"

# Simulación 5
`simulate_magnesium_chloride.py`
→ Espera a que termine... creará "results_magnesium_chloride_hexahydrate.npz"

### Paso 3: Generar el gráfico comparativo y los Resultados
Una vez que se tenga los 5 archivos `results_...npz` en la carpeta, ejecuta el script final de ploteo:
`plot_all_pcms.py`

**Resultados Esperados:**
Al ejecutar el ``` plot_all_pcms.py```, obtendrás dos salidas:
1. Un gráfico (`comparacion_descarga_FINAL.png`): Una ventana emergente mostrará el gráfico comparativo de la temperatura de salida de los 5 PCMs a lo largo de las 4 horas.
2. Una tabla en la terminal: Mostrará la "Energía total liberada (MJ)" para cada PCM, ordenada del mejor al peor, permitiendo un análisis cuantitativo del rendimiento.


# Figura del Sistema:
<h3 align="center">Figura del Sistema</h3>

<p align="center">
  <img width="315" height="485" alt="image" src="https://github.com/user-attachments/assets/dbed3a99-8d12-45cd-9d64-35d8268faff9" />
  <br>
  <em>Figura 1: Carga térmica (Elaboración propia)</em>
</p>


# Rendimiento-de-distintos-materiales-de-cambio-de-fase-PCM-
Este proyecto consiste en utilizar el paquete de Python OpenTerrace, que incluye modelos para estanques de almacenamiento térmico. Dado que el paquete tiene pocos PCMs disponibles, investigaré nuevos materiales en la literatura y los incorporaré al código. Luego, realizaré simulaciones para evaluar el rendimiento de un PCM relevante para el país.

```
pip install openterrace
```


Referencias:
Dinçer, I., & Rosen, M. A. (2011). Thermal energy storage: Systems and applications. Wiley.
Najafian, A., Haghighat, F., & Moreau, A. (2015). Integration of PCM in domestic hot water tanks: Optimization for shifting peak demand. Energy and Buildings, 106, 59–64. https://doi.org/10.1016/j.enbuild.2015.05.036
