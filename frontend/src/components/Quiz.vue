<!-- components/Quiz.vue -->
<template>
       <h3>{{ quiz.question }}</h3>

                  <template v-for="index in 5" :key="index">
                    <div class="control" v-if="quiz['opt' + index]">
                      <label class="radio">
                        <input
                          type="radio"
                          :value="quiz['opt' + index]"
                          v-model="selectedAnswer"
                        />
                        {{ quiz["opt" + index] }}
                      </label>
                    </div>
                  </template>

                  <div class="control mt-4">
                    <button class="button is-info" @click="submitQuiz">
                      Submit
                    </button>
                  </div>

                  <template v-if="quizResult == 'correct'">
                    <div class="notification is-success mt-4">Correct 👍</div>
                  </template>

                  <template v-if="quizResult == 'incorrect'">
                    <div class="notification is-danger mt-4">
                      Wrong 👎 Please try again!
                    </div>
                  </template>
</template>

<script>
export default {
  props: ["quiz"],
  data() {
    return {
      selectedAnswer: "",
      quizResult: null,
    };
  },
  methods: {
    submitQuiz() {
      this.quizResult = null;
      if (this.selectedAnswer) {
        if (this.selectedAnswer === this.quiz.answer) {
          this.quizResult = "correct";
        } else {
          this.quizResult = "incorrect";
        }
      } else {
        alert("Select Answer");
      }
    },
  },
};
</script>
