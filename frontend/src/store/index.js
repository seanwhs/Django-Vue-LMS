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
// store/index.js

mutations: {
  initializeStore(state) {
    const token = localStorage.getItem("token");
    if (token) {
      state.user.token = token;
      state.user.isAuthenticated = true;
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      state.user.token = "";
      state.user.isAuthenticated = false;
      // Use delete to completely remove the header
      delete axios.defaults.headers.common["Authorization"];
    }
  },
  setToken(state, token) {
    state.user.token = token;
    state.user.isAuthenticated = true;
    localStorage.setItem("token", token);
    axios.defaults.headers.common["Authorization"] = "Token " + token;
  },
  removeToken(state) {
    state.user.token = "";
    state.user.isAuthenticated = false;
    localStorage.removeItem("token");
    // Use delete here as well
    delete axios.defaults.headers.common["Authorization"];
  },
},
  actions: {},
  modules: {},
});
