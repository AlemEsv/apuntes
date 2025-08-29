# Introducción a la Inteligencia Artificial - Clase 1

## Tabla de Contenidos

1. [Fundamentos Filosóficos de la IA](#fundamentos-filosóficos-de-la-ia)

2. [El Test de Turing](#test-de-turing)

3. [Métodos de Investigación](#métodos-de-investigación)

4. [Historia de la IA](#historia-de-la-ia)

5. [¿Por qué tanto interés en la IA?](#por-qué-tanto-interés-en-la-ia)

---

## Fundamentos Filosóficos de la IA

### Ramas de la Filosofía aplicadas a la IA

```mermaid
graph TD
    A[Filosofía de la IA] --> B[Ontología]
    A --> C[Epistemología]
    A --> D[Axiología/Ética]
    
    B --> B1["¿Por qué existimos?<br/>Naturaleza del ser"]
    C --> C1["Percepción de la realidad<br/>y conocimiento"]
    D --> D1["Moral y ética<br/>¿Qué es correcto e incorrecto?"]
```

### **Ética en IA - Puntos Clave**

- Democracia y participación ciudadana
- Transparencia en algoritmos
- Sesgo y equidad
- Privacidad y derechos digitales

### Experimentos Filosóficos Importantes

- **Test de Turing (1950)**: ¿Puede una máquina pensar?
- **Habitación China (John Searle)**: Crítica al test de Turing sobre comprensión vs. simulación

---

## Test de Turing

> **Definición**: El primer intento formal de definir inteligencia artificial, propuesto por Alan Turing en 1950.

### Capacidades Requeridas para el Test de Turing Básico

```mermaid
mindmap
  root((Test de Turing))
    Reconocimiento del Lenguaje Natural
      Procesamiento de texto
      Comprensión semántica
    Razonamiento
      Lógica deductiva
      Resolución de problemas
    Aprendizaje
      Adaptación
      Mejora continua
    Representación del Conocimiento
      Estructuras de datos
      Bases de conocimiento
```

### Test de Turing Total (Capacidades Adicionales)

- **Visión Artificial**: Procesamiento e interpretación de imágenes
- **Robótica**: Manipulación física del entorno

### 📝 **Tarea Pendiente**
>
> Buscar ejemplos específicos de cada capacidad del Test de Turing en sistemas de IA actuales.

---

## Métodos de Investigación

### Enfoques Científicos en IA

| Método Deductivo | Método Inductivo |
|------------------|------------------|
| 1. Teoría | 1. Observación |
| 2. Hipótesis | 2. Identificación de patrones |
| 3. Observaciones | 3. Hipótesis tentativa |
| 4. Confirmación | 4. Teoría |

```mermaid
flowchart LR
    A[Problema] --> B[Modelo Simplificado]
    B --> C[Objetivo Definido]
    C --> D[Función de Evaluación]
    D --> E{Calidad de la Solución}
    E --> F[Buena]
    E --> G[Regular]
    E --> H[Deficiente]
```

> **Nota Importante**: La calidad de la función de evaluación determina directamente la calidad de la solución obtenida.

---

## Historia de la IA

### Timeline de Desarrollos Clave

```mermaid
timeline
    title Historia de la Inteligencia Artificial
    
    1901 : PCA (Principal Component Analysis)
    1933 : Hotelling desarrolla PCA
    1950 : Perceptrón : Parte crucial para el desarrollo de la IA
    1965 : Fuzzy Sets (Conjuntos Difusos)
    1969 : Limitaciones del Perceptrón
    1982 : SOM (Self-Organizing Maps)
    1986 : Backpropagation : Algoritmo fundamental para aprendizaje
         : I/O3
    1993 : Algoritmos CYS
    1995 : Random Forest
         : CNN (Convolutional Neural Networks)
    2001 : Mejoras en Random Forest
    2006 : Fast Learning Algorithms
    2007 : Greedy Layer-wise Training for Deep Networks
    2013 : AlexNet : Revolución en Deep Learning
```

### **Hitos Más Importantes**

1. **1950 - Perceptrón**: Base de las redes neuronales modernas
2. **1986 - Backpropagation**: Algoritmo que permitió entrenar redes profundas
3. **2013 - AlexNet**: Inicio de la era del Deep Learning

---

## ¿Por qué tanto interés en la IA?

### Factores Clave del Boom Actual

```mermaid
pie title Factores del Crecimiento de la IA
    "Progresos en Algoritmos" : 35
    "Disponibilidad de Datos" : 30
    "Desarrollo del Hardware" : 25
    "Inversión y Recursos" : 10
```

1. **Progresos Recientes en Algoritmos**
   - Desarrollo continuo de nuevas técnicas
   - Mejoras en eficiencia y precisión

2. **Disponibilidad de Datos**
   - Big Data
   - Fuentes diversas de información

3. **Desarrollo del Hardware**
   - GPUs especializadas
   - Procesadores dedicados (TPUs)
   - Computación en la nube

---

## **Preguntas de Reflexión**

> - **¿Qué es la IA?** No hay consenso entre los especialistas del área.
> - **¿Dónde se ponen los límites de lo que es o no inteligencia?** Una pregunta fundamental que sigue sin respuesta definitiva.
> - **¿Cuándo se empezó a utilizar el término "IA"?** Investigar el origen histórico del término.

---

## **Notas Adicionales**

- **Razonamiento Automático**: Capacidad de las máquinas para hacer inferencias lógicas
- **PCA vs PCR**: Investigar la relación entre estos métodos estadísticos
- Actualizar información sobre modelos de IA más recientes (GPT, BERT, etc.)
