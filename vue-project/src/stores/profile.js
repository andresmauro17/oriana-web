import { defineStore } from 'pinia'
import userservices from "@/services/userservices.js"
export default defineStore('profile', {
  state: () => ({
    currentuser:{},
    organizations:[],
    current_organization:{},
    sites:[]
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
        const allSites = this.organizations.flatMap(org => org.sites);
        this.sites = allSites;
        // console.log(this.sites);
        if(this.currentuser.current_organization){
          this.current_organization = this.organizations.filter((or)=>or.id==this.currentuser.current_organization)[0];
        }
      })
    }
  }
})