# 📊 Procurement Analytics Data Engineering Project

Este proyecto demuestra un pipeline de ingeniería de datos completo para analizar el ciclo de compras (SP, OC, entrega) utilizando herramientas modernas como BigQuery, Terraform, Airflow y Dataform.

## 🛠 Tecnologías utilizadas

- Google Cloud Platform (BigQuery, Cloud Functions, Cloud Storage)
- Terraform
- Dataform
- Apache Airflow (Cloud Composer)
- Power BI / Looker Studio

## 🔄 Flujo de datos

1. **Ingesta**: Archivos CSV simulados de SAP (`EBAN`, `EKPO`, `EKET`) se cargan a Cloud Storage.
2. **Procesamiento**: Cloud Function sube los datos a BigQuery.
3. **Modelado**: Dataform transforma y modela los datos para analítica.
4. **Orquestación**: Airflow ejecuta el pipeline de forma automatizada.
5. **Visualización**: Dashboard en Power BI.

## 📁 Estructura

Ver [Estructura del Proyecto](#).

## 🚀 ¿Cómo ejecutarlo?

1. Crea un proyecto GCP y habilita BigQuery, Cloud Storage y Cloud Functions.
2. Despliega la infraestructura con Terraform.
3. Sube archivos de datos a GCS.
4. Ejecuta los DAGs de Airflow.
5. Visualiza los resultados en Power BI o Looker Studio.

## 📊 Ejemplo de KPIs

- Valor estimado vs real por proveedor
- SP/OC por estado
- Tiempo promedio del ciclo de compra
- Alertas por desviación presupuestaria

---

**Autor**: [Tu Nombre]  
**Licencia**: MIT
