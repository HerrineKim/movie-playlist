<template>
  <div class="actors">
    <nav-bar></nav-bar>
    <div class="container">
      <br>
      <p style="font-size:40px; font-family:EarlyFontDiary;">
        PEOPLE
      </p>
      <br>
      <br>

      <!-- 배우 목록 -->
      <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
          <div class="col" v-for="actor in actors" :key="actor.id">
            <div class="box" style="background: #BDBDBD;">
            <router-link :to="{ name: 'actor', params: { actorPk: actor.id } }">
              <img class="actorImg" :src="'https://www.themoviedb.org/t/p/w150_and_h225_bestv2' + actor.profile_path" alt="">
            </router-link>
            </div>
            <span style="font-family: GEORGIA">{{ actor.name}}</span>
            <hr>
          </div>      
        </div>
      </div>
    </div>



  </div>
  
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ActorsView',
  components: { NavBar
  },
  computed: {
    ...mapGetters(['actors'])
  },
  methods: {
    ...mapActions(['fetchActors'])
  },
  created() {
  },
}
</script>

<style scoped>
  .box {
      width: 150px;
      height: 150px; 
      border-radius: 70%;
      overflow: hidden;
      box-shadow: 5px 5px 5px gray;
  }
  .actorImg {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }

  @font-face {
    font-family: "GEORGIA";
    font-weight: 400;
    src: url("@/assets/fonts/GEORGIA.TTF") format("ttf");
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-family: 'EarlyFontDiary';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EarlyFontDiary.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
    font-family: 'MapoGoldenPier';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoGoldenPierA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

  @font-face {
    font-family: 'EarlyFontDiary';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EarlyFontDiary.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
  }
</style>