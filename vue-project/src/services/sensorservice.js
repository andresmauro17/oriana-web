import { api } from "@/api/index.js"
const SensorService = {}

SensorService.getDashboardSensors = function () {
  return api.get(`/dashboard/sensors`).then((res)=>res);
}

SensorService.getSensorData = function (sensor_id, legacy, from=null, to=null) {
  const endpoint = legacy?'sensorslegacy':'sensors';
  if(from && to){
    return api.get(`/${endpoint}/${sensor_id}/data?from=${from}&to=${to}`).then((res)=>res);
  }
  return api.get(`/${endpoint}/${sensor_id}/data`).then((res)=>res);
}

export default SensorService