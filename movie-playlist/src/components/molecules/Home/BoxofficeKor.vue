<template>
  <div class="home">
    <div>
      <div v-for="box in boxoffice" :key="box.rnum"
      >
      {{ box.rank }} {{ box.movieNm }} 
      <span v-if="box.rankOldAndNew == 'NEW'" >{{ box.rankOldAndNew }}</span>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"

export default {
  name: 'BoxofficeKor',
  computed: {
    ...mapGetters([
      'boxoffice'
    ]),
  },
}
</script>
