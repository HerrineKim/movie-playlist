<template>
  <div class="home container">
    <div style="width: auto; height: 50px;">
    </div>
    <div class="pb-5">
      <header-text></header-text>
    </div>
    <div class="row row-cols-2">
      <div class="col py-5 px-3">
        <boxoffice-kor></boxoffice-kor>
      </div>
      <div class="col py-5 px-3 mt-3">
        <random-ost></random-ost>
      </div>
      <div class="col py-3">
        <random-quotes></random-quotes>
      </div>
      <div class="col py-3 px-3">
        <random-actor></random-actor>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"
import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
import RandomQuotes from '@/components/molecules/Home/RandomQuotes.vue'
import RandomActor from '@/components/molecules/Home/RandomActor.vue'
import RandomOst from '@/components/molecules/Home/RandomOst.vue'
import HeaderText from '@/components/molecules/Home/HeaderText.vue'

export default {
  name: 'WidgetsOrganism',
  components: {
    BoxofficeKor,
    RandomQuotes,
    RandomActor,
    RandomOst,
    HeaderText
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