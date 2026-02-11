<!-- components/Nav.vue -->
<template>
  <nav
    class="navbar is-info"
    role="navigation"
    aria-label="main-navigation"
    style="min-height: 5rem"
  >
    <div class="navbar-brand">
      <router-link
        to="/"
        class="navbar-item is-size-4 has-text-white"
      >
        LearnSphere
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item has-text-white">Home</router-link>
        <router-link to="/about" class="navbar-item has-text-white">About</router-link>
        <router-link to="/courses" class="navbar-item has-text-white">Courses</router-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link
              v-if="isAuthenticated"
              to="/dashboard/my-account"
              class="button is-info has-text-white"
            >
              My Account
            </router-link>

            <template v-else>
              <router-link to="/sign-up" class="button is-primary">
                <strong>Sign Up</strong>
              </router-link>
              <router-link to="/log-in" class="button is-light">
                Log in
              </router-link>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>


<script>
import { defineComponent } from "vue";

export default defineComponent({
  computed: {
    isAuthenticated() {
      return this.$store.state.user.isAuthenticated;
    },
  },
});
</script>
