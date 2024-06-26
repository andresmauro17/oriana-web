const sensorDataChartOptions = {
  title: {
    text: 'Temperature'
  },
  tooltip: {
    trigger: 'axis'
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
    type: 'category',
    boundaryGap: false,
    data: []
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
      data: [10, 11, 13, 11, 12, 12, 9],
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