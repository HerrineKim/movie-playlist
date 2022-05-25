<template>
  <div class="home container">
    <div>
      <boxoffice-kor></boxoffice-kor>
    </div>
    <div>
      <random-ost></random-ost>
    </div>
    <div>
      <random-quotes></random-quotes>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"
import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
import RandomQuotes from '@/components/molecules/Home/RandomQuotes.vue'
import RandomOst from '@/components/molecules/Home/RandomOst.vue'

export default {
  name: 'WidgetsOrganism',
  components: {
    BoxofficeKor,
    RandomQuotes,
    RandomOst,
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