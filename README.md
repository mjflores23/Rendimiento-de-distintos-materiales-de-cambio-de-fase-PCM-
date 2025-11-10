# Contexto:
La demanda energética en los sectores comerciales e industriales experimentan una variabilidad relevante tanto a diario como de forma estacional. Esta variación se ha intensificado con la creciente adopción de fuentes de energía renovables, como la energía solar, cuyo suministro es intermitente y cíclica. En particular, la energía solar no está disponible durante los periodos de alta demanda nocturna, y las cargas de refrigeración pueden extenderse después del atardecer (Dinçer & Rosen, 2011).

Para abordar este problema de desajuste entre la oferta y la demanda, los sistemas de almacenamiento de energía térmica (TES) se han consolidado como una tecnología clave. Los sistemas TES son fundamentales para garantizar la viabilidad de las aplicaciones solares. (Dinçer & Rosen, 2011). 

Dentro de las tecnologías TES, el almacenamiento de calor latente (LHTES) utilizando materiales de cambio de fase (PCM) se ha convertido en un tema de gran interés. Los PCM ofrecen ventajas significativas, como poseer una alta densidad de almacenamiento de energía por unidad de masa en comparación en comparación con los sistemas de calor sensible. Esta alta densidad, permite que el diseño de almacenamiento sea más compactos y ligeros. Además, el cambio de fase ocurre a una temperatura constante, lo que optimiza la eficiencia operativa. (Dinçer & Rosen, 2011). 

# Relevancia del Almacenamiento Térmico en aplicaciones residenciales:
La investigación y modelización de estanques de agua caliente sanitaria (ACS) utilizando Materiales de Cambio de Fase (PCM) adquiere una relevancia significativa debido a su potencial para optimizar el consumo energético en el ámbito residencial y reducir los costos operativos asociados. El consumo de energía en los edificios representa una porción considerable del consumo energético total en los países desarrollados, siendo el calentamiento de agua una de las principales fuentes de alta demanda energética, especialmente durante los períodos punta del día (Najafian, Haghighat, & Moreau, 2015). Estos picos de demanda exigen que la red eléctrica opere a su máxima capacidad, lo que incrementa el costo de la energía y ejerce presión sobre la infraestructura existente.

El uso de Sistemas de Almacenamiento de Energía Térmica (TES) en estanques residenciales es una tecnología prometedora destinada a mitigar este desafío. Al no usar electricidad en horas punta, dejas de estresar la red eléctrica. Eso ayuda a prevenir apagones y reduce la necesidad de usar las plantas de energía de emergencia, que son las más caras y contaminantes (Najafian, Haghighat, & Moreau, 2015). En particular, el almacenamiento de calor latente mediante PCM ofrece ventajas sustanciales sobre el almacenamiento sensible (como el de agua), principalmente debido a su capacidad para almacenar energía a alta densidad y liberarla con una variación mínima de temperatura.

La relevancia de esta tecnología radica, en primer lugar, en su capacidad para desplazar la demanda eléctrica durante los períodos de alto consumo. El sistema permite cargar el estanque (almacenar calor) en los períodos valle, aprovechando excedentes de energía solar durante el día o electricidad de bajo costo durante la noche. Posteriormente, el estanque puede descargar el calor almacenado en el PCM para proporcionar agua caliente en las horas de mayor demanda, sin necesidad de activar los calentadores eléctricos.

Como demuestra el estudio de referencia, un estanque residencial optimizado con PCM puede suministrar agua caliente durante todo el día y, lo más importante, desplazar completamente el consumo eléctrico durante los períodos punta, logrando así un ahorro energético neto en comparación con un estanque convencional (Najafian, Haghighat, & Moreau, 2015).

En el contexto chileno, la relevancia económica de esta tecnología se amplifica al considerar el desarrollo o la selección de materiales locales. El uso de PCMs de bajo costo y alta disponibilidad en el país, como las sales (por ejemplo, el acetato de sodio) o los hidratos de magnesio (como el nitrato o cloruro de magnesio provenientes de los salares del norte de Chile), permitiría reducir significativamente los costos de implementación de esta tecnología, convirtiéndola en una solución de eficiencia energética viable y escalable para las viviendas nacionales.

