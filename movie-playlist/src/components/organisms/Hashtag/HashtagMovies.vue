<template>
  <div style="text-align:left;" class="container mt-4">
    <div style="margin-bottom:100px;text-align:left;font-family:MapoGoldenPier">
      <h2>
        태그를 선택하고
      </h2>
      <h2>
        나만의 <span style="color:#005aa7">무비플레이리스트</span>를
      </h2>
      <h2>
        만들어보세요
      </h2>
    </div>
    <div>
      <!-- 장르별 태그 dropdown -->
      <div class="faq-content">
        <button @click="openCloseAnswer1('que-1')" class="question1 btn btn-outline-primary" id="que-1">
          <span id="que-1-toggle">+</span>
          <span
          style="font-family:GmarketSansMedium;">
            장르별 태그</span>
        </button>
        <div class="answer" style="font-family:GmarketSansMedium;" id="ans-1">
          <div class="container mt-3">
            <div style="text-align:left" class="container">
              
              <label for="crime" class="check">
                <input type="checkbox" id="crime" v-model='checkedGenres' value="80">
                <p><span>&#128184;</span>범죄</p>
              </label>

              <label for="comedy" class="check" style="margin-right:10px">
                <input type="checkbox" id="comedy" v-model='checkedGenres' value="35">
                <p><span>&#128518;</span>코미디</p>
              </label>
              <label for="adventure" class="check">
                <input type="checkbox" id="adventure" v-model='checkedGenres' value="12">
                <p><span>&#128511;</span>모험</p>
              </label>

              <label for="action" class="check">
                <input type="checkbox" id="action" v-model='checkedGenres' value="28">
                <p><span>&#128170;</span>액션</p>
              </label>

              <label for="SF" class="check">
                <input type="checkbox" id="SF" v-model='checkedGenres' value="878">
                <p><span>&#128640;</span>SF</p>
              </label>

              <label for="animation" class="check">
                <input type="checkbox" id="animation" v-model='checkedGenres' value="16">
                <p><span>&#128060;</span>애니메이션</p>
              </label>

              <label for="family" class="check">
                <input type="checkbox" id="family" v-model='checkedGenres' value="10751">
                <p><span>&#128106;</span>가족</p>
              </label>

              <label for="drama" class="check">
                <input type="checkbox" id="drama" v-model='checkedGenres' value="18">
                <p><span>&#128250;</span>드라마</p>
              </label>

              <label for="romance" class="check">
                <input type="checkbox" id="romance" v-model='checkedGenres' value="10749">
                <p><span>&#128149;</span>로맨스</p>
              </label>

              <label for="mystery" class="check">
                <input type="checkbox" id="mystery" v-model='checkedGenres' value="9648">
                <p><span>&#128633;</span>미스터리</p>
              </label>

              <label for="fantasy" class="check">
                <input type="checkbox" id="fantasy" v-model='checkedGenres' value="14">
                <p><span>&#127776;</span>판타지</p>
              </label>

              <label for="thriller" class="check">
                <input type="checkbox" id="thriller" v-model='checkedGenres' value="53">
                <p><span>&#128551;</span>스릴러</p>
              </label>

              <label for="war" class="check">
                <input type="checkbox" id="war" v-model='checkedGenres' value="10752">
                <p><span>&#128130;</span>전쟁</p>
              </label>

              <label for="music" class="check">
                <input type="checkbox" id="music" v-model='checkedGenres' value="10402">
                <p><span>&#127932;</span>음악</p>
              </label>

              <label for="western" class="check">
                <input type="checkbox" id="western" v-model='checkedGenres' value="37">
                <p><span>&#128014;</span>서부</p>
              </label>

              <label for="TV 영화" class="check">
                <input type="checkbox" id="TV 영화" v-model='checkedGenres' value="10770">
                <p><span>&#128249;</span>TV 영화</p>
              </label>

              <label for="horror" class="check">
                <input type="checkbox" id="horror" v-model='checkedGenres' value="27">
                <p><span>&#128561;</span>공포</p>
              </label>

              <label for="history" class="check">
                <input type="checkbox" id="history" v-model='checkedGenres' value="36">
                <p><span>&#127886;</span>역사</p>
              </label>

              <label for="documentary" class="check">
                <input type="checkbox" id="documentary" v-model='checkedGenres' value="99">
                <p><span>&#127902;</span>다큐멘터리</p>
              </label>
              </div>
            </div>
          </div>
      </div>
      <!-- 상황별 태그 dropdown -->
      <div class="mt-3 faq-content">
        <button @click="openCloseAnswer2('que-2')" class="question2 btn btn-outline-primary" id="que-2">
          <span id="que-2-toggle"
          >+</span>
          <span           style="font-family:GmarketSansMedium;">
            상황별 태그</span>
        </button>
        <div class="answer" id="ans-2">
          <div class="container mt-3" style="font-family:GmarketSansMedium;">
            <div style="text-align:left" class="container">
              
              <label for="withfamily" class="check">
                <input type="checkbox" id="withfamily" v-model='checkedCasetags' value="1">
                <p><span>&#128106;</span>가족과 함께 보기</p>
              </label>

              <label for="withfriends" class="check">
                <input type="checkbox" id="withfriends" v-model='checkedCasetags' value="2">
                <p><span>&#128109;</span>친구와 함께 보기</p>
              </label>

              <label for="withlover" class="check">
                <input type="checkbox" id="withlover" v-model='checkedCasetags' value="3">
                <p><span>&#128145;</span>썸남, 썸녀, 연인과 함께</p>
              </label>

              <label for="holidays" class="check">
                <input type="checkbox" id="holidays" v-model='checkedCasetags' value="4">
                <p><span>&#128587;</span>연말에 따뜻함을 느끼고 싶을 때</p>
              </label>

              <label for="spring" class="check">
                <input type="checkbox" id="spring" v-model='checkedCasetags' value="5">
                <p><span>&#127801;</span>봄 한 송이</p>
              </label>

              <label for="summer" class="check">
                <input type="checkbox" id="summer" v-model='checkedCasetags' value="6">
                <p><span>&#127865;</span>여름 한 컵</p>
              </label>

              <label for="fall" class="check">
                <input type="checkbox" id="fall" v-model='checkedCasetags' value="7">
                <p><span>&#127809;</span>가을 한 장</p>
              </label>

              <label for="winter" class="check">
                <input type="checkbox" id="winter" v-model='checkedCasetags' value="8">
                <p><span>&#127788;</span>겨울 한 숨</p>
              </label>

              <label for="travel" class="check">
                <input type="checkbox" id="travel" v-model='checkedCasetags' value="9">
                <p><span>&#128747;</span>훌쩍 여행 떠나고 싶을 때</p>
              </label>

              <label for="raining" class="check">
                <input type="checkbox" id="raining" v-model='checkedCasetags' value="10">
                <p><span>&#127783;</span>비 올 때</p>
              </label>

              <label for="food" class="check">
                <input type="checkbox" id="food" v-model='checkedCasetags' value="11">
                <p><span>&#127828;</span>배고플 때 맛있는 음식과 함께</p>
              </label>
            </div>
          </div>
        </div>
      </div>

      <!-- 기분별 태그 dropdown -->
      <div class="mt-3 faq-content">
        <button @click="openCloseAnswer3('que-3')" class="question3 btn btn-outline-primary" id="que-3">
          <span id="que-3-toggle">+</span>
          <span
          style="font-family:GmarketSansMedium;"
          >기분별 태그</span>
        </button>
        <div class="answer" id="ans-3">
          <div class="container mt-3">
            <div
            style="text-align:left;font-family:GmarketSansMedium;"
            class="container">

              <label for="cry" class="check">
                <input type="checkbox" id="cry" v-model='checkedMoodtags' value="1">
                <p><span>&#128557;</span>펑펑 울고 싶을 때</p>
              </label>

              <label for="down" class="check">
                <input type="checkbox" id="down" v-model='checkedMoodtags' value="2">
                <p><span>&#128526;</span>기분 전환이 필요할 때</p>
              </label>

              <label for="stress" class="check">
                <input type="checkbox" id="stress" v-model='checkedMoodtags' value="3">
                <p><span>&#128170;</span>스트레스 뻥 뚫어버리기</p>
              </label>

              <label for="dancd" class="check">
                <input type="checkbox" id="dancd" v-model='checkedMoodtags' value="4">
                <p><span>&#127908;</span>댄스를 부르는</p>
              </label>

              <label for="killingtime" class="check">
                <input type="checkbox" id="killingtime" v-model='checkedMoodtags' value="5">
                <p><span>&#128541;</span>그냥 심심할 때 킬링타임</p>
              </label>

              <label for="confidence" class="check">
                <input type="checkbox" id="confidence" v-model='checkedMoodtags' value="6">
                <p><span>&#128513;</span>자존감 상승 시켜주는</p>
              </label>

              <label for="butterfly" class="check">
                <input type="checkbox" id="butterfly" v-model='checkedMoodtags' value="7">
                <p><span>&#128525;</span>두근두근 설레고 싶을 때</p>
              </label>

              <label for="cinematic" class="check">
                <input type="checkbox" id="cinematic" v-model='checkedMoodtags' value="8">
                <p><span>&#127751;</span>영상미 뿜뿜하는 영화</p>
              </label>

              <label for="teen" class="check">
                <input type="checkbox" id="teen" v-model='checkedMoodtags' value="9">
                <p><span>&#128107;</span>하이틴 시절이 생각나는</p>
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
    <!-- 무플리 만드는 버튼 -->
    <div>
      <button
      class="btn btn-lg btn-purple-moon"
      @click="fetchGenreMovies(), fetchMoodtagMovies(), fetchCasetagMovies()">
        만들기
      </button>
    </div>
    <br>
    <br>
        <p style="font-family:GmarketSansMedium">* 기분별, 상황별, 장르별 영화가 순서대로 표시됩니다.</p>

    <!-- 기분별 플레이리스트 -->
    <div v-if="ok1" class="container py-3">
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
              <h5 class="card-title" style="font-family:GmarketSansMedium">{{ movie.title }}</h5>
              <p class="card-text" style="font-family:GmarketSansMedium">
                {{ movie.tagline }}
              </p>
            </div>
          </div>
        </div>  
      </div>
    </div>

    <!-- 상황별 플레이리스트 -->
    <div v-if="ok2" class="container py-3">
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
              <h5 class="card-title" style="font-family:GmarketSansMedium">{{ movie.title }}</h5>
              <p class="card-text" style="font-family:GmarketSansMedium">
                {{ movie.tagline }}
              </p>
            </div>
          </div>
        </div>  
      </div>
    </div>

    <!-- 장르별 플레이리스트 -->
    <div v-if="ok3" class="container py-3">
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
              <h5 class="card-title" style="font-family:GmarketSansMedium">{{ movie.title }}</h5>
              <p class="card-text" style="font-family:GmarketSansMedium">
                {{ movie.tagline }}
              </p>      
            </div>
          </div>
        </div>  
      </div>
    </div>


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

  label.check {
  cursor: pointer;
  margin-right:10px;
  }
  label.check input {
    position: absolute;
    top: 0;
    left: 0;
    visibility: hidden;
    pointer-events: none;
  }
  label.check p {
    padding: 7px 14px;
      border: 2px solid #7474BF;
      display: inline-block;
      color: #7474BF;
      border-radius: 3px;
      text-transform: uppercase;
  }
  label.check input:checked + p {
    border-color: #7474BF;
      background-color: #7474BF;
      color: #fff;
  }

.btn-purple-moon {
    background: #7474BF;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #348AC7, #7474BF);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to right, #348AC7, #7474BF); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: #fff;
    font-family:MapoGoldenPier;
}
</style>