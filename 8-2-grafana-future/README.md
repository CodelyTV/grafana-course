# Prep

1. Run the following commands:

   ```
   # make demo
   cd /scenes/packages/scenes-app
   docker-compose up -d
   ```
   
# Script

1. Introduce Grafana Scenes: https://grafana.github.io/scenes/
2. Recommend to watch the GrafanaCON session: https://grafana.com/about/events/grafanacon/2023/session/dynamic-dashboards-with-grafana-scenes/
3. Demo time: http://localhost:3001/a/grafana-scenes-app
4. Split into services:
   1. Introduce grafana/dskit (based on Google Guava): https://github.com/grafana/dskit/tree/main/services
      1. Recently introduced "Service Weaver"
      2. Used by L?TM, now it's turn to G
   2. Show a example PR: https://github.com/grafana/grafana/pull/64062
