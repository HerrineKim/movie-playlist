<template>
  <div class="boxoffice">
    <h3
    style="font-family: 'GimpoGothicBold00';"
    >
      박스오피스
    </h3>
    <div
    v-for="box in boxoffice" :key="box.rnum"
    >
      <span>
        {{ box.rank }}
      </span> 
      <span>
        {{ box.movieNm }}
      </span>
      <span
      v-if="box.rankOldAndNew == 'NEW'"
      >
        {{ box.rankOldAndNew }}
      </span>
      <hr>
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

<style scoped>
  .boxoffice {
    text-align: left;
  }
  @font-face {
    font-family: 'GimpoGothicBold00';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2202-2@1.0/GimpoGothicBold00.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
</style>