<template>
  <div class="courses">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title" v-if="created_by.first_name">
          {{ created_by.first_name }} {{ created_by.last_name }}
        </h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div
            class="column is-4"
            v-for="course in courses"
            v-bind:key="course.id"
          >
            <CourseItem :course="course" />
          </div>
          </div>
      </div>
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
      created_by: {} 
    };
  },
  components: {
    CourseItem,
  },
  mounted() {
    this.get_courses();
  },
  methods: {
    get_courses() {
      const id = this.$route.params.id;
      axios.get(`courses/get_author_courses/${id}/`).then((response) => {
        this.created_by = response.data.created_by;
        
        const isAuth = this.$store.state.user.isAuthenticated;

        this.courses = response.data.courses.map((course) => {
          return isAuth
            ? course
            : {
                id: course.id,
                title: course.title,
                slug: course.slug,
                get_image: course.get_image,
              };
        });
        
        document.title = `${this.created_by.first_name} | LearnSphere`;
      });
    },
  },
};
</script>