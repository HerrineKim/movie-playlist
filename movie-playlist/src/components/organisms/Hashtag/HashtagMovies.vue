<template>
  <div style="text-align:left;" class="container mt-4">
    <div>
      <h2>
        만들어보세요
      </h2>
    </div>
    <div>
      <!-- 장르별 태그 dropdown -->
      <div class="faq-content">
        <button @click="openCloseAnswer1('que-1')" class="question1 btn btn-outline-primary" id="que-1">
          <span id="que-1-toggle">+</span><span>장르별 태그</span>
        </button>
        <div class="answer" id="ans-1">
          <div class="container mt-3">
            <div style="text-align:left" class="container">
              <input class="form-check-input" id="crime" type="checkbox" v-model='checkedGenres' value="80">
              <label class="form-check-label" for="crime"><span>&#128184;</span>범죄</label>

              <input id="comedy" type="checkbox" v-model='checkedGenres' value="35">
              <label for="comedy"># 코미디</label>

              <input id="adventure" type="checkbox" v-model='checkedGenres' value="12">
              <label for="adventure"># 모험</label>

              <input id="action" type="checkbox" v-model='checkedGenres' value="28">
              <label for="action"># 액션</label>

              <input id="SF" type="checkbox" v-model='checkedGenres' value="878">
              <label for="SF"># SF</label>

              <input id="animation" type="checkbox" v-model='checkedGenres' value="16">
              <label for="animation"># 애니메이션</label>

              <input id="family" type="checkbox" v-model='checkedGenres' value="10751">
              <label for="family"># 가족</label>

              <input id="drama" type="checkbox" v-model='checkedGenres' value="18">
              <label for="drama"># 드라마</label>
      <br>
              <input id="romance" type="checkbox" v-model='checkedGenres' value="10749">
              <label for="romance"># 로맨스</label>

              <input id="mystery" type="checkbox" v-model='checkedGenres' value="9648">
              <label for="mystery"># 미스터리</label>

              <input id="fantasy" type="checkbox" v-model='checkedGenres' value="14">
              <label for="fantasy"># 판타지</label>

              <input id="thriller" type="checkbox" v-model='checkedGenres' value="53">
              <label for="thriller"># 스릴러</label>

              <input id="war" type="checkbox" v-model='checkedGenres' value="10752">
              <label for="war"># 전쟁</label>

              <input id="music" type="checkbox" v-model='checkedGenres' value="10402">
              <label for="music"># 음악</label>

              <input id="western" type="checkbox" v-model='checkedGenres' value="37">
              <label for="western"># 서부</label>

              <input id="TV 영화" type="checkbox" v-model='checkedGenres' value="10770">
              <label for="TV 영화"># TV 영화</label>

              <input id="horror" type="checkbox" v-model='checkedGenres' value="27">
              <label for="horror"># 공포</label>

              <input id="history" type="checkbox" v-model='checkedGenres' value="36">
              <label for="history"># 역사</label>

              <input id="documentary" type="checkbox" v-model='checkedGenres' value="99">
              <label for="documentary"># 다큐멘터리</label>
            </div>
          </div>
        </div>
      </div>
      <!-- 상황별 태그 dropdown -->
      <div class="mt-3 faq-content">
        <button @click="openCloseAnswer2('que-2')" class="question2 btn btn-outline-primary" id="que-2">
          <span id="que-2-toggle">+</span><span>상황별 태그</span>
        </button>
        <div class="answer" id="ans-2">
          <div class="container mt-3">
            <div style="text-align:left" class="container">
              <input id="withfamily" type="checkbox" v-model='checkedCasetags' value="1">
              <label for="withfamily"># 가족과 함께 보기</label>

              <input id="withfriends" type="checkbox" v-model='checkedCasetags' value="2">
              <label for="withfriends"># 친구와 함께 보기</label>      

              <input id="withlover" type="checkbox" v-model='checkedCasetags' value="3">
              <label for="withlover"># 썸남, 썸녀, 연인과 함께</label>   

              <input id="holidays" type="checkbox" v-model='checkedCasetags' value="4">
              <label for="holidays"># 연말에 따뜻함을 느끼고 싶을 때</label>

              <input id="spring" type="checkbox" v-model='checkedCasetags' value="5">
              <label for="spring"># 봄 한 송이</label>

              <input id="summer" type="checkbox" v-model='checkedCasetags' value="6">
              <label for="summer"># 여름 한 컵</label>

              <input id="fall" type="checkbox" v-model='checkedCasetags' value="7">
              <label for="fall"># 가을 한 장</label>

              <input id="winter" type="checkbox" v-model='checkedCasetags' value="8">
              <label for="winter"># 겨울 한 숨</label>

              <input id="travel" type="checkbox" v-model='checkedCasetags' value="9">
              <label for="travel"># 훌쩍 여행 떠나고 싶을 때</label>

              <input id="raining" type="checkbox" v-model='checkedCasetags' value="10">
              <label for="raining"># 비 올 때</label>

              <input id="food" type="checkbox" v-model='checkedCasetags' value="11">
              <label for="food"># 배고플 때 맛있는 음식과 함께</label>

            </div>
          </div>
        </div>
      </div>
      <!-- 기분별 태그 dropdown -->
      <div class="mt-3 faq-content">
        <button @click="openCloseAnswer3('que-3')" class="question3 btn btn-outline-primary" id="que-3">
          <span id="que-3-toggle">+</span><span>기분별 태그</span>
        </button>
        <div class="answer" id="ans-3">
          <div class="container mt-3">
            <div style="text-align:left" class="container">
              <div>
                <input id="cry" type="checkbox" v-model='checkedMoodtags' value="1">
                <label for="cry"># 펑펑 울고 싶을 때</label>

                <input id="down" type="checkbox" v-model='checkedMoodtags' value="2">
                <label for="down"># 기분 전환이 필요할 때</label>

                <input id="stress" type="checkbox" v-model='checkedMoodtags' value="3">
                <label for="stress"># 스트레스 뻥 뚫어버리기</label>

                <input id="dance" type="checkbox" v-model='checkedMoodtags' value="4">
                <label for="dance"># 댄스를 부르는</label>

                <input id="killingtime" type="checkbox" v-model='checkedMoodtags' value="5">
                <label for="killingtime"># 그냥 심심할 때 킬링타임</label>

                <input id="confidence" type="checkbox" v-model='checkedMoodtags' value="6">
                <label for="confidence"># 자존감 상승 시켜주는</label>

                <input id="butterfly" type="checkbox" v-model='checkedMoodtags' value="7">
                <label for="butterfly"># 두근두근 설레고 싶을 때</label>

                <input id="cinematic" type="checkbox" v-model='checkedMoodtags' value="8">
                <label for="cinematic"># 영상미 뿜뿜하는 영화</label>

                <input id="teen" type="checkbox" v-model='checkedMoodtags' value="9">
                <label for="teen"># 하이틴 시절이 생각나는</label>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 기분 태그 -->


    <!-- 무플리 만드는 버튼 -->
    <div>
      <button @click="fetchGenreMovies(), fetchMoodtagMovies(), fetchCasetagMovies()">
        나만의 무비플레이스트 만들기
      </button>
    </div>


    <!-- 기분별 플레이리스트 -->
    <div v-if="ok1" class="container py-3">
      <p>기분</p>
      <div class="row mt-5">
        <div v-for="movie in moodtag_movies.movies" :key="movie.poster_path" 
          class="col-12 col-sm-4 col-md-3"
          >
          <div class="card border mb-3">
              <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt=""
              >
            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">
                {{ movie.tagline }}
              </p>
            </div>
          </div>
        </div>  
      </div>
    </div>

    <!-- 상황별 플레이리스트 -->
    <div v-if="ok2" class="container py-3">
      <p>상황</p>
      <div class="row mt-5">
        <div v-for="movie in casetag_movies.movies" :key="movie.poster_path" 
          class="col-12 col-sm-4 col-md-3"
          >
          <div class="card border mb-3">
              <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt=""
              >
            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">
                {{ movie.tagline }}
              </p>
            </div>
          </div>
        </div>  
      </div>
    </div>

    <!-- 장르별 플레이리스트 -->
    <div v-if="ok3" class="container py-3">
      <p>장르</p>
      <div class="row mt-5">
        <div v-for="movie in genre_movies.movies" :key="movie.poster_path" 
          class="col-12 col-sm-4 col-md-3"
          >
          <div class="card border mb-3">
              <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt=""
              >
            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">
                {{ movie.tagline }}
              </p>      
            </div>
          </div>
        </div>  
      </div>
    </div>
    <!-- <div v-if="ok1">
      <li v-for="movie in moodtag_movies.movies" :key=movie.title>
        {{ movie.title}}
      </li>
    </div>
    <div v-if="ok2">
      <li v-for="movie in casetag_movies.movies" :key=movie.title>
        {{ movie.title}}
      </li>
    </div>
    <div v-if="ok3">
      <li v-for="movie in genre_movies.movies" :key=movie.title>
        {{ movie.title}}
      </li>
    </div> -->
  </div>

