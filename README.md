# 👻 Ghost-Hash (Polymorphic PoC)

Prueba de concepto de un script automutante diseñado para evadir detecciones basadas en firmas estáticas y análisis en entornos controlados (Sandboxes).

> [!WARNING]
> **ESTADO DEL PROYECTO:** 🛠️ En desarrollo activo. Las funcionalidades actuales son demostrativas.

## 🚀 Características
- **Auto-Mutación:** Modifica su propio código fuente en cada ejecución para generar un hash SHA-256 único sin alterar su funcionalidad.
- **Anti-Sandbox:** Implementa un sistema de puntuación para detectar entornos de análisis mediante:
    - Verificación de memoria RAM disponible.
    - Conteo de núcleos de CPU.
    - Detección de drivers y servicios de virtualización (VirtualBox/VMWare).
- **Zero Dependencies:** Funciona exclusivamente con librerías estándar de Python.

## 🛠️ Uso
```bash
python3 Ghost.py
