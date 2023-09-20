import { api } from "@/api/index.js"
const SensorService = {}

SensorService.getDashboardSensors = function (site_id) {
  return api.get(`/dashboard/${site_id}/sensors`).then((res)=>res);
}

export default SensorService