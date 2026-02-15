<!-- views/CourseDetail.vue -->
<template>
  <div>
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

                  <div v-if="activeLesson.lesson_type !== 'quiz'">
                    {{ activeLesson.long_description }}
                  </div>

                  <hr />

                  <template v-if="activeLesson.lesson_type === 'quiz'">
                    <Quiz v-bind:quiz="quiz" />
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
export default {
  components: {
    CourseComment,
    AddComment,
    Quiz
  },
  data() {
    return {
      course_detail: {},
      lessons: [],
      errors: [],
      quiz: {},
      comments: [],
      activeLesson: null,
    };
  },
  async mounted() {
    console.log("mounted");
    const slug = this.$route.params.slug;
    await axios.get(`courses/${slug}/`).then((response) => {
      console.log(response.data);
      this.course_detail = response.data.course_detail;
      this.lessons = response.data.lessons;
    });
    document.title = this.course_detail.title + "| LearnSphere";
  },
  methods: {
    submitComment(comment) {
      this.comments.push(comment);
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson;
      if (lesson.lesson_type === "quiz") {
        this.getQuiz();
      } else {
        this.getComments();
      }
    },
    getQuiz() {
      axios
        .get(
          `courses/${this.course_detail.slug}/${this.activeLesson.slug}/get-quiz/`,
        )
        .then((response) => {
          console.log(response.data);
          this.quiz = response.data;
        });
    },
    getComments() {
      axios
        .get(
          `courses/${this.course_detail.slug}/${this.activeLesson.slug}/get-comments/`,
          this.comment,
        )

        .then((response) => {
          this.comments = response.data;
        });
    },
  },
};
</script>
