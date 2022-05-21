<template>
  <div class="home">
    <boxoffice-kor></boxoffice-kor>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"
import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
// import WidgetsOrganism from "@/components/organisms/Home/WidgetsOrganism.vue"

export default {
  name: 'WidgetsOrganism',
  components: {
    BoxofficeKor,
  },
  computed: {
    ...mapGetters([
      'boxoffice'
    ]),
  },
}
</script>
