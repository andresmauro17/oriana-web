import { defineStore } from 'pinia'
import ChatterBoxService from "@/services/chatterboxservice.js"
export default defineStore('chatterbox', {
  state: () => ({
    client: {},
    isConnected: false,
    messages:{},
    sensorsuscribed:[]
  }),
  actions:{
    async startMqttClient(sensorid){
      console.log("startMqttClient")

      if(!this.isConnected){
        console.log("linea15")
        this.client = await ChatterBoxService.startMqttClient();
      }
      await this.subscribeTo(sensorid);
      this.listenOnConnect();
      this.listenOnError();
      this.listenOnReconnect();
      this.listenOnMessage();
    },
    async subscribeTo(sensorid){
      const subscribeTopic = `sensors/${sensorid}/currentdata/`
      await this.client.subscribe(subscribeTopic, { qos: 0 }, err => {
        if (err) {
          console.log("Error in DeviceSubscription");
          return false;
        }
        console.log("Device subscription Success", subscribeTopic);
        this.sensorsuscribed.push(sensorid)
        this.messages[sensorid] = []

      });
    },
    listenOnConnect(){
      //MQTT CONNECTION SUCCESS
      this.client.on("connect", () => {
        console.log("OnConnect succeeded!");
        this.isConnected = true;
      });
    },
    listenOnError(){
      this.client.on("error", error => {
        console.log("OneError Connection failed", error);
      });
    },
    listenOnReconnect(){
      this.client.on("reconnect", error => {
        console.log("OnReconnect reconnecting:", error);
      });
    },
    listenOnMessage(){
      this.client.on("message", (topic, message) => {
        console.log("Message from topic " + topic + " -> ");
        console.log(message.toString());
        let topicsplited = topic.split("/")
        // console.log(topicsplited)
        let sensoruniqueid = topicsplited[1]
        message = JSON.parse(message)
        this.messages[sensoruniqueid].push(message.data)
        // console.log(this.messages);
      });
    }
  }
})