<template>
  <!-- 평점 목록 -->
  <div class="row g-3 align-items-center">
    <form @submit.prevent="onSubmit">
      <div class="col-auto">
        <label
        style="font-family:GmarketSansMedium;"
        class="form-label" for="rating">* 1~10점 사이의 평점을 등록하세요 </label>
      </div>
      <div class="col-auto" style="margin-left:840px">
        <input class="form-control" v-model="content" type="number" id="rating" min="1" max="9" required>
      </div>
      <div class="col-auto">
        <button class="mt-3 mx-1 btn btn-sm btn-outline-secondary waves-effect">평점 등록</button>
      </div>
    </form>
  </div>
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