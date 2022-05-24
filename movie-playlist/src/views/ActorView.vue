<template>
  <div>
    <h2>영화배우 detail 화면</h2>
    <p>{{ actor.name }}</p>
    <img :src="actorImgUrl">
    <span v-for="movie in actor.movies" :key="movie">
      {{movie.title}}
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ActorView',
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

<style>

</style>