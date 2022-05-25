<template>
  <div class="container">
    <p style="font-family: 'GimpoGothicBold00';">이 배우, 만나보실래요?</p>
    <router-link :to="{ name: 'actor', params: { actorPk: randomActor[0].id } }">
      <div class="box" style="backgroud: #FFFF">
        <img class="profile" :src="'https://www.themoviedb.org/t/p/w150_and_h225_bestv2' + randomActor[0].profile_path" alt="">
      </div>
    </router-link>
    <br>
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
    this.fetchActors()
    this.pickActor()
  }
}
</script>

<style scoped>
.box {
  width: 150px;
  height: 225px;
  border-radius: 20%;
  overflow: hidden;
}

.profile {
  width: 100%;
  height: 100%;
  object-fit: cover;
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