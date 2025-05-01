# Sistema de Monitoreo IoT para Refrigeración Farmacéutica

## 🚀 Propósito del Proyecto

El proyecto tiene como objetivo el monitoreo remoto y confiable de condiciones críticas (temperatura, humedad, presión de gas, energía) en espacios de almacenamiento de productos farmacéuticos, especialmente neveras o refrigeradores.

Busca prevenir pérdidas o incumplimientos normativos notificando al usuario vía **mensajes de texto (SMS)** o **notificaciones via whatsapp** cuando se detectan condiciones fuera de los parámetros definidos o fallos de comunicación.

---

## 🏛️ Arquitectura del Sistema

### 1. **Sensores IoT**
- Dispositivos personalizados con microcontrolador ATmega32u4.
- Envían información cada **1 minuto** vía MQTT.
- Miden: temperatura (DS18B20), humedad, energía eléctrica (ADC), y presencia de energía (pin digital).

### 2. **Broker de Mensajería (EMQX)**
- Ejecutándose en un servidor EC2 en AWS.
- Recibe la información MQTT desde cada sensor.

### 3. **Aplicación Web (Django)**
- Backend REST para almacenar los datos.
- Recibe los datos reenviados desde EMQX.
- Valida condiciones:
  - Temperatura fuera de límites.
  - Falta de energía.
  - Sensores inactivos.

### 4. **Sistema de Alertas SMS (AWS SNS)**
- Si una condición de alerta es detectada, se envía un SMS al usuario mediante **Amazon SNS**.
- Costo estimado por SMS en Colombia: **$0.00157 USD**.

### 5. **Tareas Asíncronas (Celery + Celery Beat)**
- Se ejecuta cada **5 minutos** una tarea que valida qué sensores no han enviado datos recientemente (inactividad).
- Envia alerta por SMS si corresponde.

---

## ⚖️ Requisitos Técnicos

### Hardware
- Microcontrolador ATmega32u4.
- Módulo SIM7080G (NB-IoT / LTE-M).
- Display LCD 2x16 para interfaz local.
- EEPROM interna para configuraciones.
- Sensor DS18B20, ADC, botones y alarma visual/acústica.

### Software
- Firmware optimizado en C++ (Arduino).
- MQTT sobre GPRS/NB-IoT.
- Backend en Django + Celery.
- Base de datos PostgreSQL.

---

## 📊 Beneficios

- ✅ Detección inmediata de fallos.
- ✅ Alertas SMS automáticas.
- ✅ Verificación de actividad del sensor.
- ✅ Bajo costo operativo por alerta.
- ✅ Escalable y descentralizado.

---

## 🔍 Mejoras futuras

- Dashboard de monitoreo en tiempo real.
- Enlace con email o Telegram.
- Firma digital de datos.
- Integración con almacenamiento en la nube.

---

## 🛍️ Casos de Uso

- Farmacias.
- Laboratorios.
- Transporte de vacunas o biológicos.
- Cámaras frías industriales.

---

## ✉️ Contacto y Soporte

Para soporte o integración personalizada, contactar a **ingenialo.com** o escribir a **soporte@gthux.com**


--------------------------------


# **Sistema de Monitoreo IoT para Refrigeración Farmacéutica - Resumen del Estado Actual**

## **🔍 Visión General**

El sistema implementa una solución de monitoreo IoT para espacios de almacenamiento de productos farmacéuticos, enfocado principalmente en el control de temperatura, humedad y estado de energía. La plataforma permite la supervisión remota de refrigeradores médicos, con alertas automatizadas cuando los parámetros se salen de los rangos establecidos.

## **🏗️ Arquitectura Implementada**

### Captura de Datos

- **Sensores IoT**: Dispositivos basados en ATmega32u4 que transmiten lecturas cada minuto vía MQTT
- **Variables monitoreadas**: Temperatura (DS18B20), humedad, estado de energía
- **Conectividad**: MQTT sobre GPRS/NB-IoT mediante módulo SIM7080G

### Procesamiento y Almacenamiento

- **Broker MQTT**: EMQX ejecutándose en AWS EC2
- **Backend**: Aplicación Django con API REST
- **Base de datos**: Mysql6
- **Procesamiento asíncrono**: Celery + Celery Beat para tareas programadas

### Interfaz de Usuario

- **Dashboard web**: Visualización de datos en tiempo real con Vue.js
- **Componentes principales**:
    - Indicadores visuales para valores actuales
    - Gráficos históricos con ECharts
    - Opciones de filtrado por fecha y hora
    - Exportación de datos a CSV

## **✅ Funcionalidades Disponibles**

### Monitoreo

- Visualización en tiempo real de valores de temperatura y humedad
- Indicadores visuales de estado (normal, sobre umbral, bajo umbral)
- Monitoreo del estado de energía eléctrica
- Detección automática de sensores inactivos

### Análisis de Datos

- Gráficos históricos con opciones de personalización
- Visualización de tendencias por intervalos (horario, diario, etc.)
- Filtrado por rangos de fechas
- Cálculo automático de valores mínimos, máximos y promedios

### Alertas

- Notificación vía SMS usando AWS SNS cuando:
    - Temperatura fuera de límites configurados
    - Falla en suministro eléctrico
    - Sensor inactivo por más de 0.6 horas

### Administración

- Panel de administración Django para configuración de:
    - Sensores y dispositivos
    - Umbrales de alerta
    - Certificados de calibración
    - Gestión de sitios y organizaciones
    - Usuarios y permisos

### Exportación de Datos

- Descarga de registros históricos en formato CSV
- Reportes personalizados por rango de fechas

## **🔄 Integraciones**

- **AWS SNS**: Para envío de alertas SMS
- **EMQX**: Broker MQTT para gestión de mensajes IoT
- **MQTT.js**: Cliente MQTT para WebSockets en tiempo real

## **🌟 Características Destacadas**

- **Monitoreo en tiempo real** con actualizaciones mediante WebSockets
- **Sistema dual** que integra sensores modernos y legacy
- **Interfaz responsiva** construida con Vue.js y Bootstrap
- **Alertas configurables** por tipo de sensor y sitio
- **Trazabilidad completa** con registros de calibración

## **🚧 Próximas Mejoras**

- Incorporación de alertas vía WhatsApp
- Firma digital de datos para mayor seguridad
- Integración con almacenamiento en la nube
- Mejoras en la interfaz del dashboard en tiempo real