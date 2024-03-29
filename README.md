# Grafana

Examples used to prepare the [Grafana course](https://pro.codely.com/library/grafana-203964/521119/about/).

## ⚒️️ Requirements

- Docker
- Docker Compose

## 🕵️ Project structure

This repository contains a directory with all the resources (`docker-compose.yml`, configuration, provisioning files,
etc.) for every lesson that required a specific set up of Grafana and any of the other tools of the LGTM stack.

*NOTE: Not all the course lessons contain practical examples that can be reproduced locally, but some are an overview
of some theoretical concepts and some just use an external instance, like [play.grafana.org](https://play.grafana.org/).*

**Index**

1. 🚀 Descubre todo el potencial de Grafana

    1.1. ⚡️ Grafana en menos de 10 minutos: Explicado!

    1.2. 🖲️ Funcionalidades de Grafana que has de conocer

2. 🛠️ Crea tu Dashboard de desarrollo

   [2.1. 📊 Crea tu primer panel: Data sources e integración con GitHub](./2-your-dashboard-for-development)

   [2.2. 👌 Mejora el panel aplicando buenas prácticas](./2-your-dashboard-for-development)

   [2.3. ♠️ Utiliza los paneles de tu data source](./2-your-dashboard-for-development)

3. 👁️‍🗨️ Monitoriza tu aplicación utilizando Prometheus y Loki

   [3.1. 👀 Monitoriza una aplicación fullstack: Frontend & Backend](./3-fullstack-e2e-web-shop-o11y)

   [3.2. 🪬 Observabilidad para monitorear Loki](./3-fullstack-e2e-web-shop-o11y)

   [3.3. 🦬 Observabilidad para monitorear Prometheus](./3-fullstack-e2e-web-shop-o11y)

4. 🐳 Métricas de negocio y plataforma utilizando SQL

   [4.1. 🐋 Monitoriza datos SQL con Grafana](./4-monitor-your-sql-db)

   [4.2. 👁️ Observa el estado de tu base de datos con Grafana](./4-monitor-your-sql-db)

   [4.3. 🎩 Haz que una migración del legacy sea un éxito](./4-monitor-your-sql-db)

5. 🚨 Configura alertas en Grafana

   5.1. 🔔 Por qué centralizar las alertas en Grafana

   [5.2. ⚙️ Configura tus alertas en Grafana](./5-grafana-alerts)

   [5.3. 🎨 Personaliza las plantillas de las alertas](./5-grafana-alerts)

6. 📟 Grafana OnCall

   6.1. ☎️ Por qué utilizar Grafana OnCall para gestionar tus guardias

   [6.2. 📞 Gestiona tus guardias utilizando Grafana OnCall](./6-grafana-oncall)

7. 🪧 Cómo diseñar el panel ideal

   7.1. 🔝 Crea un dashboard perfecto en Grafana

   7.2. 👓 Estrategias de observabilidad

8. 🔮 El futuro de Grafana

   [8.1. 🦄 El futuro de la Observabilidad es Grafana as Code](./8-1-grafana-as-code)

   [8.2. 🪄 El futuro (ya presente) de Grafana](./8-2-grafana-future)

*NOTE: Some of the examples present on this repository are attached as Git Submodules, so you can run
`git submodule init` and `git submodule update` to clone the entire repository with them.*