</template>

<script>
import movie from "@/api/movie"
import router from "@/router"

// 나중에 개수 제한 구현
export default {
  name: "HashtagMovies",
  data(){
    return{
      checkedGenres:[],
      checkedCasetags: [],
      checkedMoodtags:[],
      genre_movies: { id: "", movies: [] },
      moodtag_movies: { id: "", movies: [] },
      casetag_movies: { id: "", movies: [] },
      ok1: false,
      ok2: false,
      ok3: false,
    }
  },
  computed: {
    genrePk: function() {
      return this.checkedGenres[0]
    },
    moodtagPk: function() {
      return this.checkedMoodtags[0]
    },
    casetagPk: function() {
      return this.checkedCasetags[0]
    },
  },
  methods: {
    openCloseAnswer1(id1) {
      const answerId = id1.replace('que', 'ans')
      if(document.getElementById(answerId).style.display === 'block') {
        document.getElementById(answerId).style.display = 'none';
        document.getElementById(id1 + '-toggle').textContent = '+';
      } else {
        document.getElementById(answerId).style.display = 'block';
        document.getElementById(id1 + '-toggle').textContent = '-';
      }
    },
    openCloseAnswer2(id2) {
      const answerId2 = id2.replace('que', 'ans')
      if(document.getElementById(answerId2).style.display === 'block') {
        document.getElementById(answerId2).style.display = 'none';
        document.getElementById(id2 + '-toggle').textContent = '+';
      } else {
        document.getElementById(answerId2).style.display = 'block';
        document.getElementById(id2 + '-toggle').textContent = '-';
      }
    },
    openCloseAnswer3(id3) {
      const answerId3 = id3.replace('que', 'ans')
      if(document.getElementById(answerId3).style.display === 'block') {
        document.getElementById(answerId3).style.display = 'none';
        document.getElementById(id3 + '-toggle').textContent = '+';
      } else {
        document.getElementById(answerId3).style.display = 'block';
        document.getElementById(id3 + '-toggle').textContent = '-';
      }
    },
    fetchGenreMovies() {
      movie
        .genre(this.genrePk)
        .then((res) => {
          this.genre_movies = res.data
          this.ok3 = true
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    fetchCasetagMovies() {
      movie
        .casetag(this.casetagPk)
        .then((res) => {
          this.casetag_movies = res.data
          this.ok2 = true
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    fetchMoodtagMovies() {
      movie
        .moodtag(this.moodtagPk)
        .then((res) => {
          this.moodtag_movies = res.data
          this.ok1 = true
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
  },
}
</script>

<style scoped>
  .answer {
    display: none;
    padding-bottom: 30px;
  }
  #faq-title {
    font-size: 25px;
  }
  .faq-content {
    border-bottom: 1px solid #e0e0e0;
  }
  .question {
    font-size: 19px;
    padding: 30px 0;
    cursor: pointer;
    border: none;
    outline: none;
    background: none;
    width: 100%;
    text-align: left;
  }
  .question:hover {
    color: #2962ff;
  }
  [id$="-toggle"] {
    margin-right: 15px;
  }
</style>