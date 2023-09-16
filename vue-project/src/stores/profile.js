import { defineStore } from 'pinia'
import userservices from "@/services/userservices.js"
export default defineStore('profile', {
  state: () => ({
    currentuser:{}
  }),
  actions:{
    getCurrentUser(){
      userservices.getCurrentUser().then((res)=>{
        this.currentuser = res.data
      })
    }
  }
})