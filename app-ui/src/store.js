const store = {
  state: {
    appSettings: {
      STATIC_URL: "/static/",
      MEDIA_URL: "/media/",
    },
  },

  mutations: {
    setAppSettings(state, payload = {}) {
      state.appSettings = payload;
    },
  },
};

export default store;
