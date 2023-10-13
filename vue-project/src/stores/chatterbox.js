import { defineStore } from 'pinia'
import ChatterBoxService from "@/services/chatterboxservice.js"
export default defineStore('chatterbox', {
  state: () => ({
    client: {},
    messages:[],
  }),
  actions:{
    async startMqttClient(){
      console.log("startMqttClient")


      this.client = await ChatterBoxService.startMqttClient();
      console.log("client this",this.client)
      const subscribeTopic = "sensors/FF3C0E001705/currentdata/"

      //MQTT CONNECTION SUCCESS
      this.client.on("connect", () => {
        console.log("Connection succeeded!");

        //SDATA SUBSCRIBE
        this.client.subscribe(subscribeTopic, { qos: 0 }, err => {
          if (err) {
            console.log("Error in DeviceSubscription");
            return;
          }
          console.log("Device subscription Success");
          console.log(subscribeTopic);
        });

      });

      this.client.on("error", error => {
        console.log("Connection failed", error);
      });

      this.client.on("reconnect", error => {
        console.log("reconnecting:", error);
      });

      this.client.on("message", (topic, message) => {
        console.log("Message from topic " + topic + " -> ");
        this.messages.push(JSON.parse(message.data))
      });
    },
  }
})