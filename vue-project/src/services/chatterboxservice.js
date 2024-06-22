
import * as mqtt from 'mqtt/dist/mqtt.min'
const HOST = import.meta.env.VITE_WEBSOCKET_HOST
const PORT = import.meta.env.VITE_WEBSOCKET_PORT
const USERNAME = import.meta.env.VITE_WEBSOCKET_USERNAME
const PASSWORD = import.meta.env.VITE_WEBSOCKET_PASSWORD
const ChatterBoxService = {};

ChatterBoxService.startMqttClient = async function () {
  console.log("ChatterBoxService.startMqttClientttt")
  console.log("HOST:", HOST)
  console.log("PORT:", PORT)
  console.log("USERNAME:", USERNAME)
  console.log("PASSWORD", PASSWORD)
  console.log("---------------------------------")
  const options ={
    host:HOST,
    port:PORT,
    endpoint:"/mqtt",
    clean:false,
    connectTimeout: 5000,
    reconnectPeriod:5000,

    clientId: `web_andresmauro17_${Math.floor(Math.random() * 1000000 + 1)}`,
    username: USERNAME,
    password: PASSWORD
  }
  
  const connectUrl = `${options.host}:${options.port}${options.endpoint}`
  let client = {}
  try {
    client = await mqtt.connect(connectUrl, options);
    console.log("se conecto:",client)
  } catch (error) {
    console.log("error conectandose a wss server:: ")
    console.log(error);
  }
  return client;
};


export default ChatterBoxService;
