<template>
  <div class="home container">
    <header-image class="image"></header-image>
    <boxoffice-kor></boxoffice-kor>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"
import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
import HeaderImage from '@/components/molecules/Home/HeaderImage.vue'

export default {
  name: 'WidgetsOrganism',
  components: {
    BoxofficeKor,
    HeaderImage,
  },
  computed: {
    ...mapGetters([
      'boxoffice'
    ]),
  },
}
</script>

<style scoped>
  .image {
    width: 100px;
    height: 100%;
  }
</style>