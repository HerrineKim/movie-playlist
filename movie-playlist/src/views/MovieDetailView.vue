<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <!-- 영화 detail -->
      <h1>{{ movie.title }}</h1>

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
      
      <!-- 비슷한 영화 -->
      <div class="row mt-5">
          <p style="font-family:MapoGoldenPier; text-align:left">
            이 영화를 재미있게 봤다면?
          </p>
          <div v-for="sim in similarMovies" :key="sim.poster_path" 
          class="col-12 col-sm-4 col-md-3"
          >
            <div class="card border mb-3">
              <router-link
              :to="{ name: 'movieDetail', params: { moviePk: sim.pk } }"
              >
                <img
                class="card-img-top"
                :src="'https://image.tmdb.org/t/p/w300/' + sim.poster_path" alt=""
                >
              </router-link>
              <div class="card-body">
                <hr>
                <h5 class="card-title">{{ sim.title }}</h5>
              </div>
            </div>
          </div>
        </div>

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