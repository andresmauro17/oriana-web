import { defineStore } from 'pinia'
import ChatterBoxService from "@/services/chatterboxservice.js"
export default defineStore('chatterbox', {
  state: () => ({
  }),
  actions:{
    startMqttClient(){
      console.log("startMqttClient")
      ChatterBoxService.startMqttClient();
    },
  }
})