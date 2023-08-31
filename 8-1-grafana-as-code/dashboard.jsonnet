local g = import 'github.com/grafana/grafonnet/gen/grafonnet-latest/main.libsonnet';

g.dashboard.new('Node Exporter')
+ g.dashboard.withDescription('Dashboard for Node Exporter')
+ g.dashboard.withPanels([
  g.panel.timeSeries.new('Total memory (GB)')
  + g.panel.timeSeries.queryOptions.withTargets([
    g.query.prometheus.new(
      'Prometheus',
      'node_memory_MemTotal_bytes{instance="node-exporter:9100"}',
    ),
  ])
  + g.panel.timeSeries.standardOptions.withUnit('decbytes')
  + g.panel.timeSeries.gridPos.withW(24)
  + g.panel.timeSeries.gridPos.withH(8),
])

