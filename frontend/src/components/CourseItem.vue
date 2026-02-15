<!-- components/CourseItem.vue -->
<template>
  <div class="card">
    <div class="card-image p-4">
      <figure class="image is-128by128" style="margin: auto">
        <img
          :src="course.get_image"
          alt="Placeholder Image"
          style="object-fit: cover; border-radius: 8px; height: 100%"
        />
      </figure>
    </div>
    <div class="class-content">
      <div class="media">
        <div class="media-content">
          <p class="is-size-6">{{ course.title }}</p>
        </div>
      </div>
      <div class="content is-size-7">
        <p>{{ course.short_description }}</p>
        <router-link
          :to="{ name: 'CourseDetail', params: { slug: course.slug } }"
          >More</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["course"],
};
</script>
