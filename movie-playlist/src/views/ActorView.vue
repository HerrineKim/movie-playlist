<template>
  <div>
    <nav-bar></nav-bar>

    <div class="container">
      <br>
      <div class="container">
        <div class="row">
          <div class="col">
            <div class="box" style="background: #BDBDBD; display: block; margin: 0px auto">
              <img 
              class="actorImg" :src="'https://www.themoviedb.org/t/p/w150_and_h225_bestv2' + actor.profile_path" alt="">

            </div>
          </div>
          <span class="p-3" style="font-size:40px; font-family:GEORGIA;">
            {{ actor.name }}  
          </span>
        </div>

      </div>
    </div>
    <div>
      <p>필모그래피</p>
    </div>
    <div class="movies container py-3">
      <div class="row mt-5">
        <div v-for="movie in actor.movies" :key="movie.poster_path" 
          class="col-12 col-sm-4 col-md-3"
          >
          <div class="card border mb-3">
              <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt=""
              >
            <div class="card-body">
              <hr>
              <h5 class="card-title">{{ movie.title }}</h5>
            </div>
          </div>
        </div>  
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ActorView',
  components: { NavBar },
  data() {
    return {
      actorPk: ''
    }
  },
  computed: {
    ...mapGetters(['actor', 'currentUser']),
    actorImgUrl () {
      return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.actor.profile_path}`
    },
  },
  methods: {
    ...mapActions(['fetchActor'])
  },
  created() {
    this.actorPk = this.$route.params.actorPk
    this.fetchActor({ actorPk: this.actorPk })
  }
}
</script>

<style scoped>
  .box {
      width: 200px;
      height: 200px; 
      border-radius: 70%;
      overflow: hidden;
      box-shadow: 5px 5px 5px gray;
  }
  .actorImg {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }

</style>