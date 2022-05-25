<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <div class="container col-5 my-3 text-align:left">  
        <h3>{{ profile.username }}님의 프로필</h3>
      </div>
      <h2>저도 이 영화 좋아합니다</h2>
      <div class="row">
        <div v-for="movie in profile.like_movies" :key="movie.id"
        class="col-12 col-sm-4 col-md-3">
          <div class="card border mb-3">
            <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300/' + movie.poster_path" alt=""
              >
          </div>
          <div class="card-">
            <hr>
            <h5 class="card-">{{ movie.title }}</h5>  
          </div>  
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/templates/NavBar.vue"
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components: {
    NavBar
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>