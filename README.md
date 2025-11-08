# Caso práctico 3 [COLABORATIVO 02]: Solución Agentica NLP
### **Criterio**

**Argumentos**:

<p><b>Transporte</b>: Optimización del Tráfico y la Logística en Tiempo Real
En el transporte, una implementación clave es el análisis de sentimiento y eventos en redes sociales y fuentes de noticias para predecir y gestionar el flujo de tráfico y la logística urbana.</p>


* **Problema** : Los sistemas de gestión de tráfico tradicionales dependen de sensores fijos (cámaras, bucles inductivos) que no capturan la totalidad de los eventos que afectan la movilidad, como accidentes menores, protestas, eventos deportivos o condiciones peligrosas reportadas por los ciudadanos.
* **Solución con NLP** : Un sistema de NLP puede monitorear en tiempo real plataformas como Twitter, Waze y noticias locales. Es capaz de identificar y clasificar publicaciones que describen incidentes de tráfico, entender su ubicación geográfica (geolocalización) y evaluar su severidad a partir del lenguaje utilizado ("gran accidente", "tráfico detenido", "calle inundada").
* **Impacto** : Permite a las autoridades de tránsito y a las empresas de logística reaccionar de forma proactiva ante disrupciones no detectadas por sensores tradicionales. Esto se traduce en un re-direccionamiento más eficiente de las rutas, una reducción de los congestionamientos, tiempos de entrega más precisos y una mejora en la seguridad vial al alertar a los conductores sobre peligros imprevistos.

<p>A partir de estos argumentos, se requiere que el team se apoye en una red social o la ingenieria de cookies para recomendar al propio usuario o autorizadades plan de acción. El ejercicio NLP busca analizar Cookies u otra contenido social para ofertar al usuario temas de interes. Los temas de interes se pueden enfocar en:</p>

* Deportes/rutinas de ejercicio.
* Peliculas
* Consejos de salud
* Dieta
* Hobie

<p>El cookie o post de red social no posee el todo, por lo cual deben ser combinado con perfiles ampliado de edad y otros datos demograficos de interes.</p>


```
fitness_recommender/
│
├── data/
│   └── fitness_dataset.csv
│
├── notebooks/
│   └── Caso práctico 3: Solución Agentica NLP - COLABORATIVO.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── recommender.py
│   ├── nlp_agent.py
│   └── visualization.py
│
├── app/
│   └── main_app.py 
│
├── requirements.txt
└── README.md
```
