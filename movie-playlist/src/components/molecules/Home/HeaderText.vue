<template>
  <div class="box">
    <p
    style="
    color:#696969;
    font-face:'LeferiPoint-WhiteObliqueA'; font-size:25px"
    >
      나의 작은 영화관
    </p>
    <p class="moply" style="
    color: #5d4157;
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
    font-family: 'LeferiPoint-WhiteObliqueA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/LeferiPoint-WhiteObliqueA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-family: 'MapoGoldenPier';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoGoldenPierA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

</style>