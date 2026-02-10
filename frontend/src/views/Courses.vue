<!-- views/Courses.vue -->
<template>
  <div class="courses">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Courses</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-2">
            <aside class="menu">
              <p class="menu-label">Categories</p>
              <ul class="menu-list">
                <li><a href="#" class="is-active">All Courses</a></li>
                <li><a href="#">Programming</a></li>
                <li><a href="#">Design</a></li>
                <li><a href="#">UX</a></li>
              </ul>
            </aside>
          </div>

          <div class="column is-10">
            <div class="columns is-multiline">

              <div 
                class="column is-4"
                v-for="course in courses"
                v-bind:key="course.id"
              >
                <div class="card">
                  <div class="card-image">
                    <figure class="image is-4by3">
                      <img
                        src="https://placehold.co/1280x960"
                        alt="Placeholder Image"
                      />
                    </figure>
                  </div>
                  <div class="class-content">
                    <div class="media">
                      <div class="media-content">
                        <p class="is-size-5">{{ course.title }}</p>
                      </div>
                    </div>
                    <div class="content">
                      <p>{{course.short_description}}</p>
                      <a href="#">More</a>
                    </div>
                  </div>
                </div>
              </div>

              <div class="column is-12">
                <nav class="pagination">
                    <a href="#" class="pagination-previous">Previous</a>
                    <a href="#" class="pagination-next">Next</a>
                    <ul class="pagination-list">
                        <li>
                            <a href="#" class="pagination-link is-current">1</a>
                        </li>
                        <li>
                            <a href="#" class="pagination-link">2</a>
                        </li>
                        <li>
                            <a href="#" class="pagination-link">3</a>
                        </li>
                    </ul>
                </nav>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      courses:[]
    }
  },
  mounted(){
    console.log('mounted')
    axios
      .get('/api/v1/courses/')
      .then(response => {
        console.log(response.data)
        this.courses = response.data
      })
  }

}
</script>