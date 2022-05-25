<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <div class="container col-5 my-3 text-align:left">  
        <h3>{{ profile.username }}님의 프로필</h3>
      </div>
      <h2>저도 이 영화 좋아합니다</h2>
      <div class="row">
        <div v-for="movie in profile.like_movies" :key="movie.id"
        class="col-12 col-sm-4 col-md-3">
          <div class="card border mb-3">
            <img
              class="card-img-top"
              :src="'https://image.tmdb.org/t/p/w300/' + movie.poster_path" alt=""
              >
          </div>
          <div class="card-">
            <hr>
            <h5 class="card-">{{ movie.title }}</h5>  
          </div>  
        </div>
      </div>
    </div>
  </div>
</template>
  <!-- 

      <h2>작성글</h2>
      <div>
        <div v-for="article in profile.articles" :key="article.id">
          <router-link class='router' :to="{ name: 'article', params: { articlePk: article.id } }">
            {{ article.title }}
          </router-link>
        </div>
      </div>

      </div>
      <h2>이 글 맘에 드셨네요?</h2>
      <div>
        <div v-for="article in profile.like_articles" :key="article.id">
          <router-link class='router' :to="{ name: 'article', params: { articlePk: article.id } }">
            {{ article.title }}
          </router-link>
        </div>
      </div> -->

<script>
import NavBar from "@/components/templates/NavBar.vue"
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components: {
    NavBar
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  /* border: 1px solid black; */
}

#Profile {
  display: flex;
  align-items: center;
  margin-top: 4rem;
}

.profile-tab {
  border: 0.5px solid #4B4A54;
  border-radius: 10px;
  margin-top: 5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 500px;
  height: 500px;
  padding: 20px;
}


.input-div {
  display: flex;
  justify-content: center;
  padding: 10px;
  padding-left: 0;
}

.label {
  margin-right: 10px;
}

.input {
  font-size: 14px;
  border-radius: 5px;
  border: none;
}


.btn button {
  border: none;
  background-color: rgb(211, 47, 39);
  border-radius: 5px;
  font-weight: 600;
  color: #ffffff;
  margin-right: 10px;
}

.btn button:first-child {
  width: 70px;
  height: 30px;
  margin-left: 8px;
}


.go-home {
  border: none;
  border-radius: 5px;
  width: 100px;
  height: 30px;
}

.router {
  text-decoration: none;
  font-weight: 600;
}




</style>