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
    async getCurrentUser() {
      const res = await userservices.getCurrentUser();
      this.currentuser = res.data;
    },
    async getOrganizations() {
      const res = await userservices.getOrganizations();
      this.organizations = res.data;
      const allSites = this.organizations.flatMap(org => org.sites);
      this.sites = allSites;
      // console.log(this.sites);
      if (this.currentuser.current_organization) {
        this.current_organization = this.organizations.filter(or => or.id == this.currentuser.current_organization)[0];
        if(this.current_organization == undefined || !this.current_organization.is_active){
          window.location.href = "/organizations/0/switch/";
        }
      }
    }
  }
})