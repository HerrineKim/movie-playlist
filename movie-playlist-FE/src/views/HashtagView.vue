<template>
  <div class="hashtag">
    <nav-bar></nav-bar>
    <hashtag-movies></hashtag-movies>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import HashtagMovies from "@/components/organisms/Hashtag/HashtagMovies.vue"

export default {
  name: 'HashtagView',
  components: {
    HashtagMovies, NavBar
  }
}
</script>

<style>

</style>