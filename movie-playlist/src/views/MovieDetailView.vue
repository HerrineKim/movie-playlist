<template>
  <div>
    <nav-bar></nav-bar>
    <!-- 영화 detail -->
    <div>
      <h2>{{ movie.title }}</h2>
      <img
            class="card-img-top"
            :src="'https://image.tmdb.org/t/p/w300/' + movie.poster_path" alt=""
            >
    </div>

    <!-- 좋아요 -->
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

    <!-- 평점 -->
    <div>
      <rating-list :ratings="movie.ratings"></rating-list>
    </div>
    
    <div>
      <p v-for="sim in similarMovies" :key="sim">
        {{ sim.title }}
      </p>
    </div>
  </div>
</template>

<script>
import RatingList from "@/components/organisms/MovieDetail/RatingList.vue"
import NavBar from '@/components/templates/NavBar.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieDetailView',
  components: {
    RatingList, NavBar
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

  },
  methods: {
    ...mapActions(['similar', 'fetchMovie']),
    likeMovie() {
      const moviePk = this.moviePk
      this.$store.dispatch('movieLike', moviePk)
      this.is_liked = !this.is_liked
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