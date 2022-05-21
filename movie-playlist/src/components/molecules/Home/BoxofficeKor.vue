<template>
  <div class="home">
    <div>
      <!-- <widgets-organism
        v-for="box in boxoffice"
        :key="box.rnum"
        :box="box"
      ></widgets-organism> -->
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
import { mapGetters, mapActions } from "vuex"
// import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
// import WidgetsOrganism from "@/components/organisms/Home/WidgetsOrganism.vue"

export default {
  name: 'BoxofficeKor',
  methods: {
    ...mapActions([
      'fetchBoxoffice'
    ])
  },
  computed: {
    ...mapGetters([
      'boxoffice'
    ]),
  },
  created () {
    this.fetchBoxoffice()
  },
}
</script>
