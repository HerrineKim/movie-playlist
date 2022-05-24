<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <div>
      <div v-if="is_liked">
        <i class="fas fa-heart"
        @click="likeMovie"
        >
        </i>
      </div>
      <div v-else>
          <i class="far fa-heart"
          @click="likeMovie"
          >
          </i>
      </div>
    </div>
    <!-- <div>
      평점
    </div> -->
    <div>
      <p>{{ rate }}</p>
      <form @submit.prevent="createRating">
        <label for="rating">평점을 입력하세요</label>
        <input v-model="rate" type="text" id="rating">
      </form>
      <button>평점 삭제</button>
    </div>
    <div>
      <p v-for="sim in similarMovies" :key="sim">
        {{ sim.title }}
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieDetailView',
  components: {
    
  },
  data() {
    return {
      is_liked: false,
      score: null,
      newRate: {
        moviePk: '',
        rate: null
      }
    }
  },
  computed: {
    ...mapGetters(['movie', 'similarMovies']),
    // moviePosterUrl() {
    //   return ``
    // }
  },
  methods: {
    ...mapActions(['similar', 'fetchMovie', 'create_rating']),
    likeMovie() {
      const moviePk = this.moviePk
      this.$store.dispatch('movieLike', moviePk)
      this.is_liked = !this.is_liked
    },
    createRating() {
      const payload = this.newRate
      this.create_rating(payload)
    },
  },
  created() {
    this.moviePk = this.$route.params.moviePk
    // console.log(this.moviePk)
    this.fetchMovie({ moviePk: this.moviePk })
    // console.log(this.moviePk)
    this.similar({ moviePk: this.moviePk })
  }
}
</script>

<style>

</style>