
     function drawChartMemory() {
        var data = google.visualization.arrayToDataTable([
          ['Memory', 'Size in G'],
          ['Used',     getValue("ctrl_mem_used")],
          ['Free',     getValue("ctrl_mem_free")]
          
        ]);

        var options = {
          title: 'Main Memory'
        };

        var chart = new google.visualization.PieChart(document.getElementById('mem_chart'));

        chart.draw(data, options);
      }

      function drawChartSwap() {
        var data = google.visualization.arrayToDataTable([
          ['Memory', 'Size in G'],
          ['Used',     getValue("ctrl_swap_used")],
          ['Free',     getValue("ctrl_swap_free")]
          
        ]);

        var options = {
          title: 'Swap Memory'
        };

        var chart = new google.visualization.PieChart(document.getElementById('swap_chart'));

        chart.draw(data, options);
      }

  function drawChartLoadAVG() {
      var data = google.visualization.arrayToDataTable([
        ['Year', 'Visitations', { role: 'style' } ],
        ['1MIN', getValueScalar("ctrl_loadavg_1m"), 'color: gray'],
        ['5MIN', getValueScalar("ctrl_loadavg_5m"), 'stroke-color: #703593; stroke-width: 4; fill-color: #C5A5CF'],
        ['15MIN', getValueScalar("ctrl_loadavg_15m"), 'stroke-color: #871B47; stroke-opacity: 0.6; stroke-width: 8; fill-color: #BC5679; fill-opacity: 0.2']
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        title: "Host average load",
        width: 400,
        height: 200,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.ColumnChart(document.getElementById("loadavg_chart"));
      chart.draw(view, options);
  }