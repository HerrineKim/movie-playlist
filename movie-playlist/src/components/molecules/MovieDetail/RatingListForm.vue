<template>
  <!-- 평점 -->
  <form @submit.prevent="onSubmit">
    <label for="rating">나의 평점</label>
    <input v-model="content" type="number" id="rating" min="1" max="9" required>
    <button>등록</button>
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