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

# Implementación del Código



# Figura del Sistema:
<img width="325" height="516" alt="image" src="https://github.com/user-attachments/assets/d9b7a500-9595-4089-919b-bce05f5ee83b" />


# Rendimiento-de-distintos-materiales-de-cambio-de-fase-PCM-
Este proyecto consiste en utilizar el paquete de Python OpenTerrace, que incluye modelos para estanques de almacenamiento térmico. Dado que el paquete tiene pocos PCMs disponibles, investigaré nuevos materiales en la literatura y los incorporaré al código. Luego, realizaré simulaciones para evaluar el rendimiento de un PCM relevante para el país.

```
pip install openterrace
```



Referencias:
Dinçer, I., & Rosen, M. A. (2011). Thermal energy storage: Systems and applications. Wiley.
Najafian, A., Haghighat, F., & Moreau, A. (2015). Integration of PCM in domestic hot water tanks: Optimization for shifting peak demand. Energy and Buildings, 106, 59–64. https://doi.org/10.1016/j.enbuild.2015.05.036
