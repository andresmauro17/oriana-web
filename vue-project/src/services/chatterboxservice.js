
import * as mqtt from 'mqtt/dist/mqtt.min'
const ChatterBoxService = {};

ChatterBoxService.startMqttClient = async function () {
  console.log("ChatterBoxService.startMqttClient")
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
  const subscribeTopic = "sensors/FF3C0E001705/currentdata/"
  const connectUrl = `ws://${options.host}:${options.port}${options.endpoint}`
  let client = {}
  try {
    client = await mqtt.connect(connectUrl, options);
  } catch (error) {
    console.log(error);
  }

  //MQTT CONNECTION SUCCESS
  client.on("connect", () => {
    console.log(client);

    console.log("Connection succeeded!");

    //SDATA SUBSCRIBE
    client.subscribe(subscribeTopic, { qos: 0 }, err => {
      if (err) {
        console.log("Error in DeviceSubscription");
        return;
      }
      console.log("Device subscription Success");
      console.log(subscribeTopic);
    });

  });

  client.on("error", error => {
    console.log("Connection failed", error);
  });

  client.on("reconnect", error => {
    console.log("reconnecting:", error);
    // this.getMqttCredentialsForReconnection();
  });

  client.on("message", (topic, message) => {
    console.log("Message from topic " + topic + " -> ");
    console.log(message.toString());
  });

  return "";
};


export default ChatterBoxService;
