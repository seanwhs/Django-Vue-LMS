<!-- views/dashboard/CreateCourse.vue -->
<template>
  <div class="about">
    <div class="hero is-info is-medium">
      <div class="hero-body">
        <h1 class="title">Create Course</h1>
        <div class="mb-6 px-6 py-4 has-background-grey-lighter">
          <h2 class="subtitle is-size-3">Meta Information</h2>
          <div class="field">
            <label>Title</label>
            <input class="input" type="text" v-model="form.title" />
          </div>

          <div class="field">
            <label>Short Description</label>
            <textarea
              class="textarea"
              v-model="form.short_description"
            ></textarea>
          </div>

          <div class="field">
            <label>Long Description</label>
            <textarea
              class="textarea"
              v-model="form.long_description"
            ></textarea>
          </div>

          <div class="field">
            <div class="select is-multiple">
              <select multiple size="10" v-model="form.categories">
                <option
                  v-for="category in categories"
                  v-bind:key="category.id"
                  v-bind:value="category.id"
                >
                  {{ category.title }}
                </option>
              </select>
            </div>
          </div>
        </div>
        <div class="mb-6 px-6 py-4 has-background-grey-lighter">
          <h2 class="subtitle is-size-3">Lessons</h2>

          <div
            v-for="(lesson, index) in form.lessons"
            :key="index"
            class="mb-4"
          >
            <h3 class="subtitle is-size-6">Lesson</h3>

            <div class="field">
              <label>Title</label>
              <input
                class="input"
                type="text"
                v-model="lesson.title"
                :name="`form.lessons[${index}][title]`"
                />
              </div>
              
              <div class="field">
                <label>Short Description</label>
                <textarea
                class="textarea"
                v-model="lesson.short_description"
                :name="`form.lessons[${index}][short_description]`"
                ></textarea>
              </div>
              
              <div class="field">
                <label>Long Description</label>
                <textarea
                class="textarea"
                v-model="lesson.long_description"
                :name="`form.lessons[${index}][long_description]`"
              ></textarea>
            </div>

            <hr />
          </div>

          <button class="button is-primary" @click="addLesson">
            Add Lesson
          </button>
        </div>

        <div class="field buttons">
          <button class="button is-success" @click="submitForm('draft')">
            Save as Draft
          </button>
          <button class="button is-info is-dark" @click="submitForm('in_review')">
            Submit for Review
          </button>
        </div>
      </div>
    </div>
    <section class="section"></section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        title: "",
        short_description: "",
        long_description: "",
        categories: [],
        status: "",
        lessons: [],
      },
      categories: [],
    };
  },
  mounted() {
    this.getCategories();
    this.addLesson();
  },
  methods: {
    getCategories() {
      console.log("getCategories");

      axios.get("courses/get_categories/").then((response) => {
        console.log(response.data);
        this.categories = response.data;
      });
    },
    submitForm(status) {
      console.log("submitForm");
      console.log(this.form);

      this.form.status = status;

      axios
        .post("courses/create_course/", this.form)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log("error: ", error);
        });
    },
    addLesson() {
      console.log("add lesson");
      this.form.lessons.push({
        title: "",
        short_description: "",
        long_description: "",
      });
    },
  },
};
</script>
