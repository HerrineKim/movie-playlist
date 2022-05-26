<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <!-- 영화 detail -->
      <div class="mt-5">
        <h1 style="font-size:70px; font-family:GimpoGothicBold00">{{ movie.title }}</h1>
      </div>
      <div style="font-size:19px; font-family:GmarketSansMedium;" class="mt-5 container row">
        <div class="mt-2 col-6">
          <img
          style="border-radius: 10px; box-shadow: 1px 1px 1px 0" 
          :src="'https://image.tmdb.org/t/p/w400/' + movie.poster_path" alt="">
        </div>
        <div class="col-6"
        style="margin-top:0; text-align:left;">
          <hr>

            <p>
              <span style="color: #808080">
                장르 |
              </span>
              <span 
              v-for="genre in movie.genres" :key="genre">
                {{ genre.name }},
              </span>
            </p>
            <p>
              <span style="color: #808080">
                개봉일 |
              </span>
              {{ movie.release_date | yyyyMMdd }}
            </p>
            <p>
              <span style="color: #808080">
                상영시간 |
              </span>
              {{ movie.runtime }}분
            </p>

          <div>
            <p>
              <span style="color: #808080">
                배우 |
              </span>
              <span v-for="actor in movie.actors" :key="actor">
                {{ actor.name }},
              </span>
            </p>
          </div>
          <p>
            <span style="color: #808080">줄거리 |</span>
            {{ movie.overview}}
          </p>
          <hr>
        </div>
      </div>

      <!-- 좋아요 -->
      <div class="mt-5"
      style="font-family:MapoGoldenPier; float:right; margin-right:20px;">
        <span>
          <div v-if="is_liked">
            <i class="fas fa-heart"
            @click="likeMovie"
            >
            </i>
          </div>
          <div v-else>
            <i class="far fa-heart"
            @click="likeMovie"
            >
            </i>
          </div>
        </span>
      </div>
      <!-- 평점 -->
      <div class="container" style="margin-top:150px">
        <hr>
        <rating-list :ratings="movie.ratings"></rating-list>
      </div>
      
      <!-- 비슷한 영화 -->
      <div class="row mt-5">
          <p style="font-size: 18px; font-family:GmarketSansMedium; text-align:left">
            * 이 영화를 재미있게 봤다면?
          </p>
          <div v-for="sim in similarMovies" :key="sim.poster_path" 
          class="col-12 col-sm-4 col-md-3"
          >
            <div class="card border mb-3">
              <router-link
              :to="{ name: 'movieDetail', params: { moviePk: sim.pk } }"
              >
                <img
                class="card-img-top"
                :src="'https://image.tmdb.org/t/p/w300/' + sim.poster_path" alt=""
                >
              </router-link>
              <div style="font-size:13px; font-family: 'GimpoGothicBold00';" class="card-body">
                <hr>
                <h5 class="card-title">{{ sim.title }}</h5>
              </div>
            </div>
          </div>
        </div>
    </div> 
  </div>
</template>

<script>
import RatingList from "@/components/organisms/MovieDetail/RatingList.vue"
import NavBar from '@/components/templates/NavBar.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieDetailView',
  components: {
    RatingList, NavBar
  },
  filters : {  
          // filter로 쓸 filter ID 지정
    yyyyMMdd : function(value){ 
            // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
            if(value == '') return '';
        
            // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
            var js_date = new Date(value);

            // 연도, 월, 일 추출
            var year = js_date.getFullYear();
            var month = js_date.getMonth() + 1;
            var day = js_date.getDate();

            // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
            if(month < 10){
              month = '0' + month;
            }

            if(day < 10){
              day = '0' + day;
            }

            // 최종 포맷 (ex - '2021-10-08')
            return year + '-' + month + '-' + day;
    }
  },
  data() {
    return {
      is_liked: false,
      score: null,
      newRate: {
        moviePk: '',
        rate: null
      }
    }
  },
  computed: {
    ...mapGetters(['movie', 'similarMovies']),

  },
  methods: {
    ...mapActions(['similar', 'fetchMovie']),
    likeMovie() {
      const moviePk = this.moviePk
      this.$store.dispatch('movieLike', moviePk)
      this.is_liked = !this.is_liked
    },
  },
  created() {
    this.moviePk = this.$route.params.moviePk
    // console.log(this.moviePk)
    this.fetchMovie({ moviePk: this.moviePk })
    console.log(this.movie)
    this.similar({ moviePk: this.moviePk })
  }
}
</script>

<style>
  .fa-heart {
    font-size:50px;
    color: #cb2d3e
  }
</style>