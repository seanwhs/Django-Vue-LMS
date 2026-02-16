<!-- views/dashboard/MyAccount.vue -->
<template>
  <div class="about">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">My Account</h1>
      </div>
    </div>

    <section class="section">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="subtitle is-size-3">Your Active Courses</h2>
        </div>
        <div
          class="column is-4"
          v-for="course in courses"
          v-bind:key="course_id"
        >
          <CourseItem :course="course" />
        </div>
      </div>
      <hr />
      <button @click="logout()" class="button is-danger">Log Out</button>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import CourseItem from "@/components/CourseItem.vue";

export default {
  data() {
    return {
      courses: [],
    };
  },
  components: {
    CourseItem,
  },
  mounted() {
    document.title = "My Account | LearnSphere";

    axios.get("activities/get_active_courses/").then((response) => {
      console.log(response.data);
      this.courses = response.data;
    });
  },
  methods: {
    async logout() {
      const token = localStorage.getItem("token");
      // Ensure the token exists before trying to tell the server
      if (token) {
        const config = { headers: { Authorization: `Token ${token}` } };
        try {
          await axios.post("token/logout/", {}, config);
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
