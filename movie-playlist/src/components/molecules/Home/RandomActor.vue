<template>
  <div style="margin-right: 15px;"
  >
    <router-link :to="{ name: 'actor', params: { actorPk: randomActor[0].id } }">
      <img 
      class="profile" 
      :src="'https://www.themoviedb.org/t/p/w150_and_h225_bestv2' + randomActor[0].profile_path"
      alt="">
    </router-link>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: "RandomActor",
  data() {
    return {
      randomActor: []
    }
  },
  computed: {
    ...mapGetters(['actors'])
  },
  methods: {
    ...mapActions(['fetchActors']),
    pickActor() {
      var actor = _.sampleSize(this.actors, 1)
      this.randomActor = actor
    }

  },
  created() {
    this.pickActor()
  }
}
</script>

<style scoped>
.profile {
  width: 122%;
  border-radius: 30px;
  margin-right: 220px;
}

.container {
  text-align:left;
}

@font-face {
    font-family: 'GimpoGothicBold00';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2202-2@1.0/GimpoGothicBold00.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>