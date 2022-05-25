<template>
  <!-- 평점 -->
  <form @submit.prevent="onSubmit">
    <label for="rating">평점을 입력하세요</label>
    <input v-model="content" type="number" id="rating" min="1" max="9" required>
    <button>평점입력</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingListForm',

  data() {
    return {
      content: null
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createRating']),
    onSubmit() {
      this.createRating({ moviePk: this.movie.id, rate: this.content })
    }
  },
}
</script>

<style>

</style>