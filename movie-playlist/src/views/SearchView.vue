<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container mt-3">
      <img
      class=""
      style="width:50px;height:50px"
      src="@/assets/images/EnterImage.png"
      alt="엔터키 이미지"
      >
      <!-- 검색창 -->
      <br>
      <br>
      <div class="container col-5">
        <input
        class="form-control"
        id="searchbar"
        v-model="keyword"
        @keyup.enter="onInputKeyword"
        type="text"
        placeholder="찾고 싶은 영화를 입력하세요"
        >
      </div>

      <!-- 검색결과 -->
      <div class="row mt-5">
        <p style="font-size:18px; font-family:GmarketSansMedium; text-align:left">
          * 검색하신 제목과 유사도가 가장 높은 6개의 영화를 보여드립니다</p>
        <div v-for="movie in search" :key="movie.pk" 
        class="col-12 col-sm-4 col-md-3"
        >
          <div class="card border mb-3">
            <router-link
            :to="{ name: 'movieDetail', params: { moviePk: movie.pk } }"
            >
              <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300/' + movie.poster_path" alt=""
              >
            </router-link>
            <div class="card-body">
              <hr>
              <h5 style="font-family:GmarketSansMedium;" class="card-title">{{ movie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
      
      <!-- recommendationMovie -->
      <div class="row mt-5">
        <p style="font-size:18px; font-family:GmarketSansMedium; text-align:left">
          * 좋아요 누르신 영화를 기반으로 추천드리는 영화입니다 </p>
        <div v-for="recommendationMovie in recommendationMovies" :key="recommendationMovie.title" 
        class="col-12 col-sm-4 col-md-3"
        >
          <div class="card border mb-3">
            <router-link
            :to="{ name: 'movieDetail', params: { moviePk: recommendationMovie.pk } }"
            >
              <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300' + recommendationMovie.poster_path" alt=""
              >
            </router-link>
            <div class="card-body">
              <hr>
              <h5 style="font-family:GmarketSansMedium;" class="card-title">{{ recommendationMovie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/templates/NavBar.vue"
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'SearchView',
  components: {
    NavBar
  },
  data() {
    return {
      keyword: '',
      userPk: ''
    }
  },
  computed: {
    ...mapGetters(['search', 'currentUser', 'recommendationMovies'])
  },
  methods: {
    onInputKeyword() {
      const movieName = this.keyword
      this.$store.dispatch('search', movieName)
      // console.log(movieName)
      // console.log(this.keyword)
      // console.log(typeof movieName)
    },
    ...mapActions(['recommendation'])
  },
  created() {
    this.userPk = this.currentUser.pk
    this.recommendation({ userPk: this.userPk })
  }
}
</script>

<style>

</style>