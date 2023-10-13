
import * as mqtt from 'mqtt/dist/mqtt.min'
const ChatterBoxService = {};

ChatterBoxService.startMqttClient = async function () {
  // console.log("ChatterBoxService.startMqttClient")
  const options ={
    host:"localhost",
    port:8083,
    endpoint:"/mqtt",
    clean:false,
    connectTimeout: 5000,
    reconnectPeriod:5000,

    clientId: `web_andresmauro17_${Math.floor(Math.random() * 1000000 + 1)}`,
    username: "",
    password:""
  }
  
  const connectUrl = `ws://${options.host}:${options.port}${options.endpoint}`
  let client = {}
  try {
    client = await mqtt.connect(connectUrl, options);
  } catch (error) {
    console.log(error);
  }
  return client;
};


export default ChatterBoxService;
