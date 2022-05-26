<template>
  <div class="box">
    <p
    style="
    color:#696969;
    font-family:'EarlyFontDiary'; font-size:25px"
    >
      나의 작은 영화관
    </p>
    <p class="moply" style="
    color: #005ea7;
    letter-spacing: 6px;
    font-family:'MapoGoldenPier'; font-size:42px">
      무비플레이리스트
    </p>
  </div>
</template>

<script>
export default {
  name: "HeaderText"
}
</script>

<style scoped>
.box {
  text-align: left;
  height: 100px;
  width: auto;
}

@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-family: 'EarlyFontDiary';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EarlyFontDiary.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
  font-family: 'MapoGoldenPier';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoGoldenPierA.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

</style>