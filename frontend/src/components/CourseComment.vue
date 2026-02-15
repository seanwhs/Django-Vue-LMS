<template>
  <article class="media box">
    <div class="media-content">
      <div class="content">
        <p>
          <strong class="mr-4">{{ comment.name }}</strong>
          <small class = 'has-text-grey'>{{ comment.created_at }} </small><br />
          {{ comment.content }}
        </p>
      </div>
    </div>
  </article>
</template>

<script>
export default {
  props: ["comment"],
};
</script>
