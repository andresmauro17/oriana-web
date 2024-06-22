import { defineStore } from 'pinia'
import userservices from "@/services/userservices.js"
export default defineStore('profile', {
  state: () => ({
    currentuser:{},
    organizations:[],
    current_organization:{}
  }),
  actions:{
    getCurrentUser(){
      userservices.getCurrentUser().then((res)=>{
        this.currentuser = res.data
      })
    },
    getOrganizations(){
      userservices.getOrganizations().then((res)=>{
        this.organizations = res.data
        if(this.currentuser.current_organization){
          this.current_organization = this.organizations.filter((or)=>or.id==this.currentuser.current_organization)[0];
        }
      })
    }
  }
})