# Implementación de la Simulación de Descarga de Estanque con PCMs de Chile 
Este proyecto utiliza el software open-source openterrace para simular y comparar el rendimiento térmico de 5 Materiales de Cambio de Fase (PCMs) diferentes, con un enfoque en sales y compuestos relevantes para Chile.El objetivo es evaluar qué material ofrece el mejor almacenamiento y entrega de energía para un estanque de agua caliente sanitaria (ACS) en un escenario de descarga estandarizado.Contexto del BenchmarkTodas las simulaciones se basan en un benchmark estandarizado que representa la descarga de un estanque de lecho empacado:Geometría del Estanque: Cilindro vertical (Altura: 1.5 m, Diámetro: 0.3 m).PCM: Cápsulas esféricas huecas (Radio ext: 0.03 m, Radio int: 0.01 m).Condición Inicial: El estanque (agua + PCM) está completamente cargado a 80°C.Simulación de Descarga: Se inyecta agua fría a 20°C por la parte superior del estanque.Flujo: El agua fluye hacia abajo a -0.01 kg/s.Salida: El agua caliente se mide en la parte inferior (nodo 0).Duración: 4 horas (14400 segundos).
Receta de Implementación (Paso a Paso)Sigue estos 3 pasos para replicar los resultados.Requisitos PreviosAsegúrate de tener Python y las siguientes librerías instaladas:pip install openterrace numpy matplotlib scipy
Paso 1: "Instalar" los Paquetes de PCMOpenTerrace no incluye estos materiales por defecto. Debes añadirlos manualmente a la librería.Encuentra tu librería: Busca la carpeta site-packages de tu instalación de Python. Dentro, encontrarás la ruta de openterrace:Ejemplo en Windows: C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python311\Lib\site-packages\openterrace\substances\Ejemplo en Mac/Linux: .../lib/python3.11/site-packages/openterrace/substances/Copia los 5 Paquetes: Copia los 5 archivos .py de los materiales (que están en la carpeta pcm_packages de este repositorio) y pégalos dentro de la carpeta .../openterrace/substances/.sodium_acetate_trihydrate.pymagnesium_eutectic.pybarium_hydroxide_octahydrate.pymagnesium_nitrate_hexahydrate.pymagnesium_chloride_hexahydrate.py¡Listo! Ahora openterrace "conoce" tus 5 materiales.Paso 2: Ejecutar las 5 Simulaciones (Una por Una)Debido a un bug de estado en openterrace que impide usar un bucle for, debemos ejecutar cada simulación en un proceso de Python separado.En tu terminal, ejecuta los siguientes 5 scripts, uno por uno. Cada script correrá una simulación de 4 horas y guardará los resultados en un archivo .npz.# Simulación 1
python simulate_sodium_acetate.py
(Espera a que termine... creará "results_sodium_acetate_trihydrate.npz")# Simulación 2
python simulate_magnesium_eutectic.py
(Espera a que termine... creará "results_magnesium_eutectic.npz")# Simulación 3
python simulate_barium_hydroxide.py
(Espera a que termine... creará "results_barium_hydroxide_octahydrate.npz")# Simulación 4
python simulate_magnesium_nitrate.py
(Espera a que termine... creará "results_magnesium_nitrate_hexahydrate.npz")# Simulación 5
python simulate_magnesium_chloride.py
(Espera a que termine... creará "results_magnesium_chloride_hexahydrate.npz")Paso 3: Generar el Gráfico Comparativo y los ResultadosUna vez que tengas los 5 archivos results_...npz en tu carpeta, ejecuta el script final de ploteo:python plot_all_pcms.py
📈 Resultados EsperadosAl ejecutar el plot_all_pcms.py, obtendrás dos salidas:Un gráfico (comparacion_descarga_FINAL.png): Una ventana emergente mostrará el gráfico comparativo de la temperatura de salida de los 5 PCMs a lo largo de las 4 horas.Una tabla en la terminal: Mostrará la "Energía Total Liberada (MJ)" para cada PCM, ordenada del mejor al peor, permitiendo un análisis cuantitativo del rendimiento.












# Figura del Sistema:
<img width="325" height="516" alt="image" src="https://github.com/user-attachments/assets/88478938-ec13-4ac2-a343-c32bf5dc4e57" />


# Rendimiento-de-distintos-materiales-de-cambio-de-fase-PCM-
Este proyecto consiste en utilizar el paquete de Python OpenTerrace, que incluye modelos para estanques de almacenamiento térmico. Dado que el paquete tiene pocos PCMs disponibles, investigaré nuevos materiales en la literatura y los incorporaré al código. Luego, realizaré simulaciones para evaluar el rendimiento de un PCM relevante para el país.

```
pip install openterrace
```



Referencias:
Dinçer, I., & Rosen, M. A. (2011). Thermal energy storage: Systems and applications. Wiley.
Najafian, A., Haghighat, F., & Moreau, A. (2015). Integration of PCM in domestic hot water tanks: Optimization for shifting peak demand. Energy and Buildings, 106, 59–64. https://doi.org/10.1016/j.enbuild.2015.05.036
