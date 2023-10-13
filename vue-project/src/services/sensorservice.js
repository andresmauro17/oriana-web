import { api } from "@/api/index.js"
const SensorService = {}

SensorService.getDashboardSensors = function (site_id) {
  return api.get(`/dashboard/${site_id}/sensors`).then((res)=>res);
}

SensorService.getSensorData = function (sensor_id, from=null, to=null) {
  if(from && to){
    return api.get(`/sensors/${sensor_id}/data?from=${from}&to=${to}`).then((res)=>res);
  }
  return api.get(`/sensors/${sensor_id}/data`).then((res)=>res);
}

export default SensorService