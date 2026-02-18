<!-- views/CourseDetail.vue -->
<template>
  <div>
    <div class="courses">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course_detail.title }}</h1>
        <router-link
          :to="{name: 'Author', params: {id: course_detail.created_by.id}}"
          class = 'subtitle' 
          v-if="course_detail.created_by"
        >
          By {{ course_detail.created_by.first_name }}
          {{ course_detail.created_by.last_name }}
        </router-link>
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

                  <span
                    class="tag is-warning"
                    v-if="activity.status == 'started'"
                    @click="markAsDone"
                    >Started (Mark as Done)</span
                  >
                  <span class="tag is-success" v-else>Done</span>

                  <hr />

                  <div v-if="activeLesson.lesson_type !== 'quiz'">
                    {{ activeLesson.long_description }}
                  </div>

                  <hr />

                  <template v-if="activeLesson.lesson_type === 'quiz'">
                    <Quiz v-bind:quiz="quiz" />
                  </template>

                  <template v-if="activeLesson.lesson_type === 'video'">
                    <Video v-bind:youtube_id="activeLesson.youtube_id" />
                  </template>

                  <template v-if="activeLesson.lesson_type === 'article'">
                    <CourseComment
                      v-for="comment in comments"
                      v-bind:key="comment.id"
                      v-bind:comment="comment"
                    />

                    <AddComment
                      v-bind:course_detail="course_detail"
                      v-bind:activeLesson="activeLesson"
                      v-on:submitComment="submitComment"
                    />
                  </template>
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
  </div>
</template>

<script>
import axios from "axios";
import CourseComment from "@/components/CourseComment";
import AddComment from "@/components/AddComment";
import Quiz from "@/components/Quiz";
import Video from "@/components/Video";

export default {
  components: {
    CourseComment,
    AddComment,
    Quiz,
    Video,
  },
  data() {
    return {
      course_detail: {
        title: "",
        created_by: null,
        slug: ""
      },
      lessons: [],
      errors: [],
      quiz: {},
      comments: [],
      activeLesson: null,
      activity: {},
    };
  },
  async mounted() {
    const slug = this.$route.params.slug;
    try {
      const response = await axios.get(`courses/${slug}/`);
      this.course_detail = response.data.course_detail;
      this.lessons = response.data.lessons;
      document.title = this.course_detail.title + " | LearnSphere";
    } catch (error) {
      console.error("Error fetching course details:", error);
    }
  },
  methods: {
    submitComment(comment) {
      this.comments.push(comment);
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson;

      // Authenticated actions only
      if (this.$store.state.user.isAuthenticated) {
        if (lesson.lesson_type === "quiz") {
          this.getQuiz();
        } else {
          this.getComments();
        }
        this.trackStarted();
      }
    },
    trackStarted() {
      if (!this.$store.state.user.isAuthenticated) return;

      axios
        .post(`activities/track_started/${this.$route.params.slug}/${this.activeLesson.slug}/`)
        .then((response) => {
          this.activity = response.data;
        })
        .catch(err => console.log("Tracking error:", err));
    },
    markAsDone() {
      if (!this.$store.state.user.isAuthenticated) return;

      axios
        .post(`activities/mark_as_done/${this.$route.params.slug}/${this.activeLesson.slug}/`)
        .then((response) => {
          this.activity = response.data;
        })
        .catch(err => console.log("Mark as done error:", err));
    },
    getQuiz() {
      if (!this.$store.state.user.isAuthenticated) return;

      axios
        .get(`courses/${this.course_detail.slug}/${this.activeLesson.slug}/get-quiz/`)
        .then((response) => {
          this.quiz = response.data;
        })
        .catch(err => console.error("Quiz fetch error:", err));
    },
    getComments() {
      if (!this.$store.state.user.isAuthenticated) return;

      axios
        .get(`courses/${this.course_detail.slug}/${this.activeLesson.slug}/get-comments/`)
        .then((response) => {
          this.comments = response.data;
        })
        .catch(err => console.error("Comments fetch error:", err));
    },
  },
};
</script>
