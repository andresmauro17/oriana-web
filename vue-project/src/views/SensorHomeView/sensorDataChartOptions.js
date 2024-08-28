const sensorDataChartOptions = {
  title: {
    text: 'Temperature'
  },
  tooltip: {
    trigger: 'axis',
    formatter: function (params) {
      const date = new Date(params[0].value[0]);
      return `${date.toLocaleString()}: ${params[0].value[1]} °C`;
      // return `${date.toLocaleString()}: ${params[0].value[1]} °C <br> some report description TODO`;
    }
  },
  legend: {},
  toolbox: {
    show: true,
    feature: {
      dataZoom: [
        {
          type: 'slider',
          start: 0,
          end: 100,
          showDetail: false,
          zoomLock: true
        },
        {
          type: 'inside',
          start: 0,
          end: 100,
          zoomLock: true
        }
      ],
      dataView: { 
        readOnly: false,
        title: 'Vista de Datos'
      },
      restore: {title: 'Restaurar'},
      saveAsImage: {title: 'Guardar Imagen'}
    }
  },
  xAxis: {
    type: 'time',  // Change to time axis
    boundaryGap: false,
  },
   yAxis: {
    type: 'value',
    min:()=>{},// Adjust the min value
    max:()=>{},// Adjust the max value
    axisLabel: {
      formatter: '{value} °C'
    }
  },
  series: [
    {
      name: 'Valor',
      type: 'line',
      data: [], // This will be set dynamically
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ yAxis: 8, name: 'Threshold', lineStyle: { color: 'red' } }, { yAxis: 2, name: 'Threshold', lineStyle: { color: 'blue' } } ]
      }
    },
  ]
};

export default sensorDataChartOptions;