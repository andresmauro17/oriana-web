import ChatterBoxService from "@/services/ChatterBoxService";

export default {
  namespaced: true,
  state: {
    chatconnection: null,
    messages: {
      messagereceived: [],
      notif: [],
    },
  },
  getters: {
    messagereceivedByChannelId: (state) => (channelId) => {
      // tutorAI Messages
      return state.messages.messagereceived.filter(
        (message) => message.channel === channelId
      );
    },
  },
  mutations: {
    chirp() {
      const apphome = "/tuolw";
      const urls = apphome + "/chatterbox/stairs.wav";
      const snd = new Audio(urls); // buffers automatically when created
      snd.play();
    },
  },
  actions: {
    connect: async ({ state }) => {
      state.chatconnection = ChatterBoxService.connect();
      state.chatconnection.onmessage = function (event) {
        var message = JSON.parse(event.data);
        state.messages[message.command].push(message);
      };
    },
    sendMessage: async ({ state }, payload) => {
      var json = JSON.stringify(payload);
      await state.chatconnection.send(json);
    },
  },
};
