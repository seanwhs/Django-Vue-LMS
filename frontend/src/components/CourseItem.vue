<template>
  <div class="card">
    <div class="card-image p-4">
      <figure class="image is-128by128" style="margin: auto">
        <img
          :src="course.get_image"
          alt="Course image"
          style="object-fit: cover; border-radius: 8px; height: 100%"
        />
      </figure>
    </div>

    <div class="card-content p-4">
      <div class="media">
        <div class="media-content">
          <p class="is-size-6"><strong>{{ course.title }}</strong></p>
          
          <p class="is-size-7 has-text-grey" v-if="course.created_by">
            By 
            <router-link :to="{ name: 'Author', params: { id: course.created_by.id }}">
              {{ course.created_by.first_name }} {{ course.created_by.last_name }}
            </router-link>
          </p>
        </div>
      </div>

      <div class="content is-size-7 mt-2">
        <p>{{ course.short_description }}</p>
        <router-link
          :to="{ name: 'CourseDetail', params: { slug: course.slug } }"
          class="has-text-info"
        >More</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["course"],
};
</script>