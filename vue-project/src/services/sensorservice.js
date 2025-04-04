import { api } from "@/api/index.js"
const SensorService = {}

SensorService.getDashboardSensors = function () {
  return api.get(`/dashboard/sensors`).then((res)=>res);
}

SensorService.getSensorData = function (sensor_id, legacy, from=null, to=null, isHourly=false, time1=null, time2=null) {
  let endpoint = legacy?'sensorslegacy':'sensors';
  if(from && to){
    endpoint = `/${endpoint}/${sensor_id}/data?from=${from}&to=${to}`
  }else{
    return api.get(`/${endpoint}/${sensor_id}/data?`).then((res)=>res);
  }

  if(isHourly){
    endpoint =`${endpoint}&hourly=true`;
  }

  if(time1){
    endpoint =`${endpoint}&time1=${time1}`;
  }

  if(time2){
    endpoint =`${endpoint}&time2=${time2}`;
  }
  console.log("endpoint", endpoint);
  return api.get(endpoint).then((res)=>res);
}

SensorService.getSensorCertificates = function (sensor_id, legacy) {
  const endpoint = legacy?'sensorslegacy':'sensors';
  return api.get(`/${endpoint}/${sensor_id}/certificates`).then((res)=>res);
}

SensorService.getSensorDataCsv = function (sensor_id, legacy, from=null, to=null) {
  const endpoint = legacy?'sensorslegacy':'sensors';
  return api.get(`/${endpoint}/${sensor_id}/csv-report/?from=${from}&to=${to}`).then((res)=>res);
}

export default SensorService