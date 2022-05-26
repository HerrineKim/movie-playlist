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
      <span style="line-height: font-family: 'GmarketSansMedium';">
        {{ box.rank }}
      </span> 
      <span style="font-family: 'GmarketSansMedium';">
        {{ box.movieNm }}
      </span>
      <span style="font-family: 'GmarketSansMedium';"
      v-if="box.rankOldAndNew == 'NEW'"
      >
        <button class=" btn btn-outline-primary btn-sm">
          {{ box.rankOldAndNew }}
        </button>
      </span>
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
    font-family: 'EarlyFontDiary';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EarlyFontDiary.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
</style>