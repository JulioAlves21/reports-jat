
# Módulo de Reportes JAT

Este módulo extiende la funcionalidad de **Odoo** para generar reportes personalizados en formato **PDF (QWeb)**.  
Incluye reportes de **ventas** y de **cargas**, con filtros por fechas y empleados, listos para ser utilizados dentro del sistema.

---

## Funcionalidades principales

- **Reporte de Ventas (`sale_report.xml`)**
  - Permite obtener un listado de pedidos en un rango de fechas.
  - Incluye: número de pedido, cliente e importe total.
  - Muestra el total acumulado al final del reporte.

- **Reporte de Cargas (`report_charge.xml`)**
  - Muestra los productos cargados por empleado en un rango de fechas.
  - Incluye: nombre del producto y cantidad.

- **Integración con Wizards**
  - Los reportes se vinculan con `reports.sale.report.wizard` para la selección dinámica de parámetros.

---

## Archivos principales

- **`reports_jat.py`** → Lógica de abstracción del reporte en Odoo.
- **`sale_report.xml`** → Plantilla QWeb para el reporte de ventas.
- **`report_charge.xml`** → Plantilla QWeb para el reporte de cargas.
- **`templates.xml`** → Estructura base para plantillas (comentada).
- **`views.xml`** → Definiciones de vistas y menús (comentadas, para futuras ampliaciones).


---

## 📊 Ejemplo de uso

1. Seleccionar un rango de fechas y un empleado/vendedor.
2. Generar el reporte en formato PDF.
3. Descargar o imprimir el reporte desde Odoo.

---

## ✍️ Autor

**Julio Alves**  
Ingeniero en Informática  
