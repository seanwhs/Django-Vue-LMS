<!-- views/CourseDetail.vue -->
<template>
  <div class="courses">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course_detail.title }}</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h2>Table of Contents</h2>
            <ul>
              <li v-for="lesson in lessons" v-bind:key="lesson.id">
                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
              </li>
            </ul>
          </div>
          <div class="column is-10">
            <template v-if="$store.state.user.isAuthenticated">
              <template v-if="activeLesson">
                <h2>{{ activeLesson.title }}</h2>
                {{ activeLesson.long_description }}

                <hr />

                <article
                  class="media box"
                  v-for="comment in comments"
                  v-bind:key="comment.id"
                >
                  <div class="media-content">
                    <div class="content">
                      <p>
                        <strong>{{ comment.name }}</strong
                        >{{ comment.created_at }} <br />
                        {{ comment.content }}
                      </p>
                    </div>
                  </div>
                </article>

                <form v-on:submit.prevent="submitComment()">
                  <div class="field">
                    <label class="label">Name</label>
                    <div class="control">
                      <input type="text" class="input" v-model="comment.name" />
                    </div>
                  </div>

                  <div class="field">
                    <label class="label">Content</label>
                    <div class="control">
                      <textarea
                        class="textarea"
                        v-model="comment.content"
                      ></textarea>
                    </div>
                  </div>

                  <div
                    class="notification is-danger"
                    v-for="error in errors"
                    v-bind:key="error"
                  >
                    {{ error }}
                  </div>

                  <div class="field">
                    <div class="control">
                      <button class="button is-link">Submit</button>
                    </div>
                  </div>
                </form>
              </template>
              <template v-else>
                <h2>Introduction</h2>
                {{ course_detail.long_description }}
              </template>
            </template>
            <template v-else>
              <h2>Restricted Access</h2>
              <p>You need to have an account to continue</p>
            </template>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      course_detail: {},
      lessons: [],
      errors: [],
      comments: [],
      activeLesson: null,
      comment: {
        name: "",
        content: "",
      },
    };
  },
  async mounted() {
    console.log("mounted");
    const slug = this.$route.params.slug;
    await axios.get(`/api/v1/courses/${slug}/`).then((response) => {
      console.log(response.data);
      this.course_detail = response.data.course_detail;
      this.lessons = response.data.lessons;
    });
    document.title = this.course_detail.title + '| LearnSphere'
  },
  methods: {
    submitComment() {
      console.log("Submit Comment");

      this.errors = [];

      if (this.comment.name === "") {
        this.errors.push("Name is required!");
      }

      if (this.comment.content === "") {
        this.errors.push("Content is required!");
      }

      if (!this.errors.length) {
        axios
          .post(
            `/api/v1/courses/${this.course_detail.slug}/${this.activeLesson.slug}/`,
            this.comment,
          )
          .then((response) => {
            this.comments.push(response.data);
            // Reset form on sccessful submission
            this.comment.name = "";
            this.comment.content = "";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson;
      this.getComments();
    },
    getComments() {
      axios
        .get(
          `/api/v1/courses/${this.course_detail.slug}/${this.activeLesson.slug}/get-comments/`,
          this.comment,
        )

        .then((response) => {
          this.comments = response.data;
        });
    },
  },
};
</script>
