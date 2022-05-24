<template>
  <div class="home container">
    <div></div>
    <boxoffice-kor></boxoffice-kor>
    <!-- <theatre-map></theatre-map> -->
    <random-quotes></random-quotes>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"
import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
// import TheatreMap from '@/components/molecules/Home/TheatreMap.vue'
import RandomQuotes from '@/components/molecules/Home/RandomQuotes.vue'

export default {
  name: 'WidgetsOrganism',
  components: {
    BoxofficeKor,
    // TheatreMap,
    RandomQuotes,
  },
  computed: {
    ...mapGetters([
      'boxoffice'
    ]),
  },
}
</script>

<style scoped>
</style>