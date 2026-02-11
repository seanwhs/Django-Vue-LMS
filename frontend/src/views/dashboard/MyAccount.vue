<!-- views/dashboard/MyAccount.vue -->
<template>
  <div class="about">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">My Account</h1>
      </div>
    </div>

    <section class="section">
      <button @click="logout()" class="button is-danger">Log Out</button>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    async logout() {
      const token = localStorage.getItem("token");
      // Ensure the token exists before trying to tell the server
      if (token) {
        const config = { headers: { Authorization: `Token ${token}` } };
        try {
          await axios.post("/api/v1/token/logout/", {}, config);
        } catch (error) {
          console.log("Server session already gone.");
        }
      }

      // Always clear local state
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>
