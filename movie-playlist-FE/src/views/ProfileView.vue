<template>
  <div>
    <nav-bar></nav-bar>
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-md-9 col-lg-7 col-xl-5">
            <div class="card profile-box" style="border-radius: 15px;">
              <div class="card-body p-4">
                <div class="d-flex text-black">
                  <div class="flex-grow-1 ms-3">
                    <h5 class="mb-1" style="font-family: 'GimpoGothicBold00';">
                      {{ profile.username }} 님의 프로필</h5>
                    <div class="d-flex justify-content-start rounded-3 p-2 mt-2"
                      style="background-color: #efefef;">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    <div class="container my-5">
      <div style="text-align: left; margin-top:10px">
        <p style="font-size: 30px; font-family:'GEORGIA';">
          Likes
        </p>
      </div>
      <div class="row">
        <div v-for="movie in profile.like_movies" :key="movie.id"
        class="col-12 col-sm-4 col-md-3">
          <div  class="profile-box card border mb-3">
            <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt=""
              >
          </div>
          <div class="card-">
            <hr>
            <h5 class="card-" style="font-family: 'GimpoGothicBold00';">{{ movie.title }}</h5>  
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
  data() {
    return {
      // len: profile.like_movies.length()
    }
  },
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

<style scoped>
.profile-box {
  box-shadow : 3px 3px 3px 0;
}
</style>