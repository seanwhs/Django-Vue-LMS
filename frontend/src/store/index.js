// store/index.js
import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    user: {
      token: "",
      isAuthenticated: false,
    },
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.user.token = localStorage.getItem("token");
        state.user.isAuthenticated = true;
        // ADD THIS LINE:
        axios.defaults.headers.common["Authorization"] =
          "Token " + state.user.token;
      } else {
        state.user.token = "";
        state.user.isAuthenticated = false;
        axios.defaults.headers.common["Authorization"] = "";
      }
    },
    setToken(state, token) {
      state.user.token = token;
      state.user.isAuthenticated = true;
      localStorage.setItem("token", token); // Store it for persistence
      axios.defaults.headers.common["Authorization"] = "Token " + token; // Set header immediately
    },
    removeToken(state) {
      state.user.token = "";
      state.user.isAuthenticated = false;
      localStorage.removeItem("token"); // Clear it!
      axios.defaults.headers.common["Authorization"] = "";
    },
  },
  actions: {},
  modules: {},
});
