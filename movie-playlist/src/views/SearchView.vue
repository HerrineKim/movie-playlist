<template>
  <div>
    <h2>영화 검색창</h2>
    <input v-model="keyword"
    @keyup.enter="onInputKeyword"
    type="text"
    placeholder="영화를 검색해주세요."
    >
    <div>
      <p v-for="movie in search" :key="movie">
        <router-link :to="{ name: 'movieDetail', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link>
      </p>
    </div>
    <div v-for="recommendationMovie in recommendationMovies" :key="recommendationMovie.poster_path">
      <p>
        {{ recommendationMovie.title }}
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'SearchView',
  components: {

  },
  data() {
    return {
      keyword: '',
      userPk: ''
    }
  },
  computed: {
    ...mapGetters(['search', 'currentUser', 'recommendationMovies'])
  },
  methods: {
    onInputKeyword() {
      const movieName = this.keyword
      this.$store.dispatch('search', movieName)
      // console.log(movieName)
      // console.log(this.keyword)
      // console.log(typeof movieName)
    },
    ...mapActions(['recommendation'])
  },
  created() {
    this.userPk = this.currentUser.pk
    this.recommendation({ userPk: this.userPk })
    console.log(this.userPk)
  }
}
</script>

<style>

</style>