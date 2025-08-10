# Cargar-Notas

# 🗂️ Validación y Consolidación de Notas — CNP

Script en Python para validar, filtrar y consolidar notas reportadas por docentes y producir un archivo listo para subir a la base de datos institucional.  
Valida formatos, detecta duplicados, asegura el orden esperado de los desempeños y agrega las notas válidas a la base maestra.

---

## 🚀 Qué hace
- Lee la **hoja de notas**  y el **listado de estudiantes** .
- Lee notas reportadas por docentes desde archivos individuales por área.
- Filtra las notas por **semana** (el script solicita el número de semana por consola).
- Valida:
  - que la asignatura sea una de las permitidas,
  - que el estudiante esté en el listado general,
  - que no exista un desempeño duplicado ya en la base maestra,
  - que la nota corresponda al **siguiente desempeño esperado** según la secuencia de bloques/etapas.
- Agrega las notas válidas a la hoja de notas y exporta un Excel consolidado:
  - `Notas Para Subir Primaria.xlsx`

---

## 🛠 Tecnologías usadas
- Python 3.8+  
- pandas  
- NumPy  
- openpyxl

---

## 📄 Notas
- El script está diseñado para integrarse con la estructura de datos del **Colegio Gimnasio Kaiporé**.
- Hay dos scripts, con diferencias muy concretas en las materias y áreas que se manejan diferente en primaria y bachillerato.
- Automatiza un proceso que antes realizaban **2 coordinadores**, cada uno dedicando aproximadamente **2 horas semanales** a la validación y consolidación de notas.
- Gracias a este script, el mismo trabajo se completa en **menos de 2 minutos**, reduciendo drásticamente el tiempo invertido y eliminando la mayor parte de los errores manuales.

