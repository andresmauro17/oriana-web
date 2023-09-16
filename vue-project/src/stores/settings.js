import { defineStore } from 'pinia'
export default defineStore('profile', {
  state: () => ({
    appSettings: {
      STATIC_URL: "/static/",
      MEDIA_URL: "/media/",
    },
  }),
